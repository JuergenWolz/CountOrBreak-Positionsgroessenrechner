import streamlit as st
import math
from pathlib import Path


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
# KONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent

LOGO_PATH = BASE_DIR / "logo.png"
CALCULATOR_PATH = BASE_DIR / "rechner.png"


# Dunkler, eleganter CountOrBreak-Goldton
GOLD = "#C99A2E"
GOLD_LIGHT = "#F1CC68"
GOLD_BRIGHT = "#FFE39A"
GOLD_DARK = "#9A7118"

BLACK = "#050505"
BLACK_SOFT = "#0A0A0A"
PANEL = "#101010"
PANEL_2 = "#141414"
BORDER = "#343434"
TEXT = "#F2F2F2"
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

    html, body, [data-testid="stAppViewContainer"] {{
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(201,154,46,0.075),
                transparent 34%
            ),
            linear-gradient(
                180deg,
                #020202 0%,
                #050505 45%,
                #020202 100%
            ) !important;
        color: {TEXT};
    }}

    [data-testid="stAppViewContainer"] {{
        min-height: 100vh;
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    [data-testid="stToolbar"] {{
        visibility: hidden;
        height: 0;
    }}

    .block-container {{
        max-width: 1500px !important;
        padding-top: 1.5rem !important;
        padding-bottom: 3rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }}


    /* --------------------------------------------------------
       ZURÜCK BUTTON
    -------------------------------------------------------- */

    .back-wrapper {{
        margin-bottom: 1.4rem;
    }}

    .back-button {{
        display: inline-flex;
        align-items: center;
        gap: 10px;

        padding: 11px 19px;

        border: 1px solid {GOLD_DARK};
        border-radius: 10px;

        background:
            linear-gradient(
                135deg,
                rgba(20,20,20,0.98),
                rgba(8,8,8,0.98)
            );

        color: {GOLD_LIGHT} !important;

        text-decoration: none !important;

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 14px;
        font-weight: 600;
        letter-spacing: 1.2px;

        box-shadow:
            0 0 0 rgba(201,154,46,0),
            inset 0 0 15px rgba(201,154,46,0.025);

        transition:
            all 0.25s ease;
    }}

    .back-button:hover {{
        color: {GOLD_BRIGHT} !important;

        border-color: {GOLD_LIGHT};

        background:
            linear-gradient(
                135deg,
                rgba(38,29,10,0.98),
                rgba(14,11,5,0.98)
            );

        box-shadow:
            0 0 18px rgba(201,154,46,0.25),
            inset 0 0 18px rgba(201,154,46,0.06);

        transform: translateY(-1px);
    }}

    .back-arrow {{
        font-size: 18px;
        line-height: 1;
    }}


    /* --------------------------------------------------------
       HEADER
    -------------------------------------------------------- */

    .top-brand {{
        display: flex;
        align-items: center;
        justify-content: center;

        min-height: 105px;

        margin-bottom: 20px;
    }}

    .top-brand img {{
        max-height: 115px;
        width: auto;

        object-fit: contain;

        filter:
            drop-shadow(0 0 9px rgba(201,154,46,0.16));
    }}

    .calculator-logo {{
        display: flex;
        justify-content: center;
        align-items: center;

        margin-bottom: 18px;
    }}

    .calculator-logo img {{
        width: 95px;
        height: 95px;

        object-fit: contain;

        border-radius: 18px;

        filter:
            drop-shadow(0 0 12px rgba(201,154,46,0.24));
    }}


    /* --------------------------------------------------------
       TITEL
    -------------------------------------------------------- */

    .title-box {{
        position: relative;

        width: 100%;

        padding: 21px 25px 18px;

        margin-bottom: 25px;

        border: 1px solid {GOLD_DARK};
        border-radius: 14px;

        background:
            linear-gradient(
                180deg,
                rgba(23,23,23,0.98),
                rgba(7,7,7,0.98)
            );

        box-shadow:
            0 0 18px rgba(201,154,46,0.09),
            inset 0 0 30px rgba(201,154,46,0.025);

        text-align: center;
    }}

    .title-row {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 22px;
    }}

    .title-line {{
        flex: 1;
        height: 1px;
        max-width: 180px;

        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD_DARK}
            );

        box-shadow:
            0 0 7px rgba(201,154,46,0.15);
    }}

    .title-line.right {{
        background:
            linear-gradient(
                90deg,
                {GOLD_DARK},
                transparent
            );
    }}

    .main-title {{
        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        color: {GOLD_LIGHT};

        font-size: clamp(25px, 3vw, 44px);

        font-weight: 500;

        letter-spacing: 2px;

        text-transform: uppercase;

        text-shadow:
            0 0 10px rgba(201,154,46,0.12);
    }}

    .subtitle {{
        margin-top: 4px;

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        color: #D7CBA9;

        font-size: 18px;

        letter-spacing: 1.1px;
    }}


    /* --------------------------------------------------------
       PANELS
    -------------------------------------------------------- */

    .panel {{
        background:
            linear-gradient(
                145deg,
                rgba(18,18,18,0.98),
                rgba(5,5,5,0.99)
            );

        border: 1px solid {BORDER};

        border-radius: 15px;

        padding: 25px;

        min-height: 100%;

        box-shadow:
            inset 0 0 35px rgba(255,255,255,0.008),
            0 0 0 rgba(201,154,46,0);

        transition:
            border-color 0.25s ease,
            box-shadow 0.25s ease;
    }}

    .panel:hover {{
        border-color: #4A4A4A;

        box-shadow:
            inset 0 0 35px rgba(201,154,46,0.012),
            0 0 12px rgba(201,154,46,0.035);
    }}

    .panel-header {{
        display: flex;
        align-items: center;
        gap: 12px;

        margin-bottom: 24px;

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 22px;

        color: {GOLD_LIGHT};

        letter-spacing: 0.7px;

        text-transform: uppercase;
    }}

    .panel-icon {{
        color: {GOLD};

        font-size: 24px;

        filter:
            drop-shadow(0 0 5px rgba(201,154,46,0.25));
    }}


    /* --------------------------------------------------------
       STREAMLIT INPUTS
    -------------------------------------------------------- */

    label,
    [data-testid="stWidgetLabel"] p {{
        color: #E7E7E7 !important;

        font-size: 15px !important;
    }}

    div[data-baseweb="select"] > div {{
        background: #111111 !important;

        border: 1px solid #57513F !important;

        border-radius: 8px !important;

        color: #F0F0F0 !important;
    }}

    div[data-baseweb="select"] > div:hover {{
        border-color: {GOLD_DARK} !important;
    }}

    input {{
        color: #F2F2F2 !important;

        background: #111111 !important;
    }}

    div[data-testid="stNumberInput"] input {{
        border-color: #4A4436 !important;
    }}

    div[data-testid="stNumberInput"] input:focus {{
        border-color: {GOLD_DARK} !important;

        box-shadow:
            0 0 0 1px {GOLD_DARK} !important;
    }}

    button[kind="secondary"] {{
        border: 1px solid #4A4A4A !important;

        background: #111111 !important;

        color: #EAEAEA !important;

        border-radius: 8px !important;
    }}

    button[kind="secondary"]:hover {{
        border-color: {GOLD} !important;

        color: {GOLD_LIGHT} !important;
    }}


    /* --------------------------------------------------------
       LONG / SHORT BUTTONS
    -------------------------------------------------------- */

    .direction-note {{
        text-align: center;

        margin-top: 5px;
        margin-bottom: 15px;

        color: {GOLD};

        font-size: 12px;

        letter-spacing: 0.8px;

        text-transform: uppercase;
    }}


    /* --------------------------------------------------------
       RESULT HEADER
    -------------------------------------------------------- */

    .result-heading {{
        display: flex;
        align-items: center;
        gap: 12px;

        margin-bottom: 26px;

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        color: {GOLD_LIGHT};

        font-size: 22px;

        text-transform: uppercase;

        letter-spacing: 0.7px;
    }}

    .result-heading-icon {{
        font-size: 24px;
        color: {GOLD};
    }}

    .result-title-row {{
        display: flex;
        align-items: center;
        justify-content: center;

        gap: 18px;

        margin-top: 8px;
    }}

    .result-line {{
        flex: 1;

        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD_DARK}
            );

        box-shadow:
            0 0 6px rgba(201,154,46,0.12);
    }}

    .result-line.right {{
        background:
            linear-gradient(
                90deg,
                {GOLD_DARK},
                transparent
            );
    }}

    .result-label {{
        color: {GOLD_LIGHT};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 21px;

        letter-spacing: 0.8px;

        text-transform: uppercase;

        text-align: center;

        white-space: nowrap;
    }}


    /* --------------------------------------------------------
       MAIN RESULT
    -------------------------------------------------------- */

    .main-result {{
        text-align: center;

        margin-top: 25px;
        margin-bottom: 26px;
    }}

    .lot-value {{
        font-family:
            "Arial",
            "Helvetica",
            sans-serif;

        color: {GOLD_BRIGHT};

        font-size: clamp(48px, 6vw, 84px);

        font-weight: 700;

        letter-spacing: -2px;

        line-height: 1;

        text-shadow:
            0 0 7px rgba(255,227,154,0.22),
            0 0 20px rgba(201,154,46,0.20),
            0 0 42px rgba(201,154,46,0.08);
    }}

    .unit-value {{
        margin-top: 15px;

        color: #F0F0F0;

        font-size: 25px;

        letter-spacing: 0.4px;
    }}


    /* --------------------------------------------------------
       RESULT ROWS
    -------------------------------------------------------- */

    .result-row {{
        display: flex;
        align-items: center;
        justify-content: space-between;

        padding: 12px 0;

        border-bottom: 1px solid #262626;

        font-size: 16px;
    }}

    .result-row:last-child {{
        border-bottom: none;
    }}

    .result-name {{
        color: #D9D9D9;
    }}

    .result-number {{
        color: {GOLD_LIGHT};

        font-weight: 500;

        text-align: right;
    }}

    .result-unit {{
        color: #D0D0D0;

        margin-left: 7px;

        font-size: 13px;
    }}


    /* --------------------------------------------------------
       SUBSECTION
    -------------------------------------------------------- */

    .subsection {{
        display: flex;
        align-items: center;
        gap: 10px;

        margin-top: 27px;
        margin-bottom: 10px;

        padding-top: 17px;

        border-top: 1px solid #292929;

        color: {GOLD_LIGHT};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 19px;

        text-transform: uppercase;

        letter-spacing: 0.6px;
    }}

    .subsection-icon {{
        color: {GOLD};
    }}


    /* --------------------------------------------------------
       RISK OVERVIEW
    -------------------------------------------------------- */

    .risk-panel {{
        margin-top: 22px;

        background:
            linear-gradient(
                145deg,
                rgba(18,18,18,0.98),
                rgba(6,6,6,0.98)
            );

        border: 1px solid {BORDER};

        border-radius: 15px;

        padding: 23px 26px;
    }}

    .risk-title {{
        display: flex;
        align-items: center;
        gap: 12px;

        color: {GOLD_LIGHT};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 20px;

        text-transform: uppercase;
    }}

    .risk-content {{
        display: flex;
        align-items: center;
        gap: 30px;

        margin-top: 17px;
    }}

    .risk-circle {{
        width: 125px;
        height: 125px;

        min-width: 125px;

        border-radius: 50%;

        display: flex;
        flex-direction: column;

        align-items: center;
        justify-content: center;

        background:
            radial-gradient(
                circle,
                #080808 54%,
                transparent 55%
            );

        border: 9px solid #353535;

        box-shadow:
            inset 0 0 15px rgba(201,154,46,0.08),
            0 0 10px rgba(0,0,0,0.5);
    }}

    .risk-circle-value {{
        color: {GOLD_LIGHT};

        font-size: 27px;

        font-weight: 600;
    }}

    .risk-circle-label {{
        color: #BEBEBE;

        font-size: 12px;
    }}

    .risk-info {{
        flex: 1;
    }}

    .risk-money {{
        color: {GOLD_LIGHT};

        font-size: 22px;

        font-weight: 500;
    }}

    .risk-account {{
        margin-top: 3px;

        color: #D5D5D5;

        font-size: 16px;
    }}

    .risk-bars {{
        display: flex;

        gap: 3px;

        margin-top: 17px;

        overflow: hidden;
    }}

    .risk-bar {{
        width: 11px;
        height: 24px;

        min-width: 11px;

        background: #292929;

        border: 1px solid #373737;
    }}

    .risk-bar.active {{
        background:
            linear-gradient(
                180deg,
                {GOLD_LIGHT},
                {GOLD_DARK}
            );

        border-color: {GOLD_DARK};

        box-shadow:
            0 0 5px rgba(201,154,46,0.15);
    }}


    /* --------------------------------------------------------
       WARNING
    -------------------------------------------------------- */

    .warning-panel {{
        margin-top: 20px;

        padding: 21px 24px;

        border: 1px solid #755814;

        border-radius: 14px;

        background:
            linear-gradient(
                145deg,
                rgba(20,17,9,0.95),
                rgba(6,6,6,0.98)
            );

        box-shadow:
            inset 0 0 30px rgba(201,154,46,0.025);
    }}

    .warning-title {{
        color: {GOLD_LIGHT};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 19px;

        letter-spacing: 0.7px;

        text-transform: uppercase;

        margin-bottom: 8px;
    }}

    .warning-text {{
        color: #D2D2D2;

        font-size: 14px;

        line-height: 1.55;
    }}


    /* --------------------------------------------------------
       BUTTONS
    -------------------------------------------------------- */

    div.stButton > button {{
        width: 100%;

        min-height: 43px;

        border-radius: 8px !important;

        border: 1px solid #4A4A4A !important;

        background:
            linear-gradient(
                145deg,
                #151515,
                #0D0D0D
            ) !important;

        color: #E7E7E7 !important;

        font-weight: 500 !important;

        transition: all 0.2s ease !important;
    }}

    div.stButton > button:hover {{
        border-color: {GOLD_DARK} !important;

        color: {GOLD_LIGHT} !important;

        box-shadow:
            0 0 12px rgba(201,154,46,0.10) !important;
    }}


    /* --------------------------------------------------------
       MOBILE
    -------------------------------------------------------- */

    @media (max-width: 900px) {{

        .block-container {{
            padding-left: 0.9rem !important;
            padding-right: 0.9rem !important;
            padding-top: 1rem !important;
        }}

        .top-brand img {{
            max-width: 190px;
        }}

        .calculator-logo img {{
            width: 78px;
            height: 78px;
        }}

        .main-title {{
            font-size: 23px;
            letter-spacing: 1px;
        }}

        .subtitle {{
            font-size: 15px;
        }}

        .title-line {{
            max-width: 70px;
        }}

        .panel {{
            padding: 18px;
        }}

        .panel-header {{
            font-size: 19px;
        }}

        .risk-content {{
            align-items: flex-start;
        }}

        .risk-circle {{
            width: 100px;
            height: 100px;
            min-width: 100px;
        }}

        .risk-circle-value {{
            font-size: 22px;
        }}

        .risk-bars {{
            max-width: 100%;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def euro(value: float) -> str:
    """Deutsche Darstellung für Geldwerte."""
    return f"{value:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")


def number_de(value: float, decimals: int = 2) -> str:
    """Deutsche Zahlendarstellung."""
    return (
        f"{value:,.{decimals}f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def get_lot_size(instrument: str) -> float:
    """
    Standard-Kontraktgröße.
    Diese Werte dienen als Presets und können je nach
    Pepperstone-Konto/Instrument abweichen.
    """

    data = {
        "EUR/USD": 100_000,
        "GBP/USD": 100_000,
        "AUD/USD": 100_000,
        "NZD/USD": 100_000,
        "USD/CAD": 100_000,
        "USD/CHF": 100_000,
        "USD/JPY": 100_000,

        "XAU/USD": 100,
        "XAG/USD": 5_000,

        "GER40": 1,
        "US30": 1,
        "NAS100": 1,
        "UK100": 1,

        "BTC/USD": 1,
        "ETH/USD": 1,

        "CUSTOM": 100_000,
    }

    return data.get(instrument, 100_000)


def get_default_stop(instrument: str) -> float:
    defaults = {
        "EUR/USD": 50,
        "GBP/USD": 50,
        "AUD/USD": 50,
        "NZD/USD": 50,
        "USD/CAD": 50,
        "USD/CHF": 50,
        "USD/JPY": 50,

        "XAU/USD": 5,
        "XAG/USD": 0.20,

        "GER40": 50,
        "US30": 100,
        "NAS100": 100,
        "UK100": 50,

        "BTC/USD": 500,
        "ETH/USD": 50,

        "CUSTOM": 50,
    }

    return defaults.get(instrument, 50)


def get_pip_size(instrument: str) -> float:
    """
    Preisbewegung eines Pips/Points.
    """

    data = {
        "EUR/USD": 0.0001,
        "GBP/USD": 0.0001,
        "AUD/USD": 0.0001,
        "NZD/USD": 0.0001,
        "USD/CAD": 0.0001,
        "USD/CHF": 0.0001,
        "USD/JPY": 0.01,

        "XAU/USD": 0.01,
        "XAG/USD": 0.001,

        "GER40": 1.0,
        "US30": 1.0,
        "NAS100": 1.0,
        "UK100": 1.0,

        "BTC/USD": 1.0,
        "ETH/USD": 0.01,

        "CUSTOM": 0.0001,
    }

    return data.get(instrument, 0.0001)


def get_default_price(instrument: str) -> float:
    prices = {
        "EUR/USD": 1.17000,
        "GBP/USD": 1.35000,
        "AUD/USD": 0.65500,
        "NZD/USD": 0.60000,
        "USD/CAD": 1.37500,
        "USD/CHF": 0.80000,
        "USD/JPY": 148.000,

        "XAU/USD": 3400.00,
        "XAG/USD": 38.00,

        "GER40": 23600.0,
        "US30": 45500.0,
        "NAS100": 23500.0,
        "UK100": 9000.0,

        "BTC/USD": 110000.0,
        "ETH/USD": 4000.0,

        "CUSTOM": 1.17000,
    }

    return prices.get(instrument, 1.0)


def calculate_pip_value(
    instrument: str,
    price: float,
    lot_size: float,
    pip_size: float,
) -> float:
    """
    Näherungsweise Berechnung des Wertes einer Pip-/Point-Bewegung
    pro Lot in der Basiswährung.

    Bei klassischen Forex-Paaren mit USD als Quote:
        Pip-Wert = Lotgröße * Pipgröße

    Bei anderen Instrumenten wird die Kontraktgröße direkt
    verwendet.

    Für einen Live-Brokerwert sollte der konkrete Contract
    Specification von Pepperstone verwendet werden.
    """

    # Forex mit USD als Quote
    usd_quote_pairs = {
        "EUR/USD",
        "GBP/USD",
        "AUD/USD",
        "NZD/USD",
    }

    if instrument in usd_quote_pairs:
        return lot_size * pip_size

    # USD/JPY etc. – Näherung über aktuellen Kurs
    if instrument in {"USD/JPY", "USD/CAD", "USD/CHF"}:
        if price > 0:
            return (lot_size * pip_size) / price

    # CFDs / Indizes / Metalle / Krypto
    return lot_size * pip_size


def calculate_position(
    account_size: float,
    risk_percent: float,
    stop_distance: float,
    pip_value: float,
    pip_size: float,
    contract_size: float,
    entry_price: float,
    leverage: float,
):
    """
    Berechnet die empfohlene Positionsgröße.

    Risiko:
        Konto * Risiko%

    Anzahl Pips/Points:
        Stop-Abstand / Pip-Größe

    Risiko pro Lot:
        Pips * Pip-Wert

    Lots:
        Max. Verlust / Risiko pro Lot
    """

    max_loss = account_size * (risk_percent / 100)

    if stop_distance <= 0:
        return {
            "max_loss": max_loss,
            "distance_units": 0,
            "risk_per_lot": 0,
            "lots": 0,
            "units": 0,
            "position_value": 0,
            "margin": 0,
        }

    if pip_size <= 0 or pip_value <= 0:
        return {
            "max_loss": max_loss,
            "distance_units": 0,
            "risk_per_lot": 0,
            "lots": 0,
            "units": 0,
            "position_value": 0,
            "margin": 0,
        }

    distance_units = stop_distance / pip_size

    risk_per_lot = distance_units * pip_value

    if risk_per_lot <= 0:
        lots = 0
    else:
        lots = max_loss / risk_per_lot

    # Auf zwei Nachkommastellen für Lotdarstellung runden
    lots = max(0, round(lots, 2))

    units = lots * contract_size

    position_value = units * entry_price

    if leverage > 0:
        margin = position_value / leverage
    else:
        margin = 0

    return {
        "max_loss": max_loss,
        "distance_units": distance_units,
        "risk_per_lot": risk_per_lot,
        "lots": lots,
        "units": units,
        "position_value": position_value,
        "margin": margin,
    }


# ============================================================
# HEADER
# ============================================================

# Zurück zur Startseite
#
# Die URL kann später einfach durch die tatsächliche
# Streamlit-URL der CountOrBreak-Startseite ersetzt werden.
#
# Standardmäßig wird browser history verwendet.

st.markdown(
    """
    <div class="back-wrapper">
        <a class="back-button" href="javascript:history.back()">
            <span class="back-arrow">←</span>
            <span>ZURÜCK ZUR STARTSEITE</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)


# Logo
if LOGO_PATH.exists():
    st.markdown('<div class="top-brand">', unsafe_allow_html=True)
    st.image(str(LOGO_PATH), width=210)
    st.markdown("</div>", unsafe_allow_html=True)


# Rechner-Icon
if CALCULATOR_PATH.exists():
    st.markdown('<div class="calculator-logo">', unsafe_allow_html=True)
    st.image(str(CALCULATOR_PATH), width=95)
    st.markdown("</div>", unsafe_allow_html=True)


# Titel
st.markdown(
    """
    <div class="title-box">

        <div class="title-row">

            <div class="title-line"></div>

            <div class="main-title">
                Positionsgrößenrechner
            </div>

            <div class="title-line right"></div>

        </div>

        <div class="subtitle">
            Risk first. Profits second.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# SESSION STATE
# ============================================================

if "direction" not in st.session_state:
    st.session_state.direction = "LONG"


# ============================================================
# HAUPTBEREICH
# ============================================================

left, right = st.columns(
    [0.95, 1.35],
    gap="large",
)


# ============================================================
# LINKE SEITE – TRADE-EINGABEN
# ============================================================

with left:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-header">
                <span class="panel-icon">⚖</span>
                <span>Trade-Eingaben</span>
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
            "AUD/USD",
            "NZD/USD",
            "USD/CAD",
            "USD/CHF",
            "USD/JPY",
            "XAU/USD",
            "XAG/USD",
            "GER40",
            "US30",
            "NAS100",
            "UK100",
            "BTC/USD",
            "ETH/USD",
            "CUSTOM",
        ],
        index=0,
        key="instrument",
    )

    st.markdown("**Richtung**")

    direction_col1, direction_col2 = st.columns(2)

    with direction_col1:
        if st.button(
            "↗ LONG",
            key="long_button",
            use_container_width=True,
        ):
            st.session_state.direction = "LONG"

    with direction_col2:
        if st.button(
            "↓ SHORT",
            key="short_button",
            use_container_width=True,
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
    # KONTO
    # --------------------------------------------------------

    account_size = st.number_input(
        "Kontogröße",
        min_value=0.0,
        value=10_000.0,
        step=500.0,
        format="%.2f",
        key="account_size",
    )

    currency = st.selectbox(
        "Kontowährung",
        ["EUR", "USD", "GBP", "CHF"],
        index=0,
        key="currency",
    )

    # --------------------------------------------------------
    # RISIKO
    # --------------------------------------------------------

    risk_percent = st.number_input(
        "Risiko pro Trade",
        min_value=0.01,
        max_value=100.0,
        value=1.0,
        step=0.25,
        format="%.2f",
        key="risk_percent",
    )

    # --------------------------------------------------------
    # PREIS
    # --------------------------------------------------------

    default_price = get_default_price(instrument)

    entry_price = st.number_input(
        "Einstiegskurs",
        min_value=0.00001,
        value=float(default_price),
        step=float(get_pip_size(instrument)),
        format="%.5f",
        key="entry_price",
    )

    # --------------------------------------------------------
    # STOP
    # --------------------------------------------------------

    default_stop = get_default_stop(instrument)

    stop_distance = st.number_input(
        "Stop-Abstand",
        min_value=0.00001,
        value=float(default_stop),
        step=float(get_pip_size(instrument)),
        format="%.5f",
        key="stop_distance",
    )

    # --------------------------------------------------------
    # HEBEL
    # --------------------------------------------------------

    leverage = st.number_input(
        "Hebel",
        min_value=1.0,
        max_value=500.0,
        value=30.0,
        step=1.0,
        format="%.0f",
        key="leverage",
    )

    # --------------------------------------------------------
    # KONTRAKTGRÖSSE
    # --------------------------------------------------------

    contract_size = st.number_input(
        "Kontraktgröße / Lot",
        min_value=0.000001,
        value=float(get_lot_size(instrument)),
        step=1.0,
        format="%.6f",
        key=f"contract_{instrument}",
        help=(
            "Die Kontraktgröße kann je nach CFD-Instrument "
            "und Broker variieren. Für Pepperstone bitte "
            "die jeweilige Contract Specification prüfen."
        ),
    )

    # --------------------------------------------------------
    # PIP / POINT
    # --------------------------------------------------------

    pip_size = st.number_input(
        "Pip-/Point-Größe",
        min_value=0.000001,
        value=float(get_pip_size(instrument)),
        step=0.0001,
        format="%.6f",
        key=f"pip_{instrument}",
    )

    # --------------------------------------------------------
    # PIP WERT
    # --------------------------------------------------------

    auto_pip_value = calculate_pip_value(
        instrument=instrument,
        price=entry_price,
        lot_size=contract_size,
        pip_size=pip_size,
    )

    pip_value = st.number_input(
        "Pip-/Point-Wert pro Lot",
        min_value=0.000001,
        value=float(max(auto_pip_value, 0.000001)),
        step=0.01,
        format="%.4f",
        key=f"pipvalue_{instrument}",
        help=(
            "Für exakte Pepperstone-CFD-Berechnungen kann hier "
            "der tatsächliche Wert aus der jeweiligen "
            "Contract Specification eingetragen werden."
        ),
    )


# ============================================================
# BERECHNUNG
# ============================================================

result = calculate_position(
    account_size=account_size,
    risk_percent=risk_percent,
    stop_distance=stop_distance,
    pip_value=pip_value,
    pip_size=pip_size,
    contract_size=contract_size,
    entry_price=entry_price,
    leverage=leverage,
)


# ============================================================
# RECHTE SEITE – ERGEBNIS
# ============================================================

with right:

    st.markdown(
        """
        <div class="panel">

            <div class="result-heading">
                <span class="result-heading-icon">◎</span>
                <span>Ergebnis</span>
            </div>

            <div class="result-title-row">

                <div class="result-line"></div>

                <div class="result-label">
                    Empfohlene Position
                </div>

                <div class="result-line right"></div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # LOTS
    # --------------------------------------------------------

    lots = result["lots"]

    units = result["units"]

    st.markdown(
        f"""
        <div class="main-result">

            <div class="lot-value">
                {number_de(lots, 2)} LOTS
            </div>

            <div class="unit-value">
                = {number_de(units, 0)} EINHEITEN
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # DETAILERGEBNISSE
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="result-row">
            <span class="result-name">Max. Verlust</span>
            <span class="result-number">
                {euro(result["max_loss"])}
                <span class="result-unit">{currency}</span>
            </span>
        </div>

        <div class="result-row">
            <span class="result-name">Stop-Abstand</span>
            <span class="result-number">
                {number_de(stop_distance, 2)}
                <span class="result-unit">
                    {"Pips" if "40" not in instrument and instrument not in ["US30", "NAS100", "GER40", "UK100"] else "Points"}
                </span>
            </span>
        </div>

        <div class="result-row">
            <span class="result-name">Positionswert</span>
            <span class="result-number">
                {euro(result["position_value"])}
                <span class="result-unit">{currency}</span>
            </span>
        </div>

        <div class="result-row">
            <span class="result-name">Pip-/Point-Wert</span>
            <span class="result-number">
                {euro(pip_value)}
                <span class="result-unit">{currency}</span>
            </span>
        </div>

        <div class="result-row">
            <span class="result-name">Risikoprozent</span>
            <span class="result-number">
                {number_de(risk_percent, 2)}
                <span class="result-unit">%</span>
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # --------------------------------------------------------
    # MARGIN & HEBEL
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="subsection">
            <span class="subsection-icon">⚖</span>
            <span>Margin &amp; Hebel</span>
        </div>

        <div class="result-row">
            <span class="result-name">
                Erforderliche Margin
            </span>

            <span class="result-number">
                {euro(result["margin"])}
                <span class="result-unit">{currency}</span>
            </span>
        </div>

        <div class="result-row">
            <span class="result-name">
                Verwendeter Hebel
            </span>

            <span class="result-number">
                1 : {number_de(leverage, 0)}
            </span>
        </div>

        <div class="result-row">
            <span class="result-name">
                Freie Margin (geschätzt)
            </span>

            <span class="result-number">
                {euro(max(account_size - result["margin"], 0))}
                <span class="result-unit">{currency}</span>
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown("</div>", unsafe_allow_html=True)


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

risk_fraction = min(max(risk_percent / 10.0, 0), 1)

active_bars = max(1, min(20, math.ceil(risk_fraction * 20)))

bars_html = ""

for i in range(20):
    if i < active_bars:
        bars_html += '<div class="risk-bar active"></div>'
    else:
        bars_html += '<div class="risk-bar"></div>'


st.markdown(
    f"""
    <div class="risk-panel">

        <div class="risk-title">
            <span>♢</span>
            <span>Risikoübersicht</span>
        </div>

        <div class="risk-content">

            <div class="risk-circle">

                <div class="risk-circle-value">
                    {number_de(risk_percent, 2)}
                </div>

                <div class="risk-circle-label">
                    PRO TRADE
                </div>

            </div>

            <div class="risk-info">

                <div class="risk-money">
                    {euro(result["max_loss"])} {currency}
                </div>

                <div class="risk-account">
                    von {euro(account_size)} {currency}
                </div>

                <div class="risk-bars">
                    {bars_html}
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
    <div class="warning-panel">

        <div class="warning-title">
            ⚠ &nbsp; Risikohinweis
        </div>

        <div class="warning-text">

            CFDs sind komplexe Instrumente und bergen aufgrund
            der Hebelwirkung ein hohes Risiko, schnell Geld zu
            verlieren. Ein erheblicher Anteil der
            Kleinanlegerkonten verliert Geld beim CFD-Handel
            mit diesem Anbieter. Überlegen Sie, ob Sie
            verstehen, wie CFDs funktionieren und ob Sie es
            sich leisten können, das hohe Risiko einzugehen,
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
    f"""
    <div style="
        text-align:center;
        margin-top:28px;
        color:#686868;
        font-family:Georgia,serif;
        font-size:11px;
        letter-spacing:0.8px;
    ">
        COUNT OR BREAK · RISK FIRST. PROFITS SECOND.
    </div>
    """,
    unsafe_allow_html=True,
)
