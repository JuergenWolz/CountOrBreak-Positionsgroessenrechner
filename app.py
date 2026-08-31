import streamlit as st
import math

# ============================================================
# COUNT OR BREAK — POSITIONSGRÖSSENRECHNER
# Pepperstone / CFD
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

# HIER DIE URL DEINER COUNT OR BREAK STARTSEITE EINTRAGEN
STARTSEITE_URL = "https://DEINE-STARTSEITE.streamlit.app"

LOGO_PATH = "logo.png"
RECHNER_PATH = "rechner.png"

# CountOrBreak Gold
GOLD = "#C99A2E"
GOLD_LIGHT = "#E6C15A"
GOLD_BRIGHT = "#F4D77A"
GOLD_DARK = "#8C6416"

BLACK = "#050505"
PANEL = "#0D0D0D"
PANEL_2 = "#111111"
BORDER = "#282828"
TEXT = "#F1F1F1"
MUTED = "#A7A7A7"

# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Montserrat:wght@400;500;600;700&display=swap');

html, body, [class*="css"] {{
    font-family: 'Montserrat', sans-serif;
}}

.stApp {{
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(201,154,46,0.08) 0%,
            rgba(0,0,0,0) 35%
        ),
        #000000;
    color: {TEXT};
}}

.block-container {{
    max-width: 1500px;
    padding-top: 2rem;
    padding-bottom: 3rem;
    padding-left: 2rem;
    padding-right: 2rem;
}}

#MainMenu {{
    visibility: hidden;
}}

header {{
    visibility: hidden;
}}

footer {{
    visibility: hidden;
}}

[data-testid="stSidebar"] {{
    display: none;
}}

/* =========================================================
   TOP NAVIGATION
   ========================================================= */

.cb-topbar {{
    display: flex;
    align-items: center;
    justify-content: flex-start;
    margin-bottom: 22px;
}}

.cb-back {{
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 10px 17px;
    border: 1px solid rgba(201,154,46,0.48);
    border-radius: 8px;
    color: {GOLD_LIGHT};
    background: rgba(8,8,8,0.88);
    text-decoration: none !important;
    font-family: 'Montserrat', sans-serif;
    font-size: 13px;
    font-weight: 600;
    letter-spacing: 0.7px;
    transition: all 0.25s ease;
    box-shadow:
        inset 0 0 15px rgba(201,154,46,0.025),
        0 0 0 rgba(201,154,46,0);
}}

.cb-back:hover {{
    color: {GOLD_BRIGHT};
    border-color: {GOLD};
    box-shadow:
        0 0 18px rgba(201,154,46,0.18),
        inset 0 0 18px rgba(201,154,46,0.05);
    transform: translateX(-2px);
}}

/* =========================================================
   BRAND AREA
   ========================================================= */

.cb-brand {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 30px;
    margin-bottom: 24px;
}}

.cb-logo {{
    display: flex;
    align-items: center;
    justify-content: center;
}}

.cb-logo img {{
    width: 190px;
    max-width: 100%;
    height: auto;
    object-fit: contain;
}}

.cb-calculator {{
    width: 86px;
    height: 86px;
    display: flex;
    align-items: center;
    justify-content: center;
    border: 1px solid rgba(201,154,46,0.75);
    border-radius: 16px;
    background:
        radial-gradient(
            circle,
            rgba(201,154,46,0.14),
            rgba(0,0,0,0.72)
        );
    box-shadow:
        0 0 20px rgba(201,154,46,0.18),
        inset 0 0 18px rgba(201,154,46,0.05);
}}

.cb-calculator img {{
    width: 64px;
    height: 64px;
    object-fit: contain;
}}

/* =========================================================
   MAIN TITLE
   ========================================================= */

