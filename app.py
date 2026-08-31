import streamlit as st
import math
import os


# ============================================================
# COUNT OR BREAK — POSITIONSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# KONFIGURATION
# ============================================================

GOLD = "#D6A82C"
GOLD_LIGHT = "#F4D477"
GOLD_BRIGHT = "#FFD866"
GOLD_DARK = "#9D7415"

BLACK = "#050505"
BLACK_2 = "#0A0A0A"
PANEL = "#0D0D0D"
PANEL_2 = "#111111"
BORDER = "#3A3A3A"
TEXT = "#F1F1F1"
TEXT_MUTED = "#B8B8B8"


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def find_asset(candidates):
    """
    Sucht ein Bild unter mehreren möglichen Dateinamen.
    Dadurch funktioniert die App auch dann, wenn die hochgeladenen
    Icon-Dateien leicht anders benannt wurden.
    """
    possible_dirs = [
        ".",
        "assets",
        "images",
        "icons",
        "static",
    ]

    for directory in possible_dirs:
        for filename in candidates:
            path = os.path.join(directory, filename)
            if os.path.isfile(path):
                return path

    return None


def euro(value):
    """Deutsche Zahlenformatierung."""
    try:
        return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "0,00"


def number_de(value, decimals=2):
    try:
        return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")
    except Exception:
        return "0"


