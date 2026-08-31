import streamlit as st
import math


# ============================================================
# COUNT OR BREAK
# POSITIONSSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    page_icon="rechner.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# KONFIGURATION
# ============================================================

# Hier ggf. die URL deiner CountOrBreak-Startseite eintragen.
START_PAGE_URL = "https://countorbreak.streamlit.app"

LOGO_FILE = "logo.png"
CALCULATOR_ICON = "rechner.png"

# CountOrBreak Goldtöne
GOLD_DARK = "#B88620"
GOLD = "#C99A32"
GOLD_LIGHT = "#E1B84B"
GOLD_BRIGHT = "#F2C75C"
GOLD_GLOW = "rgba(214, 169, 54, 0.28)"

BLACK = "#050505"
BLACK_SOFT = "#0B0B0B"
PANEL = "#101010"
PANEL_2 = "#141414"
BORDER = "rgba(201, 154, 50, 0.38)"
BORDER_SOFT = "rgba(255, 255, 255, 0.14)"
TEXT = "#F0F0F0"
TEXT_MUTED = "#B9B9B9"


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* --------------------------------------------------------
       GRUNDLAYOUT
       -------------------------------------------------------- */

    html, body, [class*="css"] {{
        font-family: "Montserrat", "Arial", sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(184, 134, 32, 0.055),
                transparent 34%
            ),
            linear-gradient(
                180deg,
                #020202 0%,
                #050505 50%,
                #020202 100%
            );

        color: {TEXT};
    }}

    .main {{
        padding-top: 1rem;
    }}

    .block-container {{
        max-width: 1450px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
    }}

    /* Streamlit Standard-Elemente etwas zurücknehmen */

    header[data-testid="stHeader"] {{
        background: transparent;
    }}

    [data-testid="stToolbar"] {{
        display: none;
    }}

    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}


    /* --------------------------------------------------------
       ZURÜCK-BUTTON
       -------------------------------------------------------- */

    .cb-back-wrapper {{
        margin-bottom: 24px;
    }}

    .cb-back-button {{
        display: inline-flex;
        align-items: center;
        gap: 10px;

        padding: 12px 20px;

        background:
            linear-gradient(
                145deg,
                rgba(20, 20, 20, 0.97),
                rgba(7, 7, 7, 0.99)
            );

        border: 1px solid rgba(176, 126, 24, 0.75);
        border-radius: 9px;

        color: {GOLD};

        font-family:
            "Montserrat",
            "Arial",
            sans-serif;

        font-size: 14px;
        font-weight: 600;
        letter-spacing: 1.2px;

        text-decoration: none;

        box-shadow:
            0 0 8px rgba(176, 126, 24, 0.08),
            inset 0 0 12px rgba(176, 126, 24, 0.025);

        transition:
            color 0.25s ease,
            border-color 0.25s ease,
            box-shadow 0.25s ease,
            transform 0.25s ease,
            background 0.25s ease;

        cursor: pointer;
    }}

    .cb-back-arrow {{
        color: {GOLD};
        font-size: 17px;
        line-height: 1;

        transition:
            color 0.25s ease,
            transform 0.25s ease;
    }}

    .cb-back-button:hover {{
        color: {GOLD_BRIGHT};

        border-color: {GOLD_LIGHT};

        background:
            linear-gradient(
                145deg,
                rgba(30, 25, 12, 0.98),
                rgba(12, 10, 5, 0.98)
            );

        box-shadow:
            0 0 10px {GOLD_GLOW},
            0 0 24px rgba(214, 169, 54, 0.12),
            inset 0 0 15px rgba(214, 169, 54, 0.06);

        transform: translateY(-1px);
    }}

    .cb-back-button:hover .cb-back-arrow {{
        color: {GOLD_BRIGHT};
        transform: translateX(-3px);
    }}

    .cb-back-button:active {{
        transform: translateY(0);
    }}


    /* --------------------------------------------------------
       HEADER
       -------------------------------------------------------- */

    .cb-header {{
        display: flex;
        justify-content: center;
        align-items: center;

        gap: 28px;

        margin: 4px 0 26px 0;
    }}

    .cb-logo {{
        display: flex;
        justify-content: center;
        align-items: center;
    }}

    .cb-logo img {{
        width: 170px;
        max-width: 100%;
        height: auto;

        object-fit: contain;

        filter:
            drop-shadow(
                0 0 8px rgba(201, 154, 50, 0.10)
            );
    }}

    .cb-calculator-icon {{
        display: flex;
        justify-content: center;
        align-items: center;

        width: 94px;
        height: 94px;

        border: 1px solid rgba(201, 154, 50, 0.75);
        border-radius: 16px;

        background:
            radial-gradient(
                circle,
                rgba(201, 154, 50, 0.10),
                rgba(0, 0, 0, 0.85)
            );

        box-shadow:
            0 0 12px rgba(201, 154, 50, 0.14),
            inset 0 0 18px rgba(201, 154, 50, 0.045);
    }}

    .cb-calculator-icon img {{
        width: 68px;
        height: 68px;

        object-fit: contain;

        filter:
            drop-shadow(
                0 0 8px rgba(201, 154, 50, 0.24)
            );
    }}


    /* --------------------------------------------------------
       TITELBEREICH
       -------------------------------------------------------- */

    .cb-title-box {{
        position: relative;

        width: 100%;

        padding: 18px 24px 16px 24px;

        margin-bottom: 24px;

        border: 1px solid {GOLD_DARK};
        border-radius: 13px;

        background:
            linear-gradient(
                180deg,
                rgba(23, 23, 23, 0.96),
                rgba(8, 8, 8, 0.98)
            );

        box-shadow:
            0 0 12px rgba(184, 134, 32, 0.08),
            inset 0 0 24px rgba(184, 134, 32, 0.025);

        text-align: center;
    }}

    .cb-title-row {{
        display: flex;
        align-items: center;
        justify-content: center;

        gap: 28px;
    }}

    .cb-title-line {{
        height: 1px;
        flex: 1;

        max-width: 210px;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(201, 154, 50, 0.65)
            );
    }}

    .cb-title-line.right {{
        background:
            linear-gradient(
                90deg,
                rgba(201, 154, 50, 0.65),
                transparent
            );
    }}

    .cb-title {{
        color: {GOLD_DARK};

        font-family:
            "Cinzel",
            "Georgia",
            serif;

        font-size: clamp(28px, 3.2vw, 46px);

        font-weight: 600;

        letter-spacing: 2px;

        text-transform: uppercase;

        text-shadow:
            0 0 10px rgba(184, 134, 32, 0.16);
    }}

    .cb-subtitle {{
        margin-top: 2px;

        color: #D8C88F;

        font-family:
            "Montserrat",
            "Arial",
            sans-serif;

        font-size: 19px;

        letter-spacing: 1px;
    }}


    /* --------------------------------------------------------
       HAUPTPANELS
       -------------------------------------------------------- */

    .cb-panel {{
        background:
            linear-gradient(
                145deg,
                rgba(20, 20, 20, 0.96),
                rgba(7, 7, 7, 0.98)
            );

        border: 1px solid {BORDER_SOFT};

        border-radius: 15px;

        padding: 25px 26px;

        min-height: 100%;

        box-shadow:
            inset 0 0 25px rgba(255, 255, 255, 0.012),
            0 8px 30px rgba(0, 0, 0, 0.25);
    }}

    .cb-panel-title {{
        display: flex;
        align-items: center;

        gap: 12px;

        margin-bottom: 22px;

        color: {GOLD_DARK};

        font-family:
            "Cinzel",
            "Georgia",
            serif;

        font-size: 23px;

        font-weight: 600;

        letter-spacing: 0.8px;

        text-transform: uppercase;
    }}

    .cb-panel-icon {{
        width: 28px;
        height: 28px;

        display: flex;
        align-items: center;
        justify-content: center;

        color: {GOLD_DARK};

        font-size: 21px;
    }}


    /* --------------------------------------------------------
       STREAMLIT INPUTS
       -------------------------------------------------------- */

    label {{
        color: #E8E8E8 !important;

        font-family:
            "Montserrat",
            "Arial",
            sans-serif !important;

        font-size: 15px !important;

        font-weight: 500 !important;
    }}

    .stTextInput input,
    .stNumberInput input,
    .stSelectbox div[data-baseweb="select"] > div {{
        background: #111111 !important;

        color: #EEEEEE !important;

        border: 1px solid rgba(201, 154, 50, 0.42) !important;

        border-radius: 8px !important;
    }}

    .stTextInput input:focus,
    .stNumberInput input:focus {{
        border-color: {GOLD_LIGHT} !important;

        box-shadow:
            0 0 0 1px rgba(201, 154, 50, 0.18),
            0 0 10px rgba(201, 154, 50, 0.08) !important;
    }}

    div[data-baseweb="select"] {{
        border-radius: 8px !important;
    }}

    div[data-baseweb="select"] > div {{
        min-height: 44px;
    }}


    /* --------------------------------------------------------
       LONG / SHORT BUTTONS
       -------------------------------------------------------- */

    .direction-note {{
        margin-top: 5px;
        margin-bottom: 15px;

        color: {GOLD};

        text-align: center;

        font-size: 12px;

        letter-spacing: 0.8px;

        text-transform: uppercase;
    }}

    div.stButton > button {{
        width: 100%;

        min-height: 44px;

        background:
            linear-gradient(
                145deg,
                #161616,
                #0B0B0B
            ) !important;

        color: #EEEEEE !important;

        border: 1px solid rgba(255, 255, 255, 0.20) !important;

        border-radius: 8px !important;

        font-family:
            "Montserrat",
            "Arial",
            sans-serif !important;

        font-weight: 600 !important;

        transition:
            all 0.2s ease !important;
    }}

    div.stButton > button:hover {{
        color: {GOLD_BRIGHT} !important;

        border-color: {GOLD_LIGHT} !important;

        box-shadow:
            0 0 12px rgba(201, 154, 50, 0.16) !important;
    }}


    /* --------------------------------------------------------
       ERGEBNIS
       -------------------------------------------------------- */

    .cb-result-heading {{
        display: flex;
        align-items: center;

        gap: 12px;

        margin-bottom: 20px;

        color: {GOLD_DARK};

        font-family:
            "Cinzel",
            "Georgia",
            serif;

        font-size: 23px;

        font-weight: 600;

        letter-spacing: 0.8px;

        text-transform: uppercase;
    }}

    .cb-result-title {{
        display: flex;
        justify-content: center;
        align-items: center;

        gap: 22px;

        margin-top: 8px;

        margin-bottom: 8px;

        color: {GOLD_DARK};

        font-family:
            "Cinzel",
            "Georgia",
            serif;

        font-size: 23px;

        letter-spacing: 1px;

        text-transform: uppercase;
    }}

    .cb-result-title-line {{
        width: 115px;
        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD_DARK}
            );
    }}

    .cb-result-title-line.right {{
        background:
            linear-gradient(
                90deg,
                {GOLD_DARK},
                transparent
            );
    }}

    .cb-result-value {{
        margin-top: 4px;

        text-align: center;

        color: #FFE18A;

        font-family:
            "Montserrat",
            "Arial",
            sans-serif;

        font-size: clamp(54px, 6vw, 86px);

        font-weight: 700;

        line-height: 1.05;

        letter-spacing: -1px;

        text-shadow:
            0 0 10px rgba(255, 211, 91, 0.35),
            0 0 25px rgba(201, 154, 50, 0.20);
    }}

    .cb-result-units {{
        margin-top: 10px;
        margin-bottom: 24px;

        text-align: center;

        color: #EEEEEE;

        font-family:
            "Montserrat",
            "Arial",
            sans-serif;

        font-size: 24px;

        font-weight: 500;
    }}


    /* --------------------------------------------------------
       RESULTAT-ZEILEN
       -------------------------------------------------------- */

    .cb-stat-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;

        padding: 13px 0;

        border-bottom: 1px solid rgba(255, 255, 255, 0.10);

        font-family:
            "Montserrat",
            "Arial",
            sans-serif;

        font-size: 16px;
    }}

    .cb-stat-label {{
        color: #E5E5E5;
    }}

    .cb-stat-value {{
        color: {GOLD_LIGHT};

        font-weight: 500;

        text-align: right;
    }}

    .cb-section-title {{
        display: flex;
        align-items: center;

        gap: 10px;

        margin-top: 26px;
        margin-bottom: 10px;

        padding-top: 8px;

        color: {GOLD_DARK};

        font-family:
            "Cinzel",
            "Georgia",
            serif;

        font-size: 20px;

        font-weight: 600;

        letter-spacing: 0.7px;

        text-transform: uppercase;
    }}


    /* --------------------------------------------------------
       RISIKOÜBERSICHT
       -------------------------------------------------------- */

    .cb-risk-card {{
        margin-top: 20px;

        padding: 23px 26px;

        border: 1px solid {BORDER_SOFT};

        border-radius: 15px;

        background:
            linear-gradient(
                145deg,
                rgba(18, 18, 18, 0.97),
                rgba(7, 7, 7, 0.99)
            );

        box-shadow:
            inset 0 0 22px rgba(255, 255, 255, 0.012);
    }}

    .cb-risk-title {{
        color: {GOLD_DARK};

        font-family:
            "Cinzel",
            "Georgia",
            serif;

        font-size: 21px;

        font-weight: 600;

        letter-spacing: 0.7px;

        text-transform: uppercase;

        margin-bottom: 18px;
    }}

    .cb-risk-number {{
        color: {GOLD_LIGHT};

        font-size: 28px;

        font-weight: 600;
    }}

    .cb-risk-description {{
        color: #E8E8E8;

        font-size: 15px;
    }}


    /* --------------------------------------------------------
       RISIKOHINWEIS
       -------------------------------------------------------- */

    .cb-warning {{
        margin-top: 20px;

        padding: 22px 26px;

        border: 1px solid rgba(184, 134, 32, 0.75);

        border-radius: 14px;

        background:
            linear-gradient(
                145deg,
                rgba(18, 18, 18, 0.97),
                rgba(7, 7, 7, 0.99)
            );

        box-shadow:
            0 0 14px rgba(184, 134, 32, 0.06),
            inset 0 0 18px rgba(184, 134, 32, 0.018);
    }}

    .cb-warning-title {{
        color: {GOLD_DARK};

        font-family:
            "Cinzel",
            "Georgia",
            serif;

        font-size: 20px;

        font-weight: 600;

        letter-spacing: 0.7px;

        text-transform: uppercase;

        margin-bottom: 8px;
    }}

    .cb-warning-text {{
        color: #E0E0E0;

        font-size: 14px;

        line-height: 1.6;
    }}


    /* --------------------------------------------------------
       MOBILE
       -------------------------------------------------------- */

    @media (max-width: 900px) {{

        .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}

        .cb-header {{
            gap: 18px;
        }}

        .cb-logo img {{
            width: 135px;
        }}

        .cb-calculator-icon {{
            width: 76px;
            height: 76px;
        }}

        .cb-calculator-icon img {{
            width: 54px;
            height: 54px;
        }}

        .cb-title {{
            font-size: 27px;
        }}

        .cb-title-row {{
            gap: 10px;
        }}

        .cb-title-line {{
            max-width: 60px;
        }}

        .cb-result-value {{
            font-size: 55px;
        }}

        .cb-result-units {{
            font-size: 20px;
        }}
    }}

    @media (max-width: 600px) {{

        .cb-header {{
            flex-direction: column;
        }}

        .cb-title-line {{
            display: none;
        }}

        .cb-title {{
            font-size: 24px;
        }}

        .cb-subtitle {{
            font-size: 16px;
        }}

        .cb-panel {{
            padding: 20px 17px;
        }}

        .cb-result-value {{
            font-size: 46px;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def safe_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return default


def format_number(value, decimals=2):
    """
    Deutsche Darstellung:
    1000.00 -> 1.000,00
    """
    return f"{value:,.{decimals}f}".replace(",", "X").replace(".", ",").replace("X", ".")


def calculate_position_size(
    account_size,
    risk_percent,
    entry_price,
    stop_price,
    instrument,
):
    """
    Vereinfachte Positionsgrößenberechnung für CFDs.

    Für Forex:
        Risiko / Stop-Abstand / Pip-Wert

    Für andere CFD-Kategorien wird mit einer
    konfigurierten Kontraktgröße gearbeitet.
    """

    if account_size <= 0:
        return 0.0

    if risk_percent <= 0:
        return 0.0

    if entry_price <= 0 or stop_price <= 0:
        return 0.0

    stop_distance = abs(entry_price - stop_price)

    if stop_distance <= 0:
        return 0.0

    max_loss = account_size * (risk_percent / 100)

    # --------------------------------------------------------
    # FOREX
    # --------------------------------------------------------

    if instrument in [
        "EUR/USD",
        "GBP/USD",
        "USD/JPY",
        "AUD/USD",
        "USD/CAD",
        "USD/CHF",
        "NZD/USD",
    ]:

        # Pip-Größe
        if "JPY" in instrument:
            pip_size = 0.01
        else:
            pip_size = 0.0001

        pips = stop_distance / pip_size

        if pips <= 0:
            return 0.0

        # Näherungswert:
        # 1 Standard-Lot = ca. 10 USD Pip-Wert
        # Für Konten in EUR wird hier bewusst eine
        # vereinfachte Näherung verwendet.
        pip_value_per_lot = 10.0

        lots = max_loss / (pips * pip_value_per_lot)

        return max(0.0, lots)

    # --------------------------------------------------------
    # GOLD
    # --------------------------------------------------------

    if instrument in ["XAU/USD", "GOLD"]:

        # 1 Lot = 100 oz
        contract_size = 100.0

        loss_per_lot = stop_distance * contract_size

        if loss_per_lot <= 0:
            return 0.0

        return max_loss / loss_per_lot

    # --------------------------------------------------------
    # INDIZES
    # --------------------------------------------------------

    if instrument in [
        "US30",
        "NAS100",
        "SPX500",
        "GER40",
        "UK100",
    ]:

        # Näherungsweise 1 Einheit pro Punkt je Lot.
        point_value = 1.0

        loss_per_lot = stop_distance * point_value

        if loss_per_lot <= 0:
            return 0.0

        return max_loss / loss_per_lot

    # --------------------------------------------------------
    # DEFAULT CFD
    # --------------------------------------------------------

    contract_size = 1.0

    loss_per_lot = stop_distance * contract_size

    if loss_per_lot <= 0:
        return 0.0

    return max_loss / loss_per_lot


# ============================================================
# SESSION STATE
# ============================================================

if "direction" not in st.session_state:
    st.session_state.direction = "LONG"


# ============================================================
# ZURÜCK ZUR STARTSEITE
# ============================================================

st.markdown(
    f"""
    <div class="cb-back-wrapper">
        <a
            href="{START_PAGE_URL}"
            target="_self"
            class="cb-back-button"
        >
            <span class="cb-back-arrow">←</span>
            <span>ZURÜCK ZUR STARTSEITE</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

st.markdown(
    f"""
    <div class="cb-header">

        <div class="cb-logo">
            <img
                src="{LOGO_FILE}"
                alt="CountOrBreak Logo"
            />
        </div>

        <div class="cb-calculator-icon">
            <img
                src="{CALCULATOR_ICON}"
                alt="Positionsgrößenrechner"
            />
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

        <div class="cb-title-row">

            <div class="cb-title-line"></div>

            <div class="cb-title">
                POSITIONSGRÖSSENRECHNER
            </div>

            <div class="cb-title-line right"></div>

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
# ============================================================

left_col, right_col = st.columns(
    [1, 1.35],
    gap="large",
)


# ============================================================
# LINKE SEITE – TRADE-EINGABEN
# ============================================================

with left_col:

    st.markdown(
        """
        <div class="cb-panel">

            <div class="cb-panel-title">

                <div class="cb-panel-icon">
                    ⚖
                </div>

                <div>
                    TRADE-EINGABEN
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # INSTRUMENT
    # --------------------------------------------------------

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
            "XAU/USD",
            "US30",
            "NAS100",
            "SPX500",
            "GER40",
            "UK100",
        ],
        index=0,
    )

    # --------------------------------------------------------
    # RICHTUNG
    # --------------------------------------------------------

    st.markdown(
        "<div style='height:6px'></div>",
        unsafe_allow_html=True,
    )

    direction_col1, direction_col2 = st.columns(2)

    with direction_col1:
        if st.button(
            "↗ LONG",
            use_container_width=True,
            key="long_button",
        ):
            st.session_state.direction = "LONG"

    with direction_col2:
        if st.button(
            "↓ SHORT",
            use_container_width=True,
            key="short_button",
        ):
            st.session_state.direction = "SHORT"

    st.markdown(
        f"""
        <div class="direction-note">
            AKTUELLE RICHTUNG: {st.session_state.direction}
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # KONTOGRÖSSE
    # --------------------------------------------------------

    account_size = st.number_input(
        "Kontogröße",
        min_value=0.0,
        value=10000.0,
        step=100.0,
        format="%.2f",
    )

    # --------------------------------------------------------
    # RISIKO
    # --------------------------------------------------------

    risk_percent = st.number_input(
        "Risiko pro Trade",
        min_value=0.0,
        max_value=100.0,
        value=1.0,
        step=0.10,
        format="%.2f",
    )

    # --------------------------------------------------------
    # EINSTIEG
    # --------------------------------------------------------

    if instrument == "USD/JPY":

        default_entry = 147.500
        default_stop = 147.000
        step_price = 0.001

    elif instrument in [
        "US30",
        "NAS100",
        "SPX500",
        "GER40",
        "UK100",
    ]:

        default_entry = 23000.0
        default_stop = 22900.0
        step_price = 1.0

    elif instrument == "XAU/USD":

        default_entry = 3400.0
        default_stop = 3390.0
        step_price = 0.1

    else:

        default_entry = 1.17000
        default_stop = 1.16500
        step_price = 0.00001

    entry_price = st.number_input(
        "Einstiegskurs",
        min_value=0.0,
        value=float(default_entry),
        step=float(step_price),
        format="%.5f"
        if instrument not in [
            "US30",
            "NAS100",
            "SPX500",
            "GER40",
            "UK100",
        ]
        else "%.2f",
    )

    # --------------------------------------------------------
    # STOP LOSS
    # --------------------------------------------------------

    stop_price = st.number_input(
        "Stop-Loss Kurs",
        min_value=0.0,
        value=float(default_stop),
        step=float(step_price),
        format="%.5f"
        if instrument not in [
            "US30",
            "NAS100",
            "SPX500",
            "GER40",
            "UK100",
        ]
        else "%.2f",
    )

    # --------------------------------------------------------
    # KONTO-WÄHRUNG
    # --------------------------------------------------------

    account_currency = st.selectbox(
        "Kontowährung",
        ["EUR", "USD", "GBP"],
        index=0,
    )


# ============================================================
# BERECHNUNG
# ============================================================

max_loss = account_size * (risk_percent / 100.0)

stop_distance = abs(entry_price - stop_price)

lots = calculate_position_size(
    account_size=account_size,
    risk_percent=risk_percent,
    entry_price=entry_price,
    stop_price=stop_price,
    instrument=instrument,
)

# ------------------------------------------------------------
# Einheiten
# ------------------------------------------------------------

if instrument in [
    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "AUD/USD",
    "USD/CAD",
    "USD/CHF",
    "NZD/USD",
]:

    units = lots * 100000

elif instrument == "XAU/USD":

    units = lots * 100

else:

    units = lots


# ============================================================
# RECHTE SEITE – ERGEBNIS
# ============================================================

with right_col:

    st.markdown(
        """
        <div class="cb-panel">

            <div class="cb-result-heading">

                <div class="cb-panel-icon">
                    ◎
                </div>

                <div>
                    ERGEBNIS
                </div>

            </div>

            <div class="cb-result-title">

                <div class="cb-result-title-line"></div>

                <div>
                    EMPFOHLENE POSITION
                </div>

                <div class="cb-result-title-line right"></div>

            </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # HAUPTERGEBNIS
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="cb-result-value">
            {format_number(lots, 2)} LOTS
        </div>

        <div class="cb-result-units">
            = {format_number(units, 0)} EINHEITEN
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # STATISTIKEN
    # --------------------------------------------------------

    if instrument in [
        "EUR/USD",
        "GBP/USD",
        "AUD/USD",
        "USD/CAD",
        "USD/CHF",
        "NZD/USD",
    ]:

        pip_size = 0.0001
        stop_pips = stop_distance / pip_size

        pip_value = lots * 10

    elif instrument == "USD/JPY":

        pip_size = 0.01
        stop_pips = stop_distance / pip_size

        pip_value = lots * 10

    else:

        stop_pips = stop_distance
        pip_value = lots

    position_value = lots * 100000 if instrument in [
        "EUR/USD",
        "GBP/USD",
        "USD/JPY",
        "AUD/USD",
        "USD/CAD",
        "USD/CHF",
        "NZD/USD",
    ] else units

    st.markdown(
        f"""
        <div class="cb-stat-row">
            <div class="cb-stat-label">
                Max. Verlust
            </div>

            <div class="cb-stat-value">
                {format_number(max_loss, 2)}
                &nbsp;{account_currency}
            </div>
        </div>

        <div class="cb-stat-row">
            <div class="cb-stat-label">
                Stop-Abstand
            </div>

            <div class="cb-stat-value">
                {format_number(stop_pips, 1)}
                &nbsp;{"Pips" if instrument in [
                    "EUR/USD",
                    "GBP/USD",
                    "USD/JPY",
                    "AUD/USD",
                    "USD/CAD",
                    "USD/CHF",
                    "NZD/USD",
                ] else "Punkte"}
            </div>
        </div>

        <div class="cb-stat-row">
            <div class="cb-stat-label">
                Positionswert
            </div>

            <div class="cb-stat-value">
                {format_number(position_value, 2)}
                &nbsp;{account_currency}
            </div>
        </div>

        <div class="cb-stat-row">
            <div class="cb-stat-label">
                Pip-Wert
            </div>

            <div class="cb-stat-value">
                {format_number(pip_value, 2)}
                &nbsp;{account_currency}
            </div>
        </div>

        <div class="cb-stat-row">
            <div class="cb-stat-label">
                Risikoprozent
            </div>

            <div class="cb-stat-value">
                {format_number(risk_percent, 2)}
                &nbsp;%
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # MARGIN & HEBEL
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="cb-section-title">
            <span>⚖</span>
            <span>MARGIN &amp; HEBEL</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # Für die Darstellung wird ein konservativer Standardhebel
    # verwendet. Pepperstone kann je nach Instrument,
    # Kontotyp und regulatorischem Standort andere
    # Margin-Anforderungen haben.

    leverage = 30

    margin = (
        position_value / leverage
        if leverage > 0
        else 0
    )

    free_margin = max(
        0,
        account_size - margin,
    )

    st.markdown(
        f"""
        <div class="cb-stat-row">
            <div class="cb-stat-label">
                Erforderliche Margin
            </div>

            <div class="cb-stat-value">
                {format_number(margin, 2)}
                &nbsp;{account_currency}
            </div>
        </div>

        <div class="cb-stat-row">
            <div class="cb-stat-label">
                Verwendeter Hebel
            </div>

            <div class="cb-stat-value">
                1 : {leverage}
            </div>
        </div>

        <div class="cb-stat-row">
            <div class="cb-stat-label">
                Freie Margin (geschätzt)
            </div>

            <div class="cb-stat-value">
                {format_number(free_margin, 2)}
                &nbsp;{account_currency}
            </div>
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

risk_ratio = min(max(risk_percent / 5.0, 0), 1)

risk_blocks = 20
filled_blocks = int(round(risk_ratio * risk_blocks))

blocks_html = ""

for i in range(risk_blocks):

    if i < filled_blocks:
        blocks_html += (
            '<span style="'
            f'display:inline-block;'
            f'width:14px;'
            f'height:22px;'
            f'margin-right:3px;'
            f'background:{GOLD};'
            f'border:1px solid {GOLD_LIGHT};'
            f'box-shadow:0 0 5px rgba(201,154,50,0.20);'
            '"></span>'
        )

    else:
        blocks_html += (
            '<span style="'
            'display:inline-block;'
            'width:14px;'
            'height:22px;'
            'margin-right:3px;'
            'background:#202020;'
            'border:1px solid #333333;'
            '"></span>'
        )


st.markdown(
    f"""
    <div class="cb-risk-card">

        <div class="cb-risk-title">
            🛡 &nbsp;RISIKOÜBERSICHT
        </div>

        <div style="
            display:flex;
            align-items:center;
            gap:28px;
            flex-wrap:wrap;
        ">

            <div style="
                width:120px;
                height:120px;
                border-radius:50%;
                border:10px solid #303030;
                display:flex;
                flex-direction:column;
                justify-content:center;
                align-items:center;
                box-sizing:border-box;
            ">

                <div class="cb-risk-number">
                    {format_number(risk_percent, 2)} %
                </div>

            </div>

            <div style="flex:1; min-width:250px;">

                <div class="cb-risk-number">
                    {format_number(max_loss, 2)} {account_currency}
                </div>

                <div class="cb-risk-description">
                    von {format_number(account_size, 2)} {account_currency}
                </div>

                <div style="
                    margin-top:14px;
                    white-space:nowrap;
                    overflow:hidden;
                ">
                    {blocks_html}
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
            ⚠ &nbsp;RISIKOHINWEIS
        </div>

        <div class="cb-warning-text">
            CFDs sind komplexe Instrumente und bergen aufgrund
            der Hebelwirkung ein hohes Risiko, schnell Geld zu
            verlieren. Der Positionsgrößenrechner dient
            ausschließlich der Orientierung und ersetzt keine
            individuelle Anlage-, Finanz- oder Steuerberatung.
            Prüfe vor jedem Trade die tatsächlichen
            Kontraktgrößen, Pip-Werte, Margin-Anforderungen und
            Hebelbedingungen deines Brokers.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    f"""
    <div style="
        text-align:center;
        margin-top:28px;
        color:#666666;
        font-size:11px;
        letter-spacing:0.8px;
    ">
        COUNT OR BREAK &nbsp;•&nbsp; RISK FIRST. PROFITS SECOND.
    </div>
    """,
    unsafe_allow_html=True,
)