.cb-title-box {{
    position: relative;
    min-height: 155px;
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 30px 25px;
    margin-bottom: 25px;

    background:
        linear-gradient(
            180deg,
            rgba(25,25,25,0.95),
            rgba(5,5,5,0.98)
        );

    border: 1px solid {GOLD_DARK};
    border-radius: 14px;

    box-shadow:
        0 0 16px rgba(201,154,46,0.11),
        inset 0 0 35px rgba(201,154,46,0.025);
}}

.cb-title-row {{
    width: 100%;
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 28px;
}}

.cb-title-line {{
    flex: 1;
    height: 1px;
    max-width: 180px;
    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(201,154,46,0.8)
        );
}}

.cb-title-line.right {{
    background:
        linear-gradient(
            90deg,
            rgba(201,154,46,0.8),
            transparent
        );
}}

.cb-title {{
    color: {GOLD_LIGHT};
    font-family: 'Cinzel', serif;
    font-size: clamp(27px, 4vw, 48px);
    font-weight: 600;
    letter-spacing: 2.5px;
    text-align: center;
    text-shadow:
        0 0 14px rgba(201,154,46,0.22);
}}

.cb-subtitle {{
    margin-top: 5px;
    color: #D8C88F;
    font-family: 'Cinzel', serif;
    font-size: clamp(15px, 2vw, 23px);
    letter-spacing: 1px;
}}

/* =========================================================
   PANELS
   ========================================================= */

.cb-panel {{
    height: 100%;
    min-height: 700px;
    padding: 27px 25px;

    background:
        radial-gradient(
            circle at top right,
            rgba(201,154,46,0.025),
            transparent 40%
        ),
        linear-gradient(
            180deg,
            rgba(18,18,18,0.98),
            rgba(5,5,5,0.99)
        );

    border: 1px solid #303030;
    border-radius: 15px;

    box-shadow:
        inset 0 0 40px rgba(255,255,255,0.008),
        0 0 25px rgba(0,0,0,0.4);
}}

.cb-panel-header {{
    display: flex;
    align-items: center;
    gap: 13px;
    margin-bottom: 28px;
}}

.cb-panel-icon {{
    width: 33px;
    height: 33px;
    display: flex;
    align-items: center;
    justify-content: center;
    color: {GOLD};
    font-size: 22px;
}}

.cb-panel-title {{
    color: {GOLD};
    font-family: 'Cinzel', serif;
    font-size: 23px;
    font-weight: 600;
    letter-spacing: 1.2px;
}}

.cb-section-title {{
    color: {GOLD};
    font-family: 'Cinzel', serif;
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 0.9px;
    margin-top: 28px;
    margin-bottom: 15px;
}}

.cb-label {{
    color: #E5E5E5;
    font-size: 14px;
    font-weight: 500;
    margin-top: 14px;
    margin-bottom: 7px;
}}

/* =========================================================
   STREAMLIT INPUTS
   ========================================================= */

div[data-baseweb="select"] > div {{
    background: #111111 !important;
    border: 1px solid #5A4720 !important;
    border-radius: 8px !important;
    color: white !important;
    min-height: 48px !important;
}}

div[data-baseweb="select"] > div:hover {{
    border-color: {GOLD} !important;
    box-shadow: 0 0 12px rgba(201,154,46,0.10);
}}

div[data-baseweb="input"] {{
    background: #111111 !important;
    border-radius: 8px !important;
}}

div[data-baseweb="input"] input {{
    background: #111111 !important;
    color: #F3F3F3 !important;
}}

.stTextInput input,
.stNumberInput input {{
    background: #111111 !important;
    color: #F3F3F3 !important;
    border: 1px solid #5A4720 !important;
    border-radius: 8px !important;
    min-height: 48px !important;
}}

.stTextInput input:focus,
.stNumberInput input:focus {{
    border-color: {GOLD} !important;
    box-shadow: 0 0 12px rgba(201,154,46,0.12) !important;
}}