def calculate_forex(
    account_size,
    risk_percent,
    entry,
    stop_loss,
    contract_size,
    pip_size,
    conversion_rate,
):
    """
    Berechnung für Forex-CFDs.

    conversion_rate:
    Wert der Kurswährung in Kontowährung.
    Beispiel EUR-Konto / EURUSD:
    USD -> EUR ≈ 0,855
    """

    stop_distance_price = abs(entry - stop_loss)

    if pip_size <= 0:
        return None

    stop_pips = stop_distance_price / pip_size

    max_loss = account_size * (risk_percent / 100)

    if stop_pips <= 0:
        return None

    # Pip-Wert eines Standard-Lots in Kurswährung
    pip_value_quote_per_lot = contract_size * pip_size

    # Umrechnung in Kontowährung
    pip_value_account_per_lot = (
        pip_value_quote_per_lot * conversion_rate
    )

    if pip_value_account_per_lot <= 0:
        return None

    lots = max_loss / (
        stop_pips * pip_value_account_per_lot
    )

    # Einheiten
    units = lots * contract_size

    # Nominaler Positionswert in Basiswährung
    position_value = units * entry

    # Tatsächlicher Positionswert in Kontowährung
    position_value_account = position_value * conversion_rate

    return {
        "lots": lots,
        "units": units,
        "stop_pips": stop_pips,
        "max_loss": max_loss,
        "pip_value": pip_value_account_per_lot * lots,
        "position_value": position_value_account,
    }


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Montserrat', sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 15%,
                rgba(214,168,44,0.055),
                transparent 30%
            ),
            linear-gradient(
                180deg,
                #020202 0%,
                #050505 45%,
                #030303 100%
            );
        color: {TEXT};
    }}

    .block-container {{
        max-width: 1500px;
        padding-top: 2rem;
        padding-bottom: 4rem;
    }}

    /* ========================================================
       HEADER
       ======================================================== */

    .cb-header {{
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 26px;
    }}

    .cb-header-icon {{
        width: 92px;
        height: 92px;
        border-radius: 19px;

        display: flex;
        align-items: center;
        justify-content: center;

        border: 1px solid rgba(214,168,44,0.85);

        background:
            radial-gradient(
                circle at 50% 40%,
                rgba(214,168,44,0.16),
                rgba(0,0,0,0.85) 70%
            );

        box-shadow:
            0 0 12px rgba(214,168,44,0.28),
            inset 0 0 22px rgba(214,168,44,0.06);
    }}

    .cb-header-icon img {{
        width: 67px;
        height: 67px;
        object-fit: contain;
    }}

    /* ========================================================
       TITLE
       ======================================================== */

    .cb-title-box {{
        width: 100%;
        min-height: 125px;

        border: 1px solid {GOLD};
        border-radius: 15px;

        background:
            linear-gradient(
                180deg,
                rgba(24,24,24,0.94),
                rgba(5,5,5,0.98)
            );

        box-shadow:
            0 0 9px rgba(214,168,44,0.23),
            inset 0 0 35px rgba(214,168,44,0.025);

        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;

        position: relative;
        overflow: hidden;

        margin-bottom: 26px;
    }}

    .cb-title-box::before,
    .cb-title-box::after {{
        content: "";
        position: absolute;
        width: 115px;
        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD},
                transparent
            );

        top: 50%;
    }}

    .cb-title-box::before {{
        left: 4%;
    }}

    .cb-title-box::after {{
        right: 4%;
    }}

    .cb-title {{
        font-family: 'Cinzel', serif;
        font-size: clamp(28px, 4vw, 48px);
        font-weight: 600;
        letter-spacing: 3px;

        background:
            linear-gradient(
                180deg,
                {GOLD_LIGHT},
                {GOLD},
                #B98216
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        text-shadow:
            0 0 18px rgba(214,168,44,0.20);

        text-align: center;
        z-index: 2;
    }}

    .cb-subtitle {{
        color: #E9D78F;
        font-family: 'Montserrat', sans-serif;
        font-size: 21px;
        font-weight: 400;
        letter-spacing: 1px;
        margin-top: 3px;
        z-index: 2;
    }}

    /* ========================================================
       PANELS
       ======================================================== */

    .cb-panel {{
        width: 100%;
        height: 100%;

        border: 1px solid #363636;
        border-radius: 15px;

        background:
            linear-gradient(
                145deg,
                rgba(20,20,20,0.97),
                rgba(5,5,5,0.98)
            );

        box-shadow:
            inset 0 0 35px rgba(255,255,255,0.012),
            0 0 8px rgba(0,0,0,0.8);

        padding: 27px 27px 30px 27px;
        box-sizing: border-box;
    }}

    .cb-panel-title {{
        display: flex;
        align-items: center;
        gap: 13px;

        font-family: 'Cinzel', serif;
        font-size: 23px;
        font-weight: 500;

        color: {GOLD_LIGHT};
        letter-spacing: 1px;

        margin-bottom: 24px;
    }}

    .cb-panel-icon {{
        width: 30px;
        height: 30px;

        display: flex;
        align-items: center;
        justify-content: center;

        color: {GOLD};
        font-size: 24px;

        filter:
            drop-shadow(
                0 0 5px rgba(214,168,44,0.45)
            );
    }}

    .cb-panel-icon img {{
        width: 29px;
        height: 29px;
        object-fit: contain;
    }}

    /* ========================================================
       STREAMLIT INPUTS
       ======================================================== */

    .stSelectbox label,
    .stNumberInput label,
    .stTextInput label {{
        color: #E8E8E8 !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 15px !important;
        font-weight: 400 !important;
    }}

    div[data-baseweb="select"] > div {{
        background: #111111 !important;
        border: 1px solid #5A4925 !important;
        border-radius: 8px !important;
        color: white !important;
        min-height: 50px !important;
    }}

    div[data-baseweb="select"] span {{
        color: #F1F1F1 !important;
    }}

    div[data-baseweb="input"] {{
        background: #111111 !important;
        border: 1px solid #4D4D4D !important;
        border-radius: 8px !important;
    }}

    div[data-baseweb="input"]:focus-within {{
        border-color: {GOLD} !important;
        box-shadow: 0 0 8px rgba(214,168,44,0.18) !important;
    }}

    div[data-baseweb="input"] input {{
        color: white !important;
        background: transparent !important;
    }}

    /* ========================================================
       LONG / SHORT
       ======================================================== */

    .direction-label {{
        color: #E8E8E8;
        font-size: 15px;
        margin-bottom: 8px;
    }}

    .direction-active button {{
        background:
            linear-gradient(
                180deg,
                #705819,
                #49390F
            ) !important;

        border: 1px solid {GOLD} !important;
        color: white !important;
    }}

    .stButton > button {{
        width: 100%;
        min-height: 50px;

        background: #111111;
        color: #F0F0F0;

        border: 1px solid #4B4B4B;
        border-radius: 8px;

        font-family: 'Montserrat', sans-serif;
        font-size: 16px;

        transition:
            all 0.18s ease;
    }}

    .stButton > button:hover {{
        border-color: {GOLD};
        color: {GOLD_LIGHT};

        transform: translateY(-1px);

        box-shadow:
            0 0 12px rgba(214,168,44,0.16);
    }}

    /* ========================================================
       RESULT
       ======================================================== */

    .cb-result-title {{
        text-align: center;

        font-family: 'Cinzel', serif;
        color: {GOLD_LIGHT};

        font-size: 25px;
        font-weight: 500;
        letter-spacing: 1px;

        margin-top: 7px;
        margin-bottom: 8px;
    }}

    .cb-result-title::before,
    .cb-result-title::after {{
        content: "";
        display: inline-block;

        width: 90px;
        height: 1px;

        vertical-align: middle;
        margin: 0 17px;

        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD},
                transparent
            );
    }}

    .cb-result-value {{
        text-align: center;

        font-family: 'Montserrat', sans-serif;

        font-size: clamp(48px, 5vw, 72px);
        line-height: 1;

        font-weight: 700;

        background:
            linear-gradient(
                180deg,
                #FFF0A8,
                {GOLD_LIGHT},
                #D99C20
            );

        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;

        text-shadow:
            0 0 12px rgba(255,210,70,0.25),
            0 0 28px rgba(214,168,44,0.18);

        margin: 22px 0 14px 0;
    }}

    .cb-units {{
        text-align: center;

        color: #F2F2F2;

        font-size: 25px;
        font-weight: 400;

        margin-bottom: 28px;
    }}

    .cb-divider {{
        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(214,168,44,0.42),
                transparent
            );

        margin: 15px 0 18px 0;
    }}

    /* ========================================================
       RESULT ROWS
       ======================================================== */

    .cb-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;

        padding: 11px 0;

        border-bottom: 1px solid rgba(255,255,255,0.075);

        font-size: 17px;
    }}

    .cb-row-label {{
        color: #E6E6E6;
    }}

    .cb-row-value {{
        color: {GOLD_LIGHT};
        font-weight: 500;
        text-align: right;
    }}

    /* ========================================================
       SECTION HEADERS
       ======================================================== */

    .cb-section-title {{
        display: flex;
        align-items: center;
        gap: 10px;

        color: {GOLD_LIGHT};

        font-family: 'Cinzel', serif;
        font-size: 22px;
        font-weight: 500;

        letter-spacing: 0.5px;

        margin-top: 27px;
        margin-bottom: 11px;
    }}

    /* ========================================================
       RISK OVERVIEW
       ======================================================== */

    .cb-risk-panel {{
        margin-top: 22px;

        border: 1px solid #363636;
        border-radius: 15px;

        background:
            linear-gradient(
                145deg,
                rgba(19,19,19,0.98),
                rgba(5,5,5,0.98)
            );

        padding: 25px 28px;
    }}

    .cb-risk-title {{
        font-family: 'Cinzel', serif;
        color: {GOLD_LIGHT};

        font-size: 22px;
        letter-spacing: 1px;

        margin-bottom: 17px;
    }}

    .cb-risk-content {{
        display: flex;
        align-items: center;
        gap: 35px;
    }}

    .cb-risk-circle {{
        min-width: 125px;
        width: 125px;
        height: 125px;

        border-radius: 50%;

        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;

        border: 9px solid #3B3B3B;

        box-shadow:
            inset 0 0 20px rgba(0,0,0,0.8),
            0 0 10px rgba(214,168,44,0.08);
    }}

    .cb-risk-percent {{
        color: {GOLD_LIGHT};
        font-size: 26px;
        font-weight: 500;
    }}

    .cb-risk-text {{
        font-size: 19px;
        line-height: 1.5;
    }}

    .cb-risk-money {{
        color: {GOLD_LIGHT};
        font-size: 23px;
        font-weight: 500;
    }}

    /* ========================================================
       WARNING
       ======================================================== */

    .cb-warning {{
        margin-top: 20px;

        border: 1px solid #806014;
        border-radius: 15px;

        background:
            linear-gradient(
                145deg,
                rgba(19,19,19,0.98),
                rgba(5,5,5,0.98)
            );

        padding: 22px 27px;
    }}

    .cb-warning-title {{
        font-family: 'Cinzel', serif;

        color: {GOLD_LIGHT};

        font-size: 21px;
        letter-spacing: 1px;

        margin-bottom: 8px;
    }}

    .cb-warning-text {{
        color: #E4E4E4;
        font-size: 14px;
        line-height: 1.65;
    }}

    /* ========================================================
       FOOTER
       ======================================================== */

    .cb-footer {{
        text-align: center;
        margin-top: 28px;

        color: #777;

        font-size: 12px;
        letter-spacing: 1px;
    }}

    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 900px) {{

        .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}

        .cb-title {{
            font-size: 29px;
            letter-spacing: 1.5px;
        }}

        .cb-title-box::before,
        .cb-title-box::after {{
            display: none;
        }}

        .cb-result-title::before,
        .cb-result-title::after {{
            width: 30px;
            margin: 0 8px;
        }}

        .cb-result-value {{
            font-size: 50px;
        }}

        .cb-risk-content {{
            flex-direction: column;
            align-items: flex-start;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ASSETS
# ============================================================

calculator_icon = find_asset([
    "calculator.png",
    "rechner.png",
    "positionsgroessenrechner.png",
    "positionsgrößenrechner.png",
    "icon_rechner.png",
    "icon_calculator.png",
])


# ============================================================
# HEADER
# ============================================================

if calculator_icon:
    st.markdown(
        f"""
        <div class="cb-header">
            <div class="cb-header-icon">
                <img src="{calculator_icon}">
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
else:
    st.markdown(
        """
        <div class="cb-header">
            <div class="cb-header-icon">
                <span style="font-size:42px;">▦</span>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# TITEL
# ============================================================

st.markdown(
    """
    <div class="cb-title-box">

        <div class="cb-title">
            POSITIONSGRÖSSENRECHNER
        </div>

        <div class="cb-subtitle">
            Risk first. Profits second.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HAUPTBEREICH
# WICHTIG: ALLE TRADE-EINGABEN LIEGEN INNERHALB DES LINKEN PANELS
# ============================================================

left_col, right_col = st.columns(
    [0.95, 1.25],
    gap="large"
)


# ============================================================
# LINKER BEREICH — TRADE-EINGABEN
# ============================================================

with left_col:

    st.markdown(
        """
        <div class="cb-panel">

            <div class="cb-panel-title">
                <div class="cb-panel-icon">⚖</div>
                <div>TRADE-EINGABEN</div>
            </div>

        """,
        unsafe_allow_html=True,
    )

    instrument = st.selectbox(
        "Instrument",
        [
            "EUR/USD",
            "GBP/USD",
            "USD/JPY",
            "AUD/USD",
            "USD/CAD",
            "USD/CHF",
            "NZD/USD",
            "XAU/USD – Gold",
            "US500",
            "NAS100",
            "GER40",
            "UK100",
            "BTC/USD",
            "ETH/USD",
        ],
        index=0,
    )

    direction_col1, direction_col2 = st.columns(2)

    with direction_col1:
        long_selected = st.button(
            "↗  LONG",
            use_container_width=True,
            key="long_button",
        )

    with direction_col2:
        short_selected = st.button(
            "↓  SHORT",
            use_container_width=True,
            key="short_button",
        )

    if "direction" not in st.session_state:
        st.session_state.direction = "LONG"

    if long_selected:
        st.session_state.direction = "LONG"

    if short_selected:
        st.session_state.direction = "SHORT"

    st.markdown(
        f"""
        <div style="
            margin-top:-4px;
            margin-bottom:15px;
            color:{GOLD};
            font-size:13px;
            text-align:center;
            letter-spacing:0.5px;
        ">
            AKTUELLE RICHTUNG: {st.session_state.direction}
        </div>
        """,
        unsafe_allow_html=True,
    )

    account_size = st.number_input(
        "Kontogröße",
        min_value=1.0,
        value=10000.0,
        step=100.0,
        format="%.2f",
    )

    risk_percent = st.number_input(
        "Risiko pro Trade",
        min_value=0.01,
        max_value=100.0,
        value=1.0,
        step=0.1,
        format="%.2f",
    )

    entry_price = st.number_input(
        "Einstiegskurs",
        min_value=0.00001,
        value=1.17000,
        step=0.00001,
        format="%.5f",
    )

    stop_price = st.number_input(
        "Stop-Loss Kurs",
        min_value=0.00001,
        value=1.16500,
        step=0.00001,
        format="%.5f",
    )

    account_currency = st.selectbox(
        "Kontowährung",
        [
            "EUR",
            "USD",
            "GBP",
            "CHF",
            "JPY",
        ],
        index=0,
    )

    st.markdown(
        "<div style='height:5px'></div>",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div style="
            color:#777;
            font-size:12px;
            line-height:1.5;
            margin-top:4px;
            margin-bottom:8px;
        ">
            Die Berechnung ist für CFDs und Forex geeignet.
            Für Pepperstone können Kontraktgröße, Pip-Größe und
            Umrechnung individuell angepasst werden.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ========================================================
    # TECHNISCHE PARAMETER
    # ========================================================

    if instrument == "XAU/USD – Gold":
        default_contract = 100.0
        default_pip = 0.01
    elif instrument in ["US500", "NAS100", "GER40", "UK100"]:
        default_contract = 1.0
        default_pip = 1.0
    elif instrument in ["BTC/USD", "ETH/USD"]:
        default_contract = 1.0
        default_pip = 1.0
    else:
        default_contract = 100000.0
        default_pip = 0.0001

    contract_size = st.number_input(
        "Kontraktgröße pro Lot",
        min_value=0.0001,
        value=float(default_contract),
        step=float(default_contract),
    )

    pip_size = st.number_input(
        "Pip-/Tick-Größe",
        min_value=0.000001,
        value=float(default_pip),
        format="%.6f",
    )

    conversion_rate = st.number_input(
        "Umrechnung in Kontowährung",
        min_value=0.000001,
        value=0.855,
        step=0.001,
        format="%.4f",
        help=(
            "Beispiel EUR-Konto / EURUSD: "
            "USD → EUR ungefähr 0,855. "
            "Bei CFDs auf andere Basis-/Kurswährungen "
            "entsprechend anpassen."
        ),
    )

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# BERECHNUNG
# ============================================================

result = calculate_forex(
    account_size=account_size,
    risk_percent=risk_percent,
    entry=entry_price,
    stop_loss=stop_price,
    contract_size=contract_size,
    pip_size=pip_size,
    conversion_rate=conversion_rate,
)


# ============================================================
# RECHTER BEREICH — ERGEBNIS
# ============================================================

with right_col:

    st.markdown(
        """
        <div class="cb-panel">

            <div class="cb-panel-title">
                <div class="cb-panel-icon">◎</div>
                <div>ERGEBNIS</div>
            </div>
        """,
        unsafe_allow_html=True,
    )

    if result is None:

        st.markdown(
            """
            <div style="
                text-align:center;
                padding:100px 20px;
                color:#999;
                font-size:17px;
            ">
                Bitte Einstiegskurs und Stop-Loss prüfen.
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        lots = result["lots"]
        units = result["units"]
        stop_pips = result["stop_pips"]
        max_loss = result["max_loss"]
        pip_value = result["pip_value"]
        position_value = result["position_value"]

        st.markdown(
            f"""
            <div class="cb-result-title">
                EMPFOHLENE POSITION
            </div>

            <div class="cb-result-value">
                {number_de(lots, 2)} LOTS
            </div>

            <div class="cb-units">
                = {number_de(units, 0)} EINHEITEN
            </div>

            <div class="cb-divider"></div>

            <div class="cb-row">
                <div class="cb-row-label">
                    Max. Verlust
                </div>
                <div class="cb-row-value">
                    {euro(max_loss)} {account_currency}
                </div>
            </div>

            <div class="cb-row">
                <div class="cb-row-label">
                    Stop-Abstand
                </div>
                <div class="cb-row-value">
                    {number_de(stop_pips, 1)} Pips
                </div>
            </div>

            <div class="cb-row">
                <div class="cb-row-label">
                    Positionswert
                </div>
                <div class="cb-row-value">
                    {euro(position_value)} {account_currency}
                </div>
            </div>

            <div class="cb-row">
                <div class="cb-row-label">
                    Pip-Wert
                </div>
                <div class="cb-row-value">
                    {euro(pip_value)} {account_currency}
                </div>
            </div>

            <div class="cb-row">
                <div class="cb-row-label">
                    Risikoprozent
                </div>
                <div class="cb-row-value">
                    {number_de(risk_percent, 2)} %
                </div>
            </div>

            <div class="cb-section-title">
                ⚖ &nbsp; MARGIN &amp; HEBEL
            </div>

            <div class="cb-row">
                <div class="cb-row-label">
                    Erforderliche Margin
                </div>
                <div class="cb-row-value">
                    Wird abhängig vom Broker-Hebel berechnet
                </div>
            </div>

            <div class="cb-row">
                <div class="cb-row-label">
                    Verwendeter Hebel
                </div>
                <div class="cb-row-value">
                    Pepperstone / Instrument
                </div>
            </div>

            <div class="cb-row">
                <div class="cb-row-label">
                    Freie Margin
                </div>
                <div class="cb-row-value">
                    Wird nach Hebelberechnung angezeigt
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

    st.markdown(
        """
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

if result:

    lots = result["lots"]
    max_loss = result["max_loss"]

    risk_ratio = min(max(risk_percent / 5.0, 0), 1)

    st.markdown(
        f"""
        <div class="cb-risk-panel">

            <div class="cb-risk-title">
                ◇ &nbsp; RISIKOÜBERSICHT
            </div>

            <div class="cb-risk-content">

                <div class="cb-risk-circle">
                    <div class="cb-risk-percent">
                        {number_de(risk_percent, 2)} %
                    </div>
                </div>

                <div class="cb-risk-text">

                    <div class="cb-risk-money">
                        {euro(max_loss)} {account_currency}
                    </div>

                    <div>
                        von {euro(account_size)} {account_currency}
                    </div>

                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RISIKOHINWEIS
# ============================================================

st.markdown(
    """
    <div class="cb-warning">

        <div class="cb-warning-title">
            ⚠ &nbsp; RISIKOHINWEIS
        </div>

        <div class="cb-warning-text">

            CFDs sind komplexe Instrumente und bergen aufgrund
            der Hebelwirkung ein hohes Risiko, schnell Geld zu verlieren.
            Ein erheblicher Anteil der Kleinanlegerkonten verliert Geld
            beim CFD-Handel mit diesem Anbieter.

            Überlegen Sie, ob Sie verstehen, wie CFDs funktionieren und
            ob Sie es sich leisten können, das hohe Risiko einzugehen,
            Ihr Geld zu verlieren.

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    """
    <div class="cb-footer">
        COUNT OR BREAK &nbsp;•&nbsp; RISK FIRST. PROFITS SECOND.
    </div>
    """,
    unsafe_allow_html=True,
)
