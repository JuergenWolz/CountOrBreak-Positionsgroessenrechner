import streamlit as st
import math

# ============================================================
# COUNT OR BREAK – POSITIONSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    page_icon="rechner.png",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ============================================================
# DESIGN
# ============================================================

GOLD = "#C39A3A"
GOLD_LIGHT = "#E2BD63"
GOLD_DARK = "#A77A22"
GOLD_DEEP = "#8F681C"

BLACK = "#050505"
BLACK_2 = "#0A0A0A"
PANEL = "#0D0D0D"
PANEL_2 = "#111111"

WHITE = "#F4F1E9"
TEXT = "#E8E5DE"
MUTED = "#A8A49A"
BORDER = "#343434"

# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap');

    html, body, [class*="css"] {{
        font-family: 'Montserrat', sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(195,154,58,0.075),
                transparent 34%
            ),
            linear-gradient(
                180deg,
                #030303 0%,
                #050505 45%,
                #020202 100%
            );
        color: {TEXT};
    }}

    .block-container {{
        max-width: 1450px;
        padding-top: 1.4rem;
        padding-bottom: 3rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }}

    /* Streamlit Elemente */
    #MainMenu {{
        visibility: hidden;
    }}

    footer {{
        visibility: hidden;
    }}

    header {{
        background: transparent !important;
    }}

    /* ========================================================
       HEADER
       ======================================================== */

    .cb-header {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 42px;
        margin: 5px 0 28px 0;
        min-height: 125px;
    }}

    .cb-logo {{
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .cb-logo img {{
        width: 190px;
        max-height: 120px;
        object-fit: contain;
        filter:
            drop-shadow(0 0 10px rgba(195,154,58,0.12));
    }}

    .cb-calculator-icon {{
        display: flex;
        align-items: center;
        justify-content: center;
        width: 112px;
        height: 112px;
        border: 1px solid {GOLD_DARK};
        border-radius: 20px;
        background:
            radial-gradient(
                circle,
                rgba(195,154,58,0.11),
                rgba(5,5,5,0.95) 70%
            );
        box-shadow:
            0 0 18px rgba(195,154,58,0.18),
            inset 0 0 18px rgba(195,154,58,0.06);
    }}

    .cb-calculator-icon img {{
        width: 82px;
        height: 82px;
        object-fit: contain;
    }}

    /* ========================================================
       TITLE
       ======================================================== */

    .cb-title-box {{
        position: relative;
        border: 1px solid {GOLD_DARK};
        border-radius: 15px;
        min-height: 132px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        background:
            linear-gradient(
                180deg,
                rgba(18,18,18,0.98),
                rgba(5,5,5,0.98)
            );
        box-shadow:
            0 0 16px rgba(195,154,58,0.11),
            inset 0 0 25px rgba(195,154,58,0.025);
        margin-bottom: 30px;
        overflow: hidden;
    }}

    .cb-title-box::before {{
        content: "";
        position: absolute;
        left: 5%;
        right: 5%;
        top: 50%;
        height: 1px;
        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(195,154,58,0.50),
                transparent
            );
        z-index: 0;
    }}

    .cb-title-line {{
        position: absolute;
        width: 125px;
        height: 1px;
        top: 51%;
        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD_DARK}
            );
    }}

    .cb-title-line.left {{
        left: 5%;
    }}

    .cb-title-line.right {{
        right: 5%;
        transform: rotate(180deg);
    }}

    .cb-title {{
        position: relative;
        z-index: 2;
        font-family: 'Cinzel', serif;
        font-size: clamp(30px, 4vw, 54px);
        font-weight: 600;
        letter-spacing: 2px;
        color: {GOLD};
        text-shadow:
            0 0 10px rgba(195,154,58,0.16);
        background: rgba(5,5,5,0.94);
        padding: 0 22px;
        line-height: 1.2;
    }}

    .cb-subtitle {{
        position: relative;
        z-index: 2;
        font-family: 'Cinzel', serif;
        font-size: clamp(15px, 1.8vw, 23px);
        color: {GOLD_DARK};
        letter-spacing: 1.2px;
        background: rgba(5,5,5,0.94);
        padding: 3px 18px;
        margin-top: 3px;
    }}

    /* ========================================================
       PANELS
       ======================================================== */

    .cb-panel {{
        background:
            linear-gradient(
                145deg,
                rgba(18,18,18,0.98),
                rgba(7,7,7,0.98)
            );
        border: 1px solid #303030;
        border-radius: 16px;
        padding: 27px 28px 30px 28px;
        min-height: 100%;
        box-shadow:
            inset 0 0 35px rgba(255,255,255,0.012),
            0 8px 25px rgba(0,0,0,0.22);
    }}

    .cb-panel-title {{
        display: flex;
        align-items: center;
        gap: 15px;
        font-family: 'Cinzel', serif;
        font-size: 23px;
        font-weight: 600;
        color: {GOLD};
        letter-spacing: 0.8px;
        margin-bottom: 25px;
    }}

    .cb-panel-icon {{
        width: 28px;
        height: 28px;
        display: flex;
        align-items: center;
        justify-content: center;
        color: {GOLD};
        font-size: 25px;
    }}

    /* ========================================================
       INPUTS
       ======================================================== */

    label {{
        color: {TEXT} !important;
        font-family: 'Montserrat', sans-serif !important;
        font-size: 15px !important;
    }}

    .stSelectbox,
    .stNumberInput {{
        margin-bottom: 9px;
    }}

    .stSelectbox > div > div,
    .stNumberInput > div > div {{
        background-color: #111111 !important;
        border: 1px solid #554723 !important;
        border-radius: 8px !important;
        color: {WHITE} !important;
    }}

    .stSelectbox input,
    .stNumberInput input {{
        color: {WHITE} !important;
        background: transparent !important;
    }}

    .stSelectbox svg {{
        color: {GOLD} !important;
    }}

    .stNumberInput button {{
        background: transparent !important;
        color: {GOLD} !important;
        border: none !important;
    }}

    .stNumberInput button:hover {{
        color: {GOLD_LIGHT} !important;
        background: rgba(195,154,58,0.05) !important;
    }}

    /* ========================================================
       LONG / SHORT
       ======================================================== */

    .direction-label {{
        color: {TEXT};
        font-size: 15px;
        margin-top: 8px;
        margin-bottom: 8px;
    }}

    div.stButton > button {{
        width: 100%;
        min-height: 47px;
        background:
            linear-gradient(
                180deg,
                #151515,
                #0C0C0C
            );
        border: 1px solid #444444;
        border-radius: 8px;
        color: {TEXT};
        font-family: 'Montserrat', sans-serif;
        font-weight: 600;
        transition: all 0.18s ease;
    }}

    div.stButton > button:hover {{
        border-color: {GOLD};
        color: {GOLD_LIGHT};
        box-shadow:
            0 0 12px rgba(195,154,58,0.15);
        transform: translateY(-1px);
    }}

    /* ========================================================
       RESULT
       ======================================================== */

    .cb-result-heading {{
        display: flex;
        align-items: center;
        gap: 14px;
        color: {GOLD};
        font-family: 'Cinzel', serif;
        font-size: 23px;
        font-weight: 600;
        letter-spacing: 0.8px;
        margin-bottom: 18px;
    }}

    .cb-result-title {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 25px;
        margin: 17px 0 4px 0;
    }}

    .cb-result-title-line {{
        height: 1px;
        flex: 1;
        max-width: 145px;
        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD_DARK}
            );
    }}

    .cb-result-title-line.right {{
        transform: rotate(180deg);
    }}

    .cb-result-label {{
        font-family: 'Cinzel', serif;
        color: {GOLD};
        font-size: 25px;
        font-weight: 500;
        letter-spacing: 0.7px;
        text-align: center;
    }}

    .cb-result-value {{
        text-align: center;
        font-family: 'Montserrat', sans-serif;
        font-size: clamp(50px, 6vw, 82px);
        font-weight: 700;
        line-height: 1.05;
        color: {GOLD_LIGHT};
        text-shadow:
            0 0 9px rgba(195,154,58,0.25),
            0 0 25px rgba(195,154,58,0.12);
        margin-top: 23px;
    }}

    .cb-result-small {{
        text-align: center;
        color: {WHITE};
        font-size: 27px;
        margin-top: 10px;
        margin-bottom: 25px;
    }}

    /* ========================================================
       DATA ROWS
       ======================================================== */

    .cb-data-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 52px;
        border-top: 1px solid #252525;
        font-size: 17px;
    }}

    .cb-data-label {{
        color: {TEXT};
    }}

    .cb-data-value {{
        color: {GOLD};
        font-weight: 600;
        text-align: right;
    }}

    .cb-section-title {{
        display: flex;
        align-items: center;
        gap: 11px;
        color: {GOLD};
        font-family: 'Cinzel', serif;
        font-size: 22px;
        font-weight: 600;
        margin-top: 28px;
        margin-bottom: 8px;
        letter-spacing: 0.5px;
    }}

    /* ========================================================
       RISK OVERVIEW
       ======================================================== */

    .cb-risk-panel {{
        margin-top: 20px;
        background:
            linear-gradient(
                145deg,
                rgba(18,18,18,0.98),
                rgba(7,7,7,0.98)
            );
        border: 1px solid #303030;
        border-radius: 16px;
        padding: 25px 30px;
    }}

    .cb-risk-title {{
        display: flex;
        align-items: center;
        gap: 13px;
        font-family: 'Cinzel', serif;
        color: {GOLD};
        font-size: 22px;
        font-weight: 600;
        margin-bottom: 18px;
    }}

    .cb-risk-content {{
        display: flex;
        align-items: center;
        gap: 38px;
    }}

    .cb-risk-circle {{
        min-width: 125px;
        width: 125px;
        height: 125px;
        border-radius: 50%;
        border: 9px solid #333333;
        border-top-color: {GOLD_DARK};
        border-right-color: {GOLD_DARK};
        display: flex;
        align-items: center;
        justify-content: center;
        flex-direction: column;
        box-shadow:
            0 0 12px rgba(195,154,58,0.08);
    }}

    .cb-risk-percent {{
        color: {GOLD};
        font-size: 24px;
        font-weight: 600;
    }}

    .cb-risk-amount {{
        color: {GOLD};
        font-size: 21px;
        font-weight: 600;
    }}

    .cb-risk-details {{
        flex: 1;
    }}

    .cb-risk-main {{
        color: {GOLD};
        font-size: 23px;
        font-weight: 600;
    }}

    .cb-risk-secondary {{
        color: {TEXT};
        font-size: 17px;
        margin-top: 5px;
    }}

    .cb-risk-bar {{
        display: flex;
        gap: 3px;
        margin-top: 18px;
        flex-wrap: nowrap;
        overflow: hidden;
    }}

    .cb-risk-segment {{
        width: 14px;
        height: 24px;
        background: #272727;
        border: 1px solid #333333;
    }}

    .cb-risk-segment.active {{
        background: {GOLD_DARK};
        border-color: {GOLD};
    }}

    /* ========================================================
       WARNING
       ======================================================== */

    .cb-warning {{
        margin-top: 20px;
        border: 1px solid {GOLD_DEEP};
        border-radius: 15px;
        padding: 21px 28px;
        background:
            linear-gradient(
                145deg,
                rgba(18,18,18,0.98),
                rgba(6,6,6,0.98)
            );
    }}

    .cb-warning-title {{
        display: flex;
        align-items: center;
        gap: 14px;
        color: {GOLD};
        font-family: 'Cinzel', serif;
        font-size: 21px;
        font-weight: 600;
        margin-bottom: 8px;
    }}

    .cb-warning-text {{
        color: {TEXT};
        font-size: 15px;
        line-height: 1.55;
    }}

    /* ========================================================
       INFO
       ======================================================== */

    .cb-info {{
        margin-top: 18px;
        color: {MUTED};
        font-size: 12px;
        line-height: 1.5;
    }}

    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 850px) {{

        .block-container {{
            padding-left: 0.8rem;
            padding-right: 0.8rem;
            padding-top: 0.8rem;
        }}

        .cb-header {{
            gap: 20px;
            min-height: 100px;
        }}

        .cb-logo img {{
            width: 150px;
        }}

        .cb-calculator-icon {{
            width: 85px;
            height: 85px;
            border-radius: 15px;
        }}

        .cb-calculator-icon img {{
            width: 62px;
            height: 62px;
        }}

        .cb-title-box {{
            min-height: 105px;
        }}

        .cb-title {{
            font-size: 27px;
            letter-spacing: 1px;
        }}

        .cb-subtitle {{
            font-size: 13px;
        }}

        .cb-panel {{
            padding: 20px 17px 22px 17px;
            margin-bottom: 16px;
        }}

        .cb-panel-title {{
            font-size: 19px;
        }}

        .cb-result-label {{
            font-size: 20px;
        }}

        .cb-result-small {{
            font-size: 21px;
        }}

        .cb-risk-content {{
            flex-direction: column;
            align-items: flex-start;
            gap: 20px;
        }}

        .cb-risk-circle {{
            align-self: center;
        }}

        .cb-risk-details {{
            width: 100%;
        }}

        .cb-warning {{
            padding: 18px;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="cb-header">

        <div class="cb-logo">
            <img src="logo.png">
        </div>

        <div class="cb-calculator-icon">
            <img src="rechner.png">
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# TITLE
# ============================================================

st.markdown(
    """
    <div class="cb-title-box">

        <div class="cb-title-line left"></div>
        <div class="cb-title-line right"></div>

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
# INPUT / CALCULATOR
# ============================================================

left, right = st.columns([1, 1.35], gap="large")

# ============================================================
# LEFT – TRADE INPUTS
# ============================================================

with left:

    st.markdown(
        """
        <div class="cb-panel">

            <div class="cb-panel-title">
                <div class="cb-panel-icon">⚖</div>
                <div>TRADE-EINGABEN</div>
            </div>

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
            "EUR/GBP",
            "EUR/JPY",
            "GBP/JPY",
            "XAU/USD",
            "XAG/USD",
            "US30",
            "NAS100",
            "SPX500",
            "GER40",
            "UK100",
            "BTC/USD",
            "ETH/USD",
        ],
        index=0,
    )

    st.markdown(
        '<div class="direction-label">Richtung</div>',
        unsafe_allow_html=True,
    )

    direction_left, direction_right = st.columns(2)

    with direction_left:
        long_clicked = st.button("↗ LONG", use_container_width=True)

    with direction_right:
        short_clicked = st.button("↓ SHORT", use_container_width=True)

    if "direction" not in st.session_state:
        st.session_state.direction = "LONG"

    if long_clicked:
        st.session_state.direction = "LONG"

    if short_clicked:
        st.session_state.direction = "SHORT"

    st.markdown(
        f"""
        <div style="
            text-align:center;
            color:{GOLD};
            font-size:12px;
            margin:-1px 0 17px 0;
            letter-spacing:0.6px;
        ">
            AKTUELLE RICHTUNG: {st.session_state.direction}
        </div>
        """,
        unsafe_allow_html=True,
    )

    account_size = st.number_input(
        "Kontogröße",
        min_value=0.0,
        value=10000.0,
        step=100.0,
        format="%.2f",
    )

    account_currency = st.selectbox(
        "Kontowährung",
        ["EUR", "USD", "GBP", "CHF"],
        index=0,
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

    leverage = st.number_input(
        "Hebel",
        min_value=1,
        max_value=500,
        value=30,
        step=1,
    )

# ============================================================
# CALCULATIONS
# ============================================================

risk_amount = account_size * (risk_percent / 100.0)

price_distance = abs(entry_price - stop_price)

if price_distance <= 0:
    price_distance = 0.00001

# Pip-Größe
if "JPY" in instrument:
    pip_size = 0.01
else:
    pip_size = 0.0001

stop_pips = price_distance / pip_size

# Standard FX:
# 1 Standard-Lot = 100.000 Einheiten
contract_size = 100000

# Pip-Wert pro Lot.
# Für EUR/USD als Beispiel:
# 1 Lot ≈ 10 USD/Pip.
#
# Für einen universellen Rechner wird zunächst
# ein vereinfachter Standardwert verwendet.

if instrument in [
    "EUR/USD",
    "GBP/USD",
    "AUD/USD",
    "NZD/USD",
]:
    pip_value_per_lot = 10.0

elif instrument in [
    "USD/JPY",
    "USD/CAD",
    "USD/CHF",
]:
    pip_value_per_lot = 10.0

elif instrument in [
    "EUR/GBP",
]:
    pip_value_per_lot = 10.0

elif instrument in [
    "XAU/USD",
]:
    # Gold: vereinfachtes CFD-Modell
    pip_value_per_lot = 10.0

elif instrument in [
    "US30",
    "NAS100",
    "SPX500",
    "GER40",
    "UK100",
]:
    # Index-CFD: vereinfachtes Modell
    pip_value_per_lot = 1.0

elif instrument == "BTC/USD":
    pip_value_per_lot = 1.0

elif instrument == "ETH/USD":
    pip_value_per_lot = 1.0

else:
    pip_value_per_lot = 10.0

# Positionsgröße in Lots
lots = risk_amount / (stop_pips * pip_value_per_lot)

# Begrenzung gegen unrealistische Werte
lots = max(lots, 0.0)

# Auf 0,01 Lot runden
lots_rounded = math.floor(lots * 100) / 100

if lots_rounded <= 0:
    lots_rounded = 0.01

units = lots_rounded * contract_size

# Tatsächliches Risiko nach Rundung
actual_risk = stop_pips * pip_value_per_lot * lots_rounded

# Positionswert
position_value = lots_rounded * contract_size * entry_price

# Margin
margin_required = position_value / leverage

# Geschätzte freie Margin
free_margin = max(account_size - margin_required, 0)

# ============================================================
# RIGHT – RESULT
# ============================================================

with right:

    st.markdown(
        """
        <div class="cb-panel">

            <div class="cb-result-heading">
                <div>◎</div>
                <div>ERGEBNIS</div>
            </div>

            <div class="cb-result-title">

                <div class="cb-result-title-line"></div>

                <div class="cb-result-label">
                    EMPFOHLENE POSITION
                </div>

                <div class="cb-result-title-line right"></div>

            </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="cb-result-value">
            {lots_rounded:.2f} LOTS
        </div>

        <div class="cb-result-small">
            = {units:,.0f} EINHEITEN
        </div>

        <div class="cb-data-row">
            <div class="cb-data-label">Max. Verlust</div>
            <div class="cb-data-value">
                {actual_risk:,.2f} {account_currency}
            </div>
        </div>

        <div class="cb-data-row">
            <div class="cb-data-label">Stop-Abstand</div>
            <div class="cb-data-value">
                {stop_pips:,.1f} Pips
            </div>
        </div>

        <div class="cb-data-row">
            <div class="cb-data-label">Positionswert</div>
            <div class="cb-data-value">
                {position_value:,.2f} {account_currency}
            </div>
        </div>

        <div class="cb-data-row">
            <div class="cb-data-label">Pip-Wert</div>
            <div class="cb-data-value">
                {pip_value_per_lot * lots_rounded:,.2f} {account_currency}
            </div>
        </div>

        <div class="cb-data-row">
            <div class="cb-data-label">Risikoprozent</div>
            <div class="cb-data-value">
                {risk_percent:.2f} %
            </div>
        </div>

        <div class="cb-section-title">
            <span>⚖</span>
            <span>MARGIN &amp; HEBEL</span>
        </div>

        <div class="cb-data-row">
            <div class="cb-data-label">Erforderliche Margin</div>
            <div class="cb-data-value">
                {margin_required:,.2f} {account_currency}
            </div>
        </div>

        <div class="cb-data-row">
            <div class="cb-data-label">Verwendeter Hebel</div>
            <div class="cb-data-value">
                1 : {leverage}
            </div>
        </div>

        <div class="cb-data-row">
            <div class="cb-data-label">Freie Margin (geschätzt)</div>
            <div class="cb-data-value">
                {free_margin:,.2f} {account_currency}
            </div>
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

# ============================================================
# RISK OVERVIEW
# ============================================================

risk_ratio = min(max(risk_percent / 5.0, 0.0), 1.0)
active_segments = max(1, int(risk_ratio * 24))

segments = ""

for i in range(24):
    if i < active_segments:
        segments += '<div class="cb-risk-segment active"></div>'
    else:
        segments += '<div class="cb-risk-segment"></div>'

st.markdown(
    f"""
    <div class="cb-risk-panel">

        <div class="cb-risk-title">
            <span>♢</span>
            <span>RISIKOÜBERSICHT</span>
        </div>

        <div class="cb-risk-content">

            <div class="cb-risk-circle">

                <div class="cb-risk-percent">
                    {risk_percent:.2f} %
                </div>

            </div>

            <div class="cb-risk-details">

                <div class="cb-risk-main">
                    {actual_risk:,.2f} {account_currency}
                </div>

                <div class="cb-risk-secondary">
                    von {account_size:,.2f} {account_currency}
                </div>

                <div class="cb-risk-bar">
                    {segments}
                </div>

            </div>

        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# WARNING
# ============================================================

st.markdown(
    """
    <div class="cb-warning">

        <div class="cb-warning-title">
            <span style="font-size:30px;">⚠</span>
            <span>RISIKOHINWEIS</span>
        </div>

        <div class="cb-warning-text">
            CFDs sind komplexe Instrumente und bergen aufgrund der
            Hebelwirkung ein hohes Risiko, schnell Geld zu verlieren.
            74–89% der Kleinanlegerkonten verlieren Geld beim CFD-Handel
            mit diesem Anbieter. Überlegen Sie, ob Sie verstehen, wie CFDs
            funktionieren und ob Sie es sich leisten können, das hohe Risiko
            einzugehen, Ihr Geld zu verlieren.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)

# ============================================================
# FOOTER INFO
# ============================================================

st.markdown(
    """
    <div class="cb-info">
        Der Positionsgrößenrechner dient ausschließlich zu
        Informations- und Berechnungszwecken und stellt keine
        Anlageberatung dar. Bei CFD-Instrumenten können
        Kontraktgröße, Pip-Wert, Margin und Währung je nach
        Broker und Instrument abweichen.
    </div>
    """,
    unsafe_allow_html=True,
)