div[data-testid="stNumberInput"] button {{
    background: #111111 !important;
    color: {GOLD} !important;
    border-left: 1px solid #4A3A1A !important;
}}

.stSelectbox label,
.stNumberInput label,
.stTextInput label {{
    color: #E5E5E5 !important;
}}

/* =========================================================
   LONG / SHORT BUTTONS
   ========================================================= */

div.stButton > button {{
    width: 100%;
    min-height: 47px;
    border-radius: 8px;
    border: 1px solid #494949;
    background: #111111;
    color: #EEEEEE;
    font-family: 'Montserrat', sans-serif;
    font-weight: 600;
    letter-spacing: 0.4px;
    transition: all 0.2s ease;
}}

div.stButton > button:hover {{
    border-color: {GOLD};
    color: {GOLD_LIGHT};
    box-shadow: 0 0 14px rgba(201,154,46,0.13);
}}

.cb-direction-active {{
    color: {GOLD_LIGHT};
    font-size: 12px;
    font-weight: 600;
    text-align: center;
    margin-top: 8px;
    letter-spacing: 0.5px;
}}

/* =========================================================
   RESULT PANEL
   ========================================================= */

.cb-result-panel {{
    min-height: 700px;
    padding: 27px 25px;

    background:
        radial-gradient(
            circle at 50% 30%,
            rgba(201,154,46,0.055),
            transparent 38%
        ),
        linear-gradient(
            180deg,
            rgba(18,18,18,0.98),
            rgba(5,5,5,0.99)
        );

    border: 1px solid #303030;
    border-radius: 15px;

    box-shadow:
        inset 0 0 50px rgba(201,154,46,0.018),
        0 0 25px rgba(0,0,0,0.4);
}}

.cb-result-header {{
    display: flex;
    align-items: center;
    gap: 13px;
    color: {GOLD};
    font-family: 'Cinzel', serif;
    font-size: 23px;
    font-weight: 600;
    letter-spacing: 1.2px;
}}

.cb-result-title {{
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 22px;
    margin-top: 38px;
    color: {GOLD_LIGHT};
    font-family: 'Cinzel', serif;
    font-size: 23px;
    font-weight: 600;
    letter-spacing: 1.1px;
    text-align: center;
}}

.cb-result-line {{
    width: 100px;
    height: 1px;
    background:
        linear-gradient(
            90deg,
            transparent,
            {GOLD}
        );
}}

.cb-result-line.right {{
    background:
        linear-gradient(
            90deg,
            {GOLD},
            transparent
        );
}}

.cb-lots {{
    margin-top: 25px;
    text-align: center;
    color: {GOLD_BRIGHT};
    font-family: 'Montserrat', sans-serif;
    font-size: clamp(48px, 6vw, 78px);
    font-weight: 700;
    letter-spacing: -1px;
    text-shadow:
        0 0 18px rgba(244,215,122,0.32),
        0 0 35px rgba(201,154,46,0.15);
}}

.cb-units {{
    text-align: center;
    color: #EEEEEE;
    font-size: 25px;
    margin-top: 4px;
}}

.cb-divider {{
    height: 1px;
    margin: 25px 0 14px;
    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(201,154,46,0.42),
            transparent
        );
}}

.cb-stat {{
    display: flex;
    align-items: center;
    justify-content: space-between;
    padding: 12px 0;
    border-bottom: 1px solid #242424;
    font-size: 16px;
}}

.cb-stat-name {{
    color: #D9D9D9;
}}

.cb-stat-value {{
    color: {GOLD_LIGHT};
    font-weight: 600;
    text-align: right;
}}

.cb-margin-title {{
    margin-top: 30px;
    color: {GOLD};
    font-family: 'Cinzel', serif;
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 0.8px;
}}

/* =========================================================
   RISK OVERVIEW
   ========================================================= */

