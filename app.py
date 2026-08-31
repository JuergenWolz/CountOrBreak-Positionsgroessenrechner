import streamlit as st
from pathlib import Path
import base64


# ============================================================
# COUNT OR BREAK
# POSITIONSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# DATEIEN
# ============================================================

BASE_PATH = Path(__file__).parent


def find_file(names):
    for name in names:
        path = BASE_PATH / name
        if path.exists():
            return path
    return None


logo_path = find_file([
    "logo.png",
    "Logo.png",
    "countorbreak_logo.png",
    "CountOrBreak_logo.png",
    "countorbreak.png",
    "CountOrBreak.png",
    "cb_logo.png",
    "CB_Logo.png",
])


calculator_path = find_file([
    "rechner.png",
    "Rechner.png",
    "calculator.png",
    "Calculator.png",
    "icon_rechner.png",
    "positionsgroessenrechner.png",
    "positionsgrößenrechner.png",
])


def image_base64(path):
    if path is None:
        return None

    try:
        return base64.b64encode(
            path.read_bytes()
        ).decode("utf-8")
    except Exception:
        return None


logo_b64 = image_base64(logo_path)
calculator_b64 = image_base64(calculator_path)


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def fmt(value, decimals=2):
    return (
        f"{value:,.{decimals}f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def euro(value, decimals=2):
    return f"{fmt(value, decimals)} €"


def safe_div(a, b):
    if b == 0:
        return 0
    return a / b


# ============================================================
# CSS
# ============================================================

st.html(
    """
<style>

:root {
    --cb-gold: #C9A35A;
    --cb-gold-light: #E0BD72;
    --cb-gold-bright: #F0D28E;
    --cb-gold-dark: #735019;

    --cb-black: #030303;
    --cb-panel: #090909;
    --cb-panel-2: #0D0D0D;

    --cb-white: #EEE5D6;
    --cb-muted: #968F85;

    --cb-green: #91B96A;
}


/* ============================================================
   GLOBAL
   ============================================================ */

.stApp {
    background:
        radial-gradient(
            circle at 50% -10%,
            rgba(201,163,90,0.11),
            transparent 40%
        ),
        radial-gradient(
            circle at 0% 50%,
            rgba(201,163,90,0.035),
            transparent 30%
        ),
        #030303;
}


.block-container {
    max-width: 1420px;
    padding-top: 1.6rem;
    padding-bottom: 3rem;
}


header {
    visibility: hidden;
}


#MainMenu {
    visibility: hidden;
}


footer {
    visibility: hidden;
}


/* ============================================================
   TOP HEADER
   ============================================================ */

.cb-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 25px;

    margin-bottom: 20px;
}


.cb-top-left {
    display: flex;
    align-items: center;
    gap: 20px;
}


/* LOGO */

.cb-logo {
    width: 112px;
    height: 112px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 18px;

    border: 1px solid rgba(201,163,90,0.65);

    background:
        radial-gradient(
            circle at 50% 40%,
            rgba(201,163,90,0.05),
            transparent 65%
        ),
        #050505;

    box-shadow:
        inset 0 0 30px rgba(201,163,90,0.035),
        0 0 20px rgba(201,163,90,0.08);
}


.cb-logo img {
    width: 96px;
    height: 96px;

    object-fit: contain;
}


/* RECHNER ICON */

.cb-tool-icon {
    width: 78px;
    height: 78px;

    display: flex;
    align-items: center;
    justify-content: center;

    border-radius: 15px;

    border: 1px solid rgba(201,163,90,0.58);

    background:
        linear-gradient(
            145deg,
            #15120D,
            #050505
        );

    box-shadow:
        inset 0 0 22px rgba(201,163,90,0.04),
        0 0 16px rgba(201,163,90,0.07);
}


.cb-tool-icon img {
    width: 61px;
    height: 61px;

    object-fit: contain;
}


.cb-fallback-icon {
    font-size: 34px;
    color: var(--cb-gold-light);
}


/* TOP RIGHT */

.cb-top-note {
    padding: 11px 17px;

    border: 1px solid rgba(201,163,90,0.35);

    border-radius: 8px;

    color: #BEB4A4;

    background: rgba(8,8,8,0.7);

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 12px;

    letter-spacing: 0.08em;

    text-transform: uppercase;
}


/* ============================================================
   TITLE FRAME
   ============================================================ */

.cb-title-frame {

    position: relative;

    width: 100%;

    padding: 25px 25px 23px;

    margin-bottom: 25px;

    text-align: center;

    border: 1px solid rgba(201,163,90,0.70);

    border-radius: 10px;

    background:
        linear-gradient(
            145deg,
            rgba(17,17,17,0.98),
            rgba(5,5,5,0.98)
        );

    box-shadow:
        inset 0 0 35px rgba(201,163,90,0.025),
        0 0 25px rgba(201,163,90,0.05);
}


.cb-title-frame:before {
    content: "";

    position: absolute;

    left: 15%;
    right: 15%;
    top: 0;

    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            var(--cb-gold-light),
            transparent
        );

    box-shadow:
        0 0 10px rgba(201,163,90,0.35);
}


.cb-title {
    color: var(--cb-gold-light);

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: clamp(25px, 3vw, 38px);

    font-weight: 500;

    letter-spacing: 0.17em;

    text-transform: uppercase;

    text-shadow:
        0 0 12px rgba(201,163,90,0.18);
}


.cb-title-sub {
    margin-top: 7px;

    color: #81796E;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 12px;

    letter-spacing: 0.19em;

    text-transform: uppercase;
}


/* ============================================================
   MAIN FRAME
   ============================================================ */

.cb-main-frame {

    width: 100%;

    padding: 25px;

    border:
        1px solid rgba(201,163,90,0.47);

    border-radius: 12px;

    background:
        linear-gradient(
            145deg,
            rgba(14,14,14,0.99),
            rgba(5,5,5,0.99)
        );

    box-shadow:
        inset 0 0 50px rgba(201,163,90,0.018),
        0 20px 55px rgba(0,0,0,0.60);
}


/* ============================================================
   SECTION TITLES
   ============================================================ */

.cb-section {
    color: var(--cb-gold-light);

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 18px;

    font-weight: 500;

    letter-spacing: 0.10em;

    text-transform: uppercase;

    margin-bottom: 13px;
}


.cb-section-line {

    height: 1px;

    width: 100%;

    margin: 4px 0 20px;

    background:
        linear-gradient(
            90deg,
            rgba(201,163,90,0.60),
            rgba(201,163,90,0.05),
            transparent
        );
}


/* ============================================================
   INPUTS
   ============================================================ */

div[data-baseweb="select"] > div {

    background: #0A0A0A !important;

    border:
        1px solid rgba(201,163,90,0.38) !important;

    border-radius: 7px !important;
}


div[data-baseweb="input"] > div {

    background: #0A0A0A !important;

    border:
        1px solid rgba(201,163,90,0.38) !important;

    border-radius: 7px !important;
}


input {

    color: #E9DFCF !important;
}


label {

    color: #AAA195 !important;

    font-size: 13px !important;
}


.stRadio label {

    color: #B9AF9F !important;
}


/* ============================================================
   LONG / SHORT
   ============================================================ */

.cb-direction-box {

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 15px;

    margin: 8px 0 22px;

    padding: 12px;

    border:
        1px solid rgba(201,163,90,0.28);

    border-radius: 7px;

    background: rgba(201,163,90,0.025);

    color: #AAA093;

    font-size: 12px;

    letter-spacing: 0.05em;
}


/* ============================================================
   RESULT AREA
   ============================================================ */

.cb-result-frame {

    padding: 24px;

    border:
        1px solid rgba(201,163,90,0.62);

    border-radius: 10px;

    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(201,163,90,0.08),
            transparent 62%
        ),
        #080808;

    box-shadow:
        inset 0 0 35px rgba(201,163,90,0.025),
        0 0 22px rgba(201,163,90,0.05);

    text-align: center;
}


.cb-result-label {

    color: #B9AF9F;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 12px;

    letter-spacing: 0.16em;

    text-transform: uppercase;
}


.cb-result-value {

    margin-top: 9px;

    color: var(--cb-gold-bright);

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: clamp(43px, 5vw, 67px);

    font-weight: 500;

    line-height: 1.1;

    letter-spacing: 0.025em;

    text-shadow:
        0 0 16px rgba(201,163,90,0.20);
}


.cb-result-small {

    margin-top: 8px;

    color: #888076;

    font-size: 12px;
}


/* ============================================================
   RESULT CARDS
   ============================================================ */

.cb-card {

    display: flex;

    justify-content: space-between;

    align-items: center;

    min-height: 72px;

    margin-top: 12px;

    padding: 13px 17px;

    border:
        1px solid rgba(201,163,90,0.27);

    border-radius: 8px;

    background:
        linear-gradient(
            145deg,
            #111111,
            #080808
        );

    transition:
        transform 0.18s ease,
        border-color 0.18s ease;
}


.cb-card:hover {

    transform: translateY(-2px);

    border-color:
        rgba(201,163,90,0.55);
}


.cb-card-left {

    display: flex;

    align-items: center;

    gap: 12px;

    color: #AFA598;

    font-size: 13px;
}


.cb-card-icon {

    width: 34px;

    height: 34px;

    display: flex;

    align-items: center;

    justify-content: center;

    border:
        1px solid rgba(201,163,90,0.40);

    border-radius: 50%;

    color: var(--cb-gold);

    font-size: 14px;
}


.cb-card-sub {

    margin-top: 3px;

    color: #6F6961;

    font-size: 11px;
}


.cb-card-value {

    color: #D6C9B7;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 17px;
}


/* ============================================================
   MARGIN
   ============================================================ */

.cb-margin {

    margin-top: 20px;

    padding: 18px 20px;

    border:
        1px solid rgba(201,163,90,0.33);

    border-radius: 8px;

    background: #080808;
}


.cb-margin-title {

    color: var(--cb-gold-light);

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 16px;

    letter-spacing: 0.08em;

    text-transform: uppercase;

    margin-bottom: 12px;
}


.cb-margin-row {

    display: flex;

    justify-content: space-between;

    padding: 8px 0;

    border-bottom:
        1px solid rgba(201,163,90,0.09);

    color: #817A71;

    font-size: 12px;
}


.cb-margin-row:last-child {

    border-bottom: none;
}


.cb-margin-value {

    color: #CFC4B4;
}


/* ============================================================
   RISK INDICATOR
   ============================================================ */

.cb-risk {

    margin-top: 18px;

    padding: 18px;

    border:
        1px solid rgba(201,163,90,0.30);

    border-radius: 8px;

    background:
        linear-gradient(
            145deg,
            #11100D,
            #080808
        );
}


.cb-risk-header {

    display: flex;

    justify-content: space-between;

    align-items: center;

    color: #A59C90;

    font-size: 12px;

    text-transform: uppercase;

    letter-spacing: 0.10em;
}


.cb-risk-percent {

    color: var(--cb-gold-light);

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 18px;
}


.cb-risk-bar {

    width: 100%;

    height: 5px;

    margin-top: 13px;

    overflow: hidden;

    border-radius: 5px;

    background: #1C1A17;
}


.cb-risk-fill {

    height: 100%;

    border-radius: 5px;

    background:
        linear-gradient(
            90deg,
            #76521A,
            #C9A35A,
            #E0BD72
        );

    box-shadow:
        0 0 8px rgba(201,163,90,0.20);
}


.cb-risk-text {

    margin-top: 8px;

    color: #777067;

    font-size: 11px;
}


/* ============================================================
   WARNING
   ============================================================ */

.cb-warning {

    margin-top: 20px;

    padding: 17px 19px;

    border:
        1px solid rgba(201,163,90,0.27);

    border-radius: 8px;

    background:
        rgba(201,163,90,0.018);

    color: #827A70;

    font-size: 11px;

    line-height: 1.65;
}


.cb-warning strong {

    color: #BBAE9C;

    font-weight: 500;
}


/* ============================================================
   FOOTER
   ============================================================ */

.cb-footer {

    padding-top: 22px;

    text-align: center;

    color: #56514B;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 11px;

    letter-spacing: 0.13em;

    text-transform: uppercase;
}


.cb-footer-gold {

    color: #907039;
}


/* ============================================================
   MOBILE
   ============================================================ */

@media (max-width: 850px) {

    .block-container {

        padding-left: 0.65rem;
        padding-right: 0.65rem;
    }


    .cb-main-frame {

        padding: 16px;
    }


    .cb-top {

        align-items: flex-start;
    }


    .cb-top-note {

        display: none;
    }


    .cb-logo {

        width: 78px;
        height: 78px;
    }


    .cb-logo img {

        width: 68px;
        height: 68px;
    }


    .cb-tool-icon {

        width: 62px;
        height: 62px;
    }


    .cb-tool-icon img {

        width: 48px;
        height: 48px;
    }


    .cb-title {

        font-size: 23px;

        letter-spacing: 0.11em;
    }


    .cb-title-sub {

        font-size: 10px;
    }


    .cb-title-frame {

        padding: 20px 10px;
    }


    .cb-result-frame {

        padding: 20px 10px;
    }


    .cb-result-value {

        font-size: 43px;
    }

}

</style>
"""
)


# ============================================================
# HEADER
# ============================================================

logo_html = ""

if logo_b64:

    logo_html = f"""
    <img
        src="data:image/png;base64,{logo_b64}"
        alt="CountOrBreak"
    >
    """

else:

    logo_html = """
    <div style="
        color:#DDBB72;
        font-family:Georgia,serif;
        font-size:28px;
        letter-spacing:3px;
    ">
        CB
    </div>
    """


if calculator_b64:

    calculator_html = f"""
    <img
        src="data:image/png;base64,{calculator_b64}"
        alt="Positionsgrößenrechner"
    >
    """

else:

    calculator_html = """
    <div class="cb-fallback-icon">
        🧮
    </div>
    """


st.html(
    f"""
    <div class="cb-top">

        <div class="cb-top-left">

            <div class="cb-logo">
                {logo_html}
            </div>

            <div class="cb-tool-icon">
                {calculator_html}
            </div>

        </div>


        <div class="cb-top-note">
            Risk Management
        </div>

    </div>
    """
)


# ============================================================
# TITEL
# ============================================================

st.html(
    """
    <div class="cb-title-frame">

        <div class="cb-title">
            Positionsgrößenrechner
        </div>

        <div class="cb-title-sub">
            Risk first. Profits second.
        </div>

    </div>
    """
)


# ============================================================
# MAIN FRAME
# ============================================================

st.html('<div class="cb-main-frame">')

left, right = st.columns(
    [1, 1],
    gap="large"
)


# ============================================================
# LINKE SEITE
# ============================================================

with left:

    # --------------------------------------------------------
    # MARKT
    # --------------------------------------------------------

    st.html(
        """
        <div class="cb-section">
            Trade
        </div>

        <div class="cb-section-line"></div>
        """
    )


    market = st.selectbox(
        "Produkttyp",
        [
            "Forex CFD",
            "Index CFD",
            "Krypto CFD",
            "Rohstoff CFD",
            "Aktien CFD",
            "Futures",
            "Sonstiger CFD",
        ]
    )


    if market == "Forex CFD":
        default_instrument = "EUR/USD"

    elif market == "Index CFD":
        default_instrument = "NAS100"

    elif market == "Krypto CFD":
        default_instrument = "BTC/USD"

    elif market == "Rohstoff CFD":
        default_instrument = "XAU/USD"

    else:
        default_instrument = ""


    instrument = st.text_input(
        "Instrument",
        value=default_instrument,
        placeholder="z. B. EUR/USD"
    )


    # --------------------------------------------------------
    # RICHTUNG
    # --------------------------------------------------------

    direction = st.radio(
        "Richtung",
        ["Long", "Short"],
        horizontal=True
    )


    if direction == "Long":

        direction_text = (
            "Long · Stop-Loss unterhalb des Einstiegs"
        )

    else:

        direction_text = (
            "Short · Stop-Loss oberhalb des Einstiegs"
        )


    st.html(
        f"""
        <div class="cb-direction-box">
            {direction_text}
        </div>
        """
    )


    # --------------------------------------------------------
    # KONTO
    # --------------------------------------------------------

    st.html(
        """
        <div class="cb-section">
            Konto & Risiko
        </div>

        <div class="cb-section-line"></div>
        """
    )


    account_col, risk_col = st.columns(2)


    with account_col:

        account_size = st.number_input(
            "Kontogröße (€)",
            min_value=0.01,
            value=10000.00,
            step=100.00,
            format="%.2f"
        )


    with risk_col:

        risk_percent = st.number_input(
            "Risiko (%)",
            min_value=0.01,
            max_value=100.0,
            value=1.00,
            step=0.10,
            format="%.2f"
        )


    max_risk = (
        account_size
        * risk_percent
        / 100
    )


    # --------------------------------------------------------
    # PREIS
    # --------------------------------------------------------

    st.html(
        """
        <div class="cb-section">
            Einstieg & Stop
        </div>

        <div class="cb-section-line"></div>
        """
    )


    if market == "Forex CFD":

        default_entry = 1.17000
        default_stop = 1.16500

        price_step = 0.00001
        price_format = "%.5f"

    else:

        default_entry = 100.00

        if direction == "Long":
            default_stop = 98.00
        else:
            default_stop = 102.00

        price_step = 0.10
        price_format = "%.4f"


    price_col1, price_col2 = st.columns(2)


    with price_col1:

        entry_price = st.number_input(
            "Einstieg",
            min_value=0.00000001,
            value=default_entry,
            step=price_step,
            format=price_format
        )


    with price_col2:

        stop_loss = st.number_input(
            "Stop-Loss",
            min_value=0.00000001,
            value=default_stop,
            step=price_step,
            format=price_format
        )


    take_profit = st.number_input(
        "Take-Profit (optional)",
        min_value=0.0,
        value=0.0,
        step=price_step,
        format=price_format
    )


    # --------------------------------------------------------
    # INSTRUMENT DETAILS
    # --------------------------------------------------------

    st.html(
        """
        <div class="cb-section">
            Instrument Details
        </div>

        <div class="cb-section-line"></div>
        """
    )


    if market == "Forex CFD":

        col1, col2 = st.columns(2)


        with col1:

            lot_size = st.number_input(
                "Einheiten pro Lot",
                min_value=1.0,
                value=100000.0,
                step=1000.0,
                format="%.0f"
            )


        with col2:

            pip_size = st.number_input(
                "Pip-Größe",
                min_value=0.00000001,
                value=0.00010,
                step=0.00001,
                format="%.5f"
            )


        pip_value = st.number_input(
            "Pip-Wert pro Lot (€)",
            min_value=0.0001,
            value=10.00,
            step=0.10,
            format="%.2f"
        )


        leverage = st.number_input(
            "Hebel",
            min_value=1.0,
            value=30.0,
            step=1.0,
            format="%.0f"
        )


        price_distance = abs(
            entry_price - stop_loss
        )


        pips = safe_div(
            price_distance,
            pip_size
        )


        risk_per_lot = (
            pips
            * pip_value
        )


        lots = safe_div(
            max_risk,
            risk_per_lot
        )


        units = (
            lots
            * lot_size
        )


        position_value = (
            units
            * entry_price
        )


        margin = safe_div(
            position_value,
            leverage
        )


    elif market == "Futures":

        tick_size = st.number_input(
            "Tick-Größe",
            min_value=0.00000001,
            value=0.25,
            step=0.01,
            format="%.4f"
        )


        tick_value = st.number_input(
            "Tick-Wert (€)",
            min_value=0.0001,
            value=12.50,
            step=0.50,
            format="%.2f"
        )


        leverage = st.number_input(
            "Hebel",
            min_value=1.0,
            value=20.0,
            step=1.0,
            format="%.0f"
        )


        price_distance = abs(
            entry_price - stop_loss
        )


        ticks = safe_div(
            price_distance,
            tick_size
        )


        risk_per_contract = (
            ticks
            * tick_value
        )


        contracts = safe_div(
            max_risk,
            risk_per_contract
        )


        units = contracts


        position_value = (
            contracts
            * entry_price
        )


        margin = safe_div(
            position_value,
            leverage
        )


    else:

        value_per_move = st.number_input(
            "Wert pro 1,00 Bewegung (€)",
            min_value=0.0001,
            value=1.00,
            step=0.10,
            format="%.4f"
        )


        contract_size = st.number_input(
            "Kontraktgröße",
            min_value=0.0001,
            value=1.0,
            step=1.0,
            format="%.4f"
        )


        leverage = st.number_input(
            "Hebel",
            min_value=1.0,
            value=5.0,
            step=1.0,
            format="%.0f"
        )


        price_distance = abs(
            entry_price - stop_loss
        )


        risk_per_unit = (
            price_distance
            * value_per_move
        )


        units = safe_div(
            max_risk,
            risk_per_unit
        )


        position_value = (
            units
            * contract_size
            * entry_price
        )


        margin = safe_div(
            position_value,
            leverage
        )


    # --------------------------------------------------------
    # VALIDIERUNG
    # --------------------------------------------------------

    valid = True

    error = ""


    if entry_price <= 0:

        valid = False
        error = "Der Einstieg muss größer als 0 sein."


    elif stop_loss <= 0:

        valid = False
        error = "Der Stop-Loss muss größer als 0 sein."


    elif entry_price == stop_loss:

        valid = False
        error = (
            "Einstieg und Stop-Loss dürfen nicht identisch sein."
        )


    elif direction == "Long" and stop_loss >= entry_price:

        valid = False
        error = (
            "Bei einem Long-Trade muss der Stop-Loss "
            "unterhalb des Einstiegs liegen."
        )


    elif direction == "Short" and stop_loss <= entry_price:

        valid = False
        error = (
            "Bei einem Short-Trade muss der Stop-Loss "
            "oberhalb des Einstiegs liegen."
        )


# ============================================================
# RECHTE SEITE
# ============================================================

with right:

    st.html(
        """
        <div class="cb-section">
            Risiko-Ergebnis
        </div>

        <div class="cb-section-line"></div>
        """
    )


    if valid:

        # ----------------------------------------------------
        # HAUPTERGEBNIS
        # ----------------------------------------------------

        if market == "Forex CFD":

            result_value = (
                f"{fmt(lots, 2)} Lots"
            )

            result_small = (
                f"= {fmt(units, 0)} Einheiten"
            )

        elif market == "Futures":

            result_value = (
                f"{fmt(contracts, 2)} Kontrakte"
            )

            result_small = (
                "auf Basis der angegebenen Tick-Daten"
            )

        else:

            result_value = (
                f"{fmt(units, 2)} Einheiten"
            )

            result_small = (
                f"Positionswert: {euro(position_value)}"
            )


        st.html(
            f"""
            <div class="cb-result-frame">

                <div class="cb-result-label">
                    Empfohlene Positionsgröße
                </div>

                <div class="cb-result-value">
                    {result_value}
                </div>

                <div class="cb-result-small">
                    {result_small}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # STOP ABSTAND
        # ----------------------------------------------------

        if market == "Forex CFD":

            distance_text = (
                f"{fmt(pips, 1)} Pips"
            )

            distance_sub = (
                f"{fmt(price_distance, 5)} Kursdifferenz"
            )

        elif market == "Futures":

            distance_text = (
                f"{fmt(ticks, 1)} Ticks"
            )

            distance_sub = (
                f"{fmt(price_distance, 2)} Kursdifferenz"
            )

        else:

            distance_text = (
                fmt(price_distance, 4)
            )

            distance_sub = "Kursdifferenz"


        st.html(
            f"""
            <div class="cb-card">

                <div class="cb-card-left">

                    <div class="cb-card-icon">
                        ◇
                    </div>

                    <div>

                        Stop-Loss-Abstand

                        <div class="cb-card-sub">
                            {distance_sub}
                        </div>

                    </div>

                </div>

                <div class="cb-card-value">
                    {distance_text}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # MAX RISIKO
        # ----------------------------------------------------

        st.html(
            f"""
            <div class="cb-card">

                <div class="cb-card-left">

                    <div class="cb-card-icon">
                        !
                    </div>

                    <div>

                        Maximales Risiko

                        <div class="cb-card-sub">
                            {fmt(risk_percent, 2)} % des Kontos
                        </div>

                    </div>

                </div>

                <div class="cb-card-value">
                    {euro(max_risk)}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # POSITIONSWERT
        # ----------------------------------------------------

        st.html(
            f"""
            <div class="cb-card">

                <div class="cb-card-left">

                    <div class="cb-card-icon">
                        ◉
                    </div>

                    <div>
                        Positionswert
                    </div>

                </div>

                <div class="cb-card-value">
                    {euro(position_value)}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # CHANCE RISIKO
        # ----------------------------------------------------

        if take_profit > 0:

            if direction == "Long":

                reward_distance = (
                    take_profit
                    - entry_price
                )

            else:

                reward_distance = (
                    entry_price
                    - take_profit
                )


            if reward_distance > 0:

                rr = safe_div(
                    reward_distance,
                    price_distance
                )


                potential_profit = (
                    max_risk
                    * rr
                )


                st.html(
                    f"""
                    <div class="cb-card">

                        <div class="cb-card-left">

                            <div class="cb-card-icon">
                                ↗
                            </div>

                            <div>

                                Chance / Risiko

                            </div>

                        </div>

                        <div class="cb-card-value">
                            {fmt(rr, 2)} : 1
                        </div>

                    </div>
                    """
                )


                st.html(
                    f"""
                    <div class="cb-card">

                        <div class="cb-card-left">

                            <div class="cb-card-icon">
                                +
                            </div>

                            <div>

                                Potenzieller Gewinn

                            </div>

                        </div>

                        <div
                            class="cb-card-value"
                            style="color:#91B96A;"
                        >
                            {euro(potential_profit)}
                        </div>

                    </div>
                    """
                )


        # ----------------------------------------------------
        # MARGIN
        # ----------------------------------------------------

        st.html(
            f"""
            <div class="cb-margin">

                <div class="cb-margin-title">
                    Margin & Hebel
                </div>

                <div class="cb-margin-row">

                    <span>
                        Erforderliche Margin
                    </span>

                    <span class="cb-margin-value">
                        {euro(margin)}
                    </span>

                </div>

                <div class="cb-margin-row">

                    <span>
                        Hebel
                    </span>

                    <span class="cb-margin-value">
                        1 : {fmt(leverage, 0)}
                    </span>

                </div>

                <div class="cb-margin-row">

                    <span>
                        Kontogröße
                    </span>

                    <span class="cb-margin-value">
                        {euro(account_size)}
                    </span>

                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # RISIKO-BALKEN
        # ----------------------------------------------------

        risk_bar = min(
            max(risk_percent, 0),
            5
        ) / 5 * 100


        st.html(
            f"""
            <div class="cb-risk">

                <div class="cb-risk-header">

                    <span>
                        Risiko
                    </span>

                    <span class="cb-risk-percent">
                        {fmt(risk_percent, 2)} %
                    </span>

                </div>

                <div class="cb-risk-bar">

                    <div
                        class="cb-risk-fill"
                        style="width:{risk_bar:.1f}%"
                    ></div>

                </div>

                <div class="cb-risk-text">
                    {euro(max_risk)}
                    von {euro(account_size)}
                    maximaler Verlust bei Stop-Loss
                </div>

            </div>
            """
        )


    else:

        st.html(
            f"""
            <div class="cb-warning">

                <strong>
                    Eingabe prüfen
                </strong>

                <br><br>

                {error}

            </div>
            """
        )


# ============================================================
# RISIKOHINWEIS
# ============================================================

st.html(
    """
    <div class="cb-warning">

        <strong>⚠ RISIKOHINWEIS</strong>

        <br>

        Dieser Rechner dient ausschließlich zur
        Orientierung bei der Positions- und
        Risikoplanung.

        <br>

        CFDs sind gehebelte Produkte und können zu
        schnellen Verlusten führen. Prüfe vor jedem
        Trade die aktuellen Produktspezifikationen,
        Kontraktgrößen, Pip-/Tick-Werte,
        Margin-Anforderungen und Handelsbedingungen
        deines Brokers.

        <br>

        Die tatsächlichen Werte können je nach
        Instrument und Broker abweichen.

        <br><br>

        <strong>
            Risk first. Profits second.
        </strong>

    </div>
    """
)


# ============================================================
# FOOTER
# ============================================================

st.html(
    """
    <div class="cb-footer">

        <span class="cb-footer-gold">
            COUNT OR BREAK
        </span>

        &nbsp; · &nbsp;

        Risk Management
        &nbsp; · &nbsp;
        Position Sizing
        &nbsp; · &nbsp;
        Trading Discipline

    </div>
    """
)


# ============================================================
# ENDE
# ============================================================

st.html("</div>")