.cb-risk {{
    margin-top: 22px;
    padding: 24px 25px;

    background:
        linear-gradient(
            180deg,
            rgba(16,16,16,0.98),
            rgba(7,7,7,0.99)
        );

    border: 1px solid #303030;
    border-radius: 15px;
}}

.cb-risk-title {{
    color: {GOLD};
    font-family: 'Cinzel', serif;
    font-size: 20px;
    font-weight: 600;
    letter-spacing: 0.8px;
    margin-bottom: 18px;
}}

.cb-risk-content {{
    display: flex;
    align-items: center;
    gap: 35px;
}}

.cb-risk-circle {{
    width: 115px;
    height: 115px;
    flex: 0 0 115px;

    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;

    border: 8px solid #292929;
    box-shadow:
        inset 0 0 15px rgba(201,154,46,0.08),
        0 0 15px rgba(201,154,46,0.08);
}}

.cb-risk-circle-inner {{
    text-align: center;
}}

.cb-risk-percent {{
    color: {GOLD_LIGHT};
    font-size: 23px;
    font-weight: 600;
}}

.cb-risk-amount {{
    color: {GOLD};
    font-size: 17px;
    font-weight: 600;
}}

/* =========================================================
   WARNING
   ========================================================= */

.cb-warning {{
    margin-top: 22px;
    padding: 22px 25px;

    background:
        linear-gradient(
            180deg,
            rgba(15,15,15,0.98),
            rgba(5,5,5,0.99)
        );

    border: 1px solid #624A10;
    border-radius: 14px;

    box-shadow:
        inset 0 0 30px rgba(201,154,46,0.015);
}}

.cb-warning-title {{
    color: {GOLD};
    font-family: 'Cinzel', serif;
    font-size: 19px;
    font-weight: 600;
    letter-spacing: 0.8px;
    margin-bottom: 9px;
}}

.cb-warning-text {{
    color: #CFCFCF;
    font-size: 13px;
    line-height: 1.65;
}}

/* =========================================================
   INFO
   ========================================================= */

.cb-info {{
    color: #8F8F8F;
    font-size: 11px;
    line-height: 1.55;
    margin-top: 16px;
}}

/* =========================================================
   MOBILE
   ========================================================= */

@media (max-width: 900px) {{

    .block-container {{
        padding-left: 1rem;
        padding-right: 1rem;
        padding-top: 1rem;
    }}

    .cb-brand {{
        gap: 16px;
    }}

    .cb-logo img {{
        width: 155px;
    }}

    .cb-calculator {{
        width: 70px;
        height: 70px;
    }}

    .cb-calculator img {{
        width: 51px;
        height: 51px;
    }}

    .cb-title-box {{
        min-height: 125px;
        padding: 20px 12px;
    }}

    .cb-title-row {{
        gap: 10px;
    }}

    .cb-title-line {{
        max-width: 60px;
    }}

    .cb-title {{
        letter-spacing: 1px;
    }}

    .cb-panel,
    .cb-result-panel {{
        min-height: auto;
        padding: 21px 17px;
    }}

    .cb-result-panel {{
        margin-top: 20px;
    }}

    .cb-risk-content {{
        gap: 18px;
    }}

    .cb-risk-circle {{
        width: 90px;
        height: 90px;
        flex-basis: 90px;
        border-width: 6px;
    }}

    .cb-risk-percent {{
        font-size: 18px;
    }}

    .cb-risk-amount {{
        font-size: 14px;
    }}

    .cb-stat {{
        font-size: 14px;
    }}

    .cb-lots {{
        font-size: 48px;
    }}

    .cb-units {{
        font-size: 19px;
    }}
}}

@media (max-width: 520px) {{

    .cb-brand {{
        justify-content: space-between;
    }}

    .cb-logo img {{
        width: 140px;
    }}

    .cb-calculator {{
        width: 62px;
        height: 62px;
    }}

    .cb-calculator img {{
        width: 45px;
        height: 45px;
    }}

    .cb-title-line {{
        display: none;
    }}

    .cb-result-title {{
        font-size: 18px;
    }}

    .cb-result-line {{
        width: 45px;
    }}

    .cb-lots {{
        font-size: 42px;
    }}

    .cb-risk-content {{
        align-items: flex-start;
    }}
}}

</style>
""",
    unsafe_allow_html=True,
)

# ============================================================
# SESSION STATE
# ============================================================

if "direction" not in st.session_state:
    st.session_state.direction = "LONG"

# ============================================================
# CFD-INSTRUMENTE
# ============================================================

INSTRUMENTS = {

    # Forex
    "EUR/USD": {
        "category": "Forex",
        "contract_size": 100000,
        "pip_size": 0.0001,
        "pip_value_per_lot": 10.0,
        "default_price": 1.17000,
        "default_stop": 1.16500,
        "margin_rate": 0.0333,
        "currency": "EUR",
    },

    "GBP/USD": {
        "category": "Forex",
        "contract_size": 100000,
        "pip_size": 0.0001,
        "pip_value_per_lot": 10.0,
        "default_price": 1.35000,
        "default_stop": 1.34500,
        "margin_rate": 0.0333,
        "currency": "GBP",
    },

    "USD/JPY": {
        "category": "Forex",
        "contract_size": 100000,
        "pip_size": 0.01,
        "pip_value_per_lot": 6.80,
        "default_price": 147.000,
        "default_stop": 146.500,
        "margin_rate": 0.0333,
        "currency": "USD",
    },

    "AUD/USD": {
        "category": "Forex",
        "contract_size": 100000,
        "pip_size": 0.0001,
        "pip_value_per_lot": 10.0,
        "default_price": 0.65500,
        "default_stop": 0.65000,
        "margin_rate": 0.0333,
        "currency": "AUD",
    },

    # Indizes
    "GER40": {
        "category": "Index",
        "contract_size": 1,
        "pip_size": 1.0,
        "pip_value_per_lot": 1.0,
        "default_price": 24000.0,
        "default_stop": 23950.0,
        "margin_rate": 0.05,
        "currency": "EUR",
    },

    "US500": {
        "category": "Index",
        "contract_size": 1,
        "pip_size": 1.0,
        "pip_value_per_lot": 1.0,
        "default_price": 6400.0,
        "default_stop": 6350.0,
        "margin_rate": 0.05,
        "currency": "USD",
    },

    "NAS100": {
        "category": "Index",
        "contract_size": 1,
        "pip_size": 1.0,
        "pip_value_per_lot": 1.0,
        "default_price": 23500.0,
        "default_stop": 23450.0,
        "margin_rate": 0.05,
        "currency": "USD",
    },

    # Metalle
    "XAU/USD": {
        "category": "Metall",
        "contract_size": 100,
        "pip_size": 0.01,
        "pip_value_per_lot": 1.0,
        "default_price": 3400.00,
        "default_stop": 3390.00,
        "margin_rate": 0.05,
        "currency": "USD",
    },

    # Öl
    "USOIL": {
        "category": "Energie",
        "contract_size": 100,
        "pip_size": 0.01,
        "pip_value_per_lot": 1.0,
        "default_price": 65.00,
        "default_stop": 64.00,
        "margin_rate": 0.10,
        "currency": "USD",
    },

    # Krypto
    "BTC/USD": {
        "category": "Krypto",
        "contract_size": 1,
        "pip_size": 1.0,
        "pip_value_per_lot": 1.0,
        "default_price": 110000.0,
        "default_stop": 109000.0,
        "margin_rate": 0.50,
        "currency": "USD",
    },
}

# ============================================================
# FORMATIERUNG
# ============================================================

def format_number(value, decimals=2):
    if value is None:
        return "-"

    formatted = f"{value:,.{decimals}f}"
    return formatted.replace(",", "X").replace(".", ",").replace("X", ".")


def format_price(value, category):
    if category == "Forex":
        if value >= 10:
            return format_number(value, 3)
        return format_number(value, 5)

    if category == "Krypto":
        return format_number(value, 2)

    return format_number(value, 2)


def safe_float(value, default=0.0):
    try:
        return float(value)
    except Exception:
        return default


# ============================================================
# BERECHNUNG
# ============================================================

def calculate_position(
    instrument,
    account_size,
    risk_percent,
    entry_price,
    stop_price,
    leverage,
):
    data = INSTRUMENTS[instrument]

    category = data["category"]
    contract_size = data["contract_size"]
    pip_size = data["pip_size"]
    pip_value = data["pip_value_per_lot"]

    # --------------------------------------------------------
    # Maximaler Geldbetrag, den der Trade riskieren darf
    # --------------------------------------------------------

    max_loss = account_size * (risk_percent / 100.0)

    # --------------------------------------------------------
    # Stop-Distanz
    # --------------------------------------------------------

    price_distance = abs(entry_price - stop_price)

    if pip_size > 0:
        stop_distance = price_distance / pip_size
    else:
        stop_distance = 0

    # --------------------------------------------------------
    # Verlust pro Lot
    # --------------------------------------------------------

    loss_per_lot = stop_distance * pip_value

    if loss_per_lot <= 0:
        lots = 0
    else:
        lots = max_loss / loss_per_lot

    # Sinnvolle CFD-Darstellung
    lots = max(0.0, lots)

    # --------------------------------------------------------
    # Einheiten
    # --------------------------------------------------------

    units = lots * contract_size

    # --------------------------------------------------------
    # Positionswert
    # --------------------------------------------------------

    position_value = units * entry_price

    # --------------------------------------------------------
    # Margin
    # --------------------------------------------------------

    if leverage <= 0:
        leverage = 1

    margin = position_value / leverage

    # --------------------------------------------------------
    # Hebel aus Broker-/Instrumentenangabe
    # --------------------------------------------------------

    if data["margin_rate"] > 0:
        instrument_leverage = 1 / data["margin_rate"]
    else:
        instrument_leverage = leverage

    return {
        "lots": lots,
        "units": units,
        "max_loss": max_loss,
        "stop_distance": stop_distance,
        "position_value": position_value,
        "pip_value": pip_value,
        "margin": margin,
        "instrument_leverage": instrument_leverage,
        "category": category,
        "contract_size": contract_size,
    }


# ============================================================
# TOP NAVIGATION
# ============================================================

st.markdown(
    f"""
<div class="cb-topbar">
    <a class="cb-back" href="{STARTSEITE_URL}" target="_self">
        ←&nbsp;&nbsp;ZURÜCK ZUR STARTSEITE
    </a>
</div>
""",
    unsafe_allow_html=True,
)

# ============================================================
# BRAND
# ============================================================

st.markdown(
    f"""
<div class="cb-brand">

    <div class="cb-logo">
        <img src="{LOGO_PATH}" alt="CountOrBreak Logo">
    </div>

    <div class="cb-calculator">
        <img src="{RECHNER_PATH}" alt="Positionsgrößenrechner">
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
    [0.95, 1.25],
    gap="large",
)

# ============================================================
# LINKES PANEL — TRADE EINGABEN
# ============================================================

with left_col:

    st.markdown(
        """
<div class="cb-panel">

    <div class="cb-panel-header">

        <div class="cb-panel-icon">
            ⚖
        </div>

        <div class="cb-panel-title">
            TRADE-EINGABEN
        </div>

    </div>

</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Instrument
    # --------------------------------------------------------

    instrument = st.selectbox(
        "Instrument",
        list(INSTRUMENTS.keys()),
        index=0,
        key="instrument",
    )

    data = INSTRUMENTS[instrument]

    # --------------------------------------------------------
    # Richtung
    # --------------------------------------------------------

    st.markdown(
        '<div class="cb-label">Richtung</div>',
        unsafe_allow_html=True,
    )

    direction_col1, direction_col2 = st.columns(2)

    with direction_col1:
        if st.button(
            "↗  LONG",
            key="long_button",
            use_container_width=True,
        ):
            st.session_state.direction = "LONG"

    with direction_col2:
        if st.button(
            "↘  SHORT",
            key="short_button",
            use_container_width=True,
        ):
            st.session_state.direction = "SHORT"

    st.markdown(
        f"""
<div class="cb-direction-active">
    AKTUELLE RICHTUNG: {st.session_state.direction}
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Kontogröße
    # --------------------------------------------------------

    account_size = st.number_input(
        "Kontogröße",
        min_value=0.0,
        value=10000.0,
        step=100.0,
        format="%.2f",
        key="account_size",
    )

    # --------------------------------------------------------
    # Kontowährung
    # --------------------------------------------------------

    account_currency = st.selectbox(
        "Kontowährung",
        ["EUR", "USD", "GBP", "CHF"],
        index=0,
        key="account_currency",
    )

    # --------------------------------------------------------
    # Risiko
    # --------------------------------------------------------

    risk_percent = st.number_input(
        "Risiko pro Trade",
        min_value=0.01,
        max_value=100.0,
        value=1.00,
        step=0.25,
        format="%.2f",
        key="risk_percent",
    )

    # --------------------------------------------------------
    # Einstieg
    # --------------------------------------------------------

    entry_price = st.number_input(
        "Einstiegskurs",
        min_value=0.000001,
        value=float(data["default_price"]),
        step=float(data["pip_size"]),
        format="%.5f",
        key=f"entry_{instrument}",
    )

    # --------------------------------------------------------
    # Stop Loss
    # --------------------------------------------------------

    stop_price = st.number_input(
        "Stop-Loss-Kurs",
        min_value=0.000001,
        value=float(data["default_stop"]),
        step=float(data["pip_size"]),
        format="%.5f",
        key=f"stop_{instrument}",
    )

    # --------------------------------------------------------
    # Hebel
    # --------------------------------------------------------

    leverage_options = [10, 20, 30, 50, 100, 200, 500]

    leverage = st.selectbox(
        "Verwendeter Hebel",
        leverage_options,
        index=2,
        format_func=lambda x: f"1 : {x}",
        key="leverage",
    )

    # --------------------------------------------------------
    # Instrument Info
    # --------------------------------------------------------

    st.markdown(
        f"""
<div class="cb-info">
    Kategorie: {data["category"]}<br>
    Contract Size: {format_number(data["contract_size"], 0)} Einheiten pro Lot<br>
    Pip-Wert: {format_number(data["pip_value_per_lot"], 2)}
</div>
""",
        unsafe_allow_html=True,
    )


# ============================================================
# BERECHNEN
# ============================================================

result = calculate_position(
    instrument=instrument,
    account_size=account_size,
    risk_percent=risk_percent,
    entry_price=entry_price,
    stop_price=stop_price,
    leverage=leverage,
)


# ============================================================
# RECHTES PANEL — ERGEBNIS
# ============================================================

with right_col:

    st.markdown(
        """
<div class="cb-result-panel">

    <div class="cb-result-header">
        <span>◎</span>
        <span>ERGEBNIS</span>
    </div>

</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        """
<div class="cb-result-title">

    <div class="cb-result-line"></div>

    <div>EMPFOHLENE POSITION</div>

    <div class="cb-result-line right"></div>

</div>
""",
        unsafe_allow_html=True,
    )

    lots = result["lots"]
    units = result["units"]

    if lots > 0:

        st.markdown(
            f"""
<div class="cb-lots">
    {format_number(lots, 2)} LOTS
</div>

<div class="cb-units">
    = {format_number(units, 0)} EINHEITEN
</div>
""",
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            """
<div class="cb-lots">
    0,00 LOTS
</div>

<div class="cb-units">
    = 0 EINHEITEN
</div>
""",
            unsafe_allow_html=True,
        )

    # --------------------------------------------------------
    # Statistiken
    # --------------------------------------------------------

    st.markdown(
        '<div class="cb-divider"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="cb-stat">
    <div class="cb-stat-name">Max. Verlust</div>
    <div class="cb-stat-value">
        {format_number(result["max_loss"], 2)} {account_currency}
    </div>
</div>

<div class="cb-stat">
    <div class="cb-stat-name">Stop-Abstand</div>
    <div class="cb-stat-value">
        {format_number(result["stop_distance"], 1)} Pips
    </div>
</div>

<div class="cb-stat">
    <div class="cb-stat-name">Positionswert</div>
    <div class="cb-stat-value">
        {format_number(result["position_value"], 2)} {data["currency"]}
    </div>
</div>

<div class="cb-stat">
    <div class="cb-stat-name">Pip-Wert</div>
    <div class="cb-stat-value">
        {format_number(result["pip_value"], 2)} {data["currency"]}
    </div>
</div>

<div class="cb-stat">
    <div class="cb-stat-name">Risikoprozent</div>
    <div class="cb-stat-value">
        {format_number(risk_percent, 2)} %
    </div>
</div>
""",
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # Margin & Hebel
    # --------------------------------------------------------

    st.markdown(
        """
<div class="cb-margin-title">
    ⚖ &nbsp; MARGIN & HEBEL
</div>
""",
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
<div class="cb-stat">
    <div class="cb-stat-name">
        Erforderliche Margin
    </div>
    <div class="cb-stat-value">
        {format_number(result["margin"], 2)} {account_currency}
    </div>
</div>

<div class="cb-stat">
    <div class="cb-stat-name">
        Verwendeter Hebel
    </div>
    <div class="cb-stat-value">
        1 : {leverage}
    </div>
</div>

<div class="cb-stat">
    <div class="cb-stat-name">
        Freie Margin (geschätzt)
    </div>
    <div class="cb-stat-value">
        {format_number(max(0, account_size - result["margin"]), 2)}
        {account_currency}
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

risk_amount = result["max_loss"]

risk_ratio = min(max(risk_percent / 5.0, 0), 1)

st.markdown(
    f"""
<div class="cb-risk">

    <div class="cb-risk-title">
        🛡 &nbsp; RISIKOÜBERSICHT
    </div>

    <div class="cb-risk-content">

        <div class="cb-risk-circle">

            <div class="cb-risk-circle-inner">

                <div class="cb-risk-percent">
                    {format_number(risk_percent, 2)} %
                </div>

            </div>

        </div>

        <div>

            <div class="cb-risk-amount">
                {format_number(risk_amount, 2)} {account_currency}
            </div>

            <div style="
                color:#D0D0D0;
                font-size:15px;
                margin-top:4px;
            ">
                von {format_number(account_size, 2)} {account_currency}
            </div>

            <div style="
                margin-top:13px;
                color:#8A8A8A;
                font-size:12px;
            ">
                Maximales Risiko dieses Trades
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
        CFDs sind komplexe Instrumente und bergen aufgrund der
        Hebelwirkung ein hohes Risiko, schnell Geld zu verlieren.
        Ein Großteil der Kleinanlegerkonten verliert beim CFD-Handel
        Geld. Überlegen Sie, ob Sie verstehen, wie CFDs funktionieren
        und ob Sie es sich leisten können, das hohe Risiko einzugehen,
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
<div style="
    text-align:center;
    margin-top:25px;
    color:#575757;
    font-size:10px;
    letter-spacing:0.6px;
">
    COUNT OR BREAK &nbsp;•&nbsp; RISK FIRST. PROFITS SECOND.
</div>
""",
    unsafe_allow_html=True,
)
