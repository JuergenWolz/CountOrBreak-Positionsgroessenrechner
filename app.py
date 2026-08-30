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


calculator_path = find_file([
    "icon_rechner.png",
    "rechner.png",
    "calculator.png",
    "positionsgroessenrechner.png",
    "positionsgrößenrechner.png",
])

logo_path = find_file([
    "countorbreak_logo.png",
    "CountOrBreak_logo.png",
    "logo.png",
    "Logo.png",
])


def image_base64(path):
    if path is None:
        return None

    try:
        return base64.b64encode(path.read_bytes()).decode("utf-8")
    except Exception:
        return None


calculator_image = image_base64(calculator_path)
logo_image = image_base64(logo_path)


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def money(value):
    return (
        f"{value:,.2f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
        + " €"
    )


def number(value, decimals=2):
    return (
        f"{value:,.{decimals}f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def divide(a, b):
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
        --gold: #C9A35A;
        --gold-light: #DDBB72;
        --gold-bright: #E8CB87;
        --gold-dark: #76521A;
        --gold-border: #A77D35;

        --black: #040404;
        --panel: #0B0B0B;
        --panel2: #111111;

        --white: #F0E7D8;
        --muted: #AAA197;

        --green: #88B85F;
        --red: #C76D63;
    }


    /* ========================================================
       APP
       ======================================================== */

    .stApp {
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(201,163,90,0.08),
                transparent 35%
            ),
            #040404;
    }


    .block-container {
        max-width: 1450px;
        padding-top: 1.5rem;
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


    /* ========================================================
       HEADER
       ======================================================== */

    .cb-header {
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 25px;
        margin-bottom: 18px;
    }


    .cb-brand {
        display: flex;
        align-items: center;
        gap: 20px;
    }


    .cb-logo-box {
        width: 78px;
        height: 78px;

        display: flex;
        align-items: center;
        justify-content: center;

        border: 1px solid rgba(167,125,53,0.75);
        border-radius: 17px;

        background:
            linear-gradient(
                145deg,
                #151515,
                #050505
            );

        box-shadow:
            inset 0 0 22px rgba(201,163,90,0.04),
            0 0 16px rgba(201,163,90,0.08);
    }


    .cb-logo-box img {
        width: 60px;
        height: 60px;
        object-fit: contain;
    }


    .cb-title {
        color: var(--gold-light);

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            "Palatino Linotype",
            "Book Antiqua",
            Georgia,
            serif;

        font-size: clamp(30px, 4vw, 51px);
        font-weight: 500;

        letter-spacing: 0.075em;

        text-shadow:
            0 0 9px rgba(201,163,90,0.20);
    }


    .cb-subtitle {
        margin-top: 6px;

        color: #CFC5B5;

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            "Palatino Linotype",
            Georgia,
            serif;

        font-size: 14px;

        letter-spacing: 0.18em;

        text-transform: uppercase;
    }


    .cb-guide {
        padding: 11px 17px;

        border: 1px solid rgba(167,125,53,0.65);
        border-radius: 8px;

        color: var(--gold-light);

        background: rgba(10,10,10,0.85);

        font-family:
            "Baskerville",
            Georgia,
            serif;

        font-size: 14px;
    }


    .cb-top-line {
        width: 100%;
        height: 1px;

        margin: 8px 0 25px;

        background:
            linear-gradient(
                90deg,
                transparent,
                #5C431C,
                #A77D35,
                #DDBB72,
                #A77D35,
                #5C431C,
                transparent
            );

        box-shadow:
            0 0 10px rgba(201,163,90,0.20);
    }


    /* ========================================================
       HAUPTBOX
       ======================================================== */

    .cb-shell {
        width: 100%;

        padding: 27px;

        border:
            1px solid rgba(167,125,53,0.70);

        border-radius: 13px;

        background:
            linear-gradient(
                145deg,
                rgba(15,15,15,0.99),
                rgba(5,5,5,0.99)
            );

        box-shadow:
            inset 0 0 45px rgba(201,163,90,0.025),
            0 18px 50px rgba(0,0,0,0.55);
    }


    /* ========================================================
       SECTIONS
       ======================================================== */

    .cb-section-title {
        color: var(--gold-light);

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            "Palatino Linotype",
            Georgia,
            serif;

        font-size: 22px;
        font-weight: 500;

        letter-spacing: 0.065em;

        margin-bottom: 15px;

        text-shadow:
            0 0 8px rgba(201,163,90,0.13);
    }


    .cb-divider {
        width: 100%;
        height: 1px;

        margin: 20px 0 24px;

        background:
            linear-gradient(
                90deg,
                rgba(167,125,53,0.55),
                rgba(167,125,53,0.06)
            );
    }


    /* ========================================================
       STREAMLIT INPUTS
       ======================================================== */

    div[data-baseweb="select"] > div {
        background: #0D0D0D !important;

        border:
            1px solid rgba(167,125,53,0.55) !important;

        border-radius: 7px !important;
    }


    div[data-baseweb="input"] > div {
        background: #0D0D0D !important;

        border:
            1px solid rgba(167,125,53,0.55) !important;

        border-radius: 7px !important;
    }


    input {
        color: #F0E7D8 !important;
    }


    label {
        color: #CFC5B5 !important;
    }


    /* ========================================================
       LONG / SHORT
       ======================================================== */

    .cb-direction {
        padding: 12px 15px;

        border:
            1px solid rgba(167,125,53,0.42);

        border-radius: 7px;

        background:
            rgba(201,163,90,0.025);

        color: #BEB5A7;

        font-size: 13px;
    }


    /* ========================================================
       ERGEBNIS
       ======================================================== */

    .cb-results-title {
        color: var(--gold-light);

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            "Palatino Linotype",
            Georgia,
            serif;

        font-size: 25px;

        letter-spacing: 0.06em;

        margin-bottom: 18px;
    }


    .cb-main-result {
        width: 100%;

        padding: 25px;

        text-align: center;

        border:
            1px solid rgba(201,163,90,0.85);

        border-radius: 11px;

        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(201,163,90,0.09),
                transparent 65%
            ),
            #080808;

        box-shadow:
            inset 0 0 30px rgba(201,163,90,0.025),
            0 0 20px rgba(201,163,90,0.08);
    }


    .cb-result-label {
        color: #D4C9B8;

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            Georgia,
            serif;

        font-size: 15px;

        letter-spacing: 0.08em;

        text-transform: uppercase;
    }


    .cb-result-value {
        color: var(--green);

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            "Palatino Linotype",
            Georgia,
            serif;

        font-size: clamp(38px, 4vw, 58px);

        font-weight: 500;

        line-height: 1.15;

        margin: 9px 0;

        text-shadow:
            0 0 11px rgba(136,184,95,0.18);
    }


    .cb-result-small {
        color: #9D958A;
        font-size: 13px;
    }


    /* ========================================================
       STAT CARDS
       ======================================================== */

    .cb-stat {
        display: flex;

        align-items: center;
        justify-content: space-between;

        gap: 20px;

        margin-top: 12px;

        padding: 15px 18px;

        min-height: 82px;

        border:
            1px solid rgba(167,125,53,0.45);

        border-radius: 9px;

        background:
            linear-gradient(
                145deg,
                #141414,
                #080808
            );
    }


    .cb-stat-left {
        display: flex;

        align-items: center;

        gap: 13px;

        color: #D1C6B6;

        font-size: 14px;
    }


    .cb-stat-icon {
        width: 38px;
        height: 38px;

        min-width: 38px;

        display: flex;

        align-items: center;
        justify-content: center;

        border:
            1px solid rgba(201,163,90,0.50);

        border-radius: 50%;

        color: var(--gold-light);

        font-size: 17px;
    }


    .cb-stat-sub {
        color: #878078;
        font-size: 12px;
        margin-top: 3px;
    }


    .cb-stat-value {
        color: var(--gold-light);

        font-family:
            "Baskerville",
            Georgia,
            serif;

        font-size: 19px;

        text-align: right;
    }


    /* ========================================================
       MARGIN
       ======================================================== */

    .cb-margin {
        margin-top: 15px;

        padding: 20px;

        border:
            1px solid rgba(167,125,53,0.48);

        border-radius: 9px;

        background: #0B0B0B;
    }


    .cb-margin-title {
        color: var(--gold-light);

        font-family:
            "Baskerville",
            Georgia,
            serif;

        font-size: 19px;

        letter-spacing: 0.055em;

        margin-bottom: 14px;
    }


    .cb-margin-row {
        display: flex;

        align-items: center;
        justify-content: space-between;

        padding: 8px 0;

        border-bottom:
            1px solid rgba(167,125,53,0.10);

        color: #9F978C;

        font-size: 13px;
    }


    .cb-margin-row:last-child {
        border-bottom: none;
    }


    .cb-margin-value {
        color: #DDD2C0;
        font-size: 14px;
    }


    /* ========================================================
       WARNING
       ======================================================== */

    .cb-warning {
        margin-top: 18px;

        padding: 18px 20px;

        border:
            1px solid rgba(167,125,53,0.60);

        border-radius: 9px;

        background:
            linear-gradient(
                145deg,
                rgba(27,23,16,0.96),
                rgba(8,8,8,0.99)
            );

        color: #CFC4B3;

        font-size: 13px;

        line-height: 1.6;
    }


    .cb-warning-title {
        color: var(--gold-light);

        font-family:
            "Baskerville",
            Georgia,
            serif;

        font-size: 17px;

        margin-bottom: 6px;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .cb-footer {
        margin-top: 25px;

        padding-top: 17px;

        border-top:
            1px solid rgba(167,125,53,0.28);

        text-align: center;

        color: #716C64;

        font-family:
            "Baskerville",
            Georgia,
            serif;

        font-size: 12px;

        letter-spacing: 0.12em;
    }


    .cb-footer-gold {
        color: var(--gold);
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 850px) {

        .block-container {
            padding-left: 0.65rem;
            padding-right: 0.65rem;
        }

        .cb-shell {
            padding: 17px;
        }

        .cb-header {
            flex-direction: column;
            align-items: flex-start;
        }

        .cb-logo-box {
            width: 65px;
            height: 65px;
        }

        .cb-logo-box img {
            width: 50px;
            height: 50px;
        }

        .cb-title {
            font-size: 30px;
        }

        .cb-subtitle {
            font-size: 12px;
            letter-spacing: 0.10em;
        }

        .cb-main-result {
            padding: 21px 15px;
        }

        .cb-result-value {
            font-size: 40px;
        }

        .cb-stat {
            padding: 13px;
        }

        .cb-stat-value {
            font-size: 16px;
        }
    }

    </style>
    """
)


# ============================================================
# HEADER
# ============================================================

if calculator_image:

    calculator_html = f"""
    <img
        src="data:image/png;base64,{calculator_image}"
        alt="Positionsgrößenrechner"
    >
    """

else:

    calculator_html = """
    <span style="
        color:#DDBB72;
        font-size:38px;
    ">
        ♢
    </span>
    """


st.html(
    f"""
    <div class="cb-header">

        <div class="cb-brand">

            <div class="cb-logo-box">
                {calculator_html}
            </div>

            <div>

                <div class="cb-title">
                    COUNT OR BREAK
                </div>

                <div class="cb-subtitle">
                    Positionsgrößenrechner
                </div>

            </div>

        </div>

        <div class="cb-guide">
            ⓘ &nbsp; Risiko zuerst. Gewinne danach.
        </div>

    </div>

    <div class="cb-top-line"></div>
    """
)


# ============================================================
# HAUPTBOX
# ============================================================

st.html('<div class="cb-shell">')

left, right = st.columns(
    [1.04, 1],
    gap="large",
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
        <div class="cb-section-title">
            1. Markt
        </div>
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
        ],
    )


    default_instrument = ""

    if market == "Forex CFD":
        default_instrument = "EUR/USD"

    elif market == "Index CFD":
        default_instrument = "NAS100"

    elif market == "Krypto CFD":
        default_instrument = "BTC/USD"

    elif market == "Rohstoff CFD":
        default_instrument = "XAU/USD"


    instrument = st.text_input(
        "Instrument",
        value=default_instrument,
        placeholder="z. B. EUR/USD, NAS100, XAU/USD",
    )


    if market != "Futures":

        st.caption(
            "Pepperstone CFD · Bitte aktuelle Produktspezifikationen "
            "für das gewählte Instrument prüfen."
        )


    st.html('<div class="cb-divider"></div>')


    # --------------------------------------------------------
    # RICHTUNG
    # --------------------------------------------------------

    st.html(
        """
        <div class="cb-section-title">
            2. Trade-Richtung
        </div>
        """
    )


    direction = st.radio(
        "Trade-Richtung",
        ["Long", "Short"],
        horizontal=True,
        label_visibility="collapsed",
    )


    if direction == "Long":

        st.html(
            """
            <div class="cb-direction">
                ↗ Long – der Stop-Loss liegt unterhalb des Einstiegs.
            </div>
            """
        )

    else:

        st.html(
            """
            <div class="cb-direction">
                ↘ Short – der Stop-Loss liegt oberhalb des Einstiegs.
            </div>
            """
        )


    st.html('<div class="cb-divider"></div>')


    # --------------------------------------------------------
    # KONTO & RISIKO
    # --------------------------------------------------------

    st.html(
        """
        <div class="cb-section-title">
            3. Konto & Risiko
        </div>
        """
    )


    account_col, risk_col = st.columns(2)


    with account_col:

        account_size = st.number_input(
            "Kontogröße (€)",
            min_value=0.01,
            value=10000.00,
            step=100.00,
            format="%.2f",
        )


    with risk_col:

        risk_percent = st.number_input(
            "Risiko pro Trade (%)",
            min_value=0.01,
            max_value=100.0,
            value=1.00,
            step=0.10,
            format="%.2f",
        )


    max_risk = account_size * risk_percent / 100


    st.number_input(
        "Maximales Risiko (€)",
        min_value=0.01,
        value=float(max_risk),
        step=10.00,
        format="%.2f",
        disabled=True,
    )


    st.html('<div class="cb-divider"></div>')


    # --------------------------------------------------------
    # TRADE DATEN
    # --------------------------------------------------------

    st.html(
        """
        <div class="cb-section-title">
            4. Trade-Daten
        </div>
        """
    )


    price_col_1, price_col_2 = st.columns(2)


    if market == "Forex CFD":

        default_entry = 1.17000
        price_step = 0.00001
        price_format = "%.5f"

    else:

        default_entry = 100.0
        price_step = 0.10
        price_format = "%.4f"


    with price_col_1:

        entry_price = st.number_input(
            "Einstiegskurs",
            min_value=0.00000001,
            value=default_entry,
            step=price_step,
            format=price_format,
        )


    if direction == "Long":

        if market == "Forex CFD":
            default_stop = 1.16500
        else:
            default_stop = max(entry_price * 0.98, 0.00000001)

    else:

        if market == "Forex CFD":
            default_stop = 1.17500
        else:
            default_stop = entry_price * 1.02


    with price_col_2:

        stop_loss = st.number_input(
            "Stop-Loss",
            min_value=0.00000001,
            value=float(default_stop),
            step=price_step,
            format=price_format,
        )


    take_profit = st.number_input(
        "Take-Profit (optional)",
        min_value=0.0,
        value=0.0,
        step=price_step,
        format=price_format,
        help="0 = kein Take-Profit.",
    )


    price_distance = abs(entry_price - stop_loss)

    stop_percent = divide(
        price_distance,
        entry_price,
    ) * 100


    st.html('<div class="cb-divider"></div>')


    # --------------------------------------------------------
    # INSTRUMENT DETAILS
    # --------------------------------------------------------

    st.html(
        """
        <div class="cb-section-title">
            5. Instrument Details
        </div>
        """
    )


    # ========================================================
    # FOREX
    # ========================================================

    if market == "Forex CFD":

        col1, col2 = st.columns(2)


        with col1:

            lot_size = st.number_input(
                "Lot-Größe",
                min_value=1.0,
                value=100000.0,
                step=1000.0,
                format="%.0f",
            )


        with col2:

            pip_size = st.number_input(
                "Pip-Größe",
                min_value=0.00000001,
                value=0.00010,
                step=0.00001,
                format="%.5f",
            )


        col3, col4 = st.columns(2)


        with col3:

            pip_value = st.number_input(
                "Pip-Wert pro Lot (€)",
                min_value=0.0001,
                value=10.00,
                step=0.10,
                format="%.2f",
            )


        with col4:

            leverage = st.number_input(
                "Hebel",
                min_value=1.0,
                value=30.0,
                step=1.0,
                format="%.0f",
            )


        pips = divide(
            price_distance,
            pip_size,
        )


        risk_per_lot = pips * pip_value


        position_lots = divide(
            max_risk,
            risk_per_lot,
        )


        position_units = position_lots * lot_size


        position_value = (
            position_units
            * entry_price
        )


        margin_required = divide(
            position_value,
            leverage,
        )


    # ========================================================
    # FUTURES
    # ========================================================

    elif market == "Futures":

        col1, col2 = st.columns(2)


        with col1:

            tick_size = st.number_input(
                "Tick-Größe",
                min_value=0.00000001,
                value=0.25,
                step=0.01,
                format="%.4f",
            )


        with col2:

            tick_value = st.number_input(
                "Tick-Wert (€)",
                min_value=0.0001,
                value=12.50,
                step=0.50,
                format="%.2f",
            )


        leverage = st.number_input(
            "Hebel",
            min_value=1.0,
            value=20.0,
            step=1.0,
            format="%.0f",
        )


        ticks = divide(
            price_distance,
            tick_size,
        )


        risk_per_contract = (
            ticks * tick_value
        )


        position_contracts = divide(
            max_risk,
            risk_per_contract,
        )


        position_units = position_contracts


        position_value = (
            position_contracts
            * entry_price
        )


        margin_required = divide(
            position_value,
            leverage,
        )


    # ========================================================
    # ANDERE CFDs
    # ========================================================

    else:

        col1, col2 = st.columns(2)


        with col1:

            value_per_unit = st.number_input(
                "Wert pro 1,00 Preisbewegung (€)",
                min_value=0.0001,
                value=1.00,
                step=0.10,
                format="%.4f",
            )


        with col2:

            contract_size = st.number_input(
                "Kontrakt-/Einheitsgröße",
                min_value=0.0001,
                value=1.0,
                step=1.0,
                format="%.4f",
            )


        leverage = st.number_input(
            "Hebel",
            min_value=1.0,
            value=5.0,
            step=1.0,
            format="%.0f",
        )


        risk_per_unit = (
            price_distance
            * value_per_unit
        )


        position_units = divide(
            max_risk,
            risk_per_unit,
        )


        position_value = (
            position_units
            * contract_size
            * entry_price
        )


        margin_required = divide(
            position_value,
            leverage,
        )


    # ========================================================
    # VALIDIERUNG
    # ========================================================

    valid = True
    error_message = ""


    if entry_price <= 0:

        valid = False
        error_message = (
            "Der Einstiegskurs muss größer als 0 sein."
        )


    elif stop_loss <= 0:

        valid = False
        error_message = (
            "Der Stop-Loss muss größer als 0 sein."
        )


    elif price_distance <= 0:

        valid = False
        error_message = (
            "Einstieg und Stop-Loss dürfen nicht identisch sein."
        )


    elif direction == "Long" and stop_loss >= entry_price:

        valid = False
        error_message = (
            "Bei Long muss der Stop-Loss unterhalb "
            "des Einstiegs liegen."
        )


    elif direction == "Short" and stop_loss <= entry_price:

        valid = False
        error_message = (
            "Bei Short muss der Stop-Loss oberhalb "
            "des Einstiegs liegen."
        )


# ============================================================
# RECHTE SEITE
# ============================================================

with right:

    st.html(
        """
        <div class="cb-results-title">
            Ergebnisse
        </div>
        """
    )


    if valid:

        # ----------------------------------------------------
        # POSITIONSGRÖSSE
        # ----------------------------------------------------

        if market == "Forex CFD":

            position_display = (
                f"{number(position_lots, 2)} Lots"
            )

            position_sub = (
                f"= {number(position_units, 0)} Einheiten"
            )

        elif market == "Futures":

            position_display = (
                f"{number(position_units, 2)} Kontrakte"
            )

            position_sub = (
                "auf Basis des angegebenen Tick-Werts"
            )

        else:

            position_display = (
                f"{number(position_units, 2)} Einheiten"
            )

            position_sub = (
                f"Positionswert: {money(position_value)}"
            )


        st.html(
            f"""
            <div class="cb-main-result">

                <div class="cb-result-label">
                    Empfohlene Positionsgröße
                </div>

                <div class="cb-result-value">
                    {position_display}
                </div>

                <div class="cb-result-small">
                    {position_sub}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # RISIKO
        # ----------------------------------------------------

        st.html(
            f"""
            <div class="cb-stat">

                <div class="cb-stat-left">

                    <div class="cb-stat-icon">
                        !
                    </div>

                    <div>

                        Max. Verlust bei Stop-Loss

                        <div class="cb-stat-sub">
                            {number(risk_percent, 2)} % des Kontos
                        </div>

                    </div>

                </div>

                <div class="cb-stat-value">
                    {money(max_risk)}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # STOP DISTANZ
        # ----------------------------------------------------

        if market == "Forex CFD":

            stop_display = (
                f"{number(pips, 1)} Pips"
            )

        elif market == "Futures":

            stop_display = (
                f"{number(ticks, 1)} Ticks"
            )

        else:

            stop_display = (
                f"{number(price_distance, 4)}"
            )


        st.html(
            f"""
            <div class="cb-stat">

                <div class="cb-stat-left">

                    <div class="cb-stat-icon">
                        ◎
                    </div>

                    <div>

                        Stop-Loss-Abstand

                        <div class="cb-stat-sub">
                            {number(stop_percent, 2)} % vom Einstieg
                        </div>

                    </div>

                </div>

                <div class="cb-stat-value">
                    {stop_display}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # POSITIONSWERT
        # ----------------------------------------------------

        st.html(
            f"""
            <div class="cb-stat">

                <div class="cb-stat-left">

                    <div class="cb-stat-icon">
                        ◉
                    </div>

                    <div>
                        Positionswert
                    </div>

                </div>

                <div class="cb-stat-value">
                    {money(position_value)}
                </div>

            </div>
            """
        )


        # ----------------------------------------------------
        # CHANCE / RISIKO
        # ----------------------------------------------------

        rr_ratio = None
        potential_profit = None


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

                rr_ratio = divide(
                    reward_distance,
                    price_distance,
                )

                potential_profit = (
                    max_risk
                    * rr_ratio
                )


        if rr_ratio is not None:

            st.html(
                f"""
                <div class="cb-stat">

                    <div class="cb-stat-left">

                        <div class="cb-stat-icon">
                            ⚖
                        </div>

                        <div>
                            Chance / Risiko
                        </div>

                    </div>

                    <div class="cb-stat-value">
                        {number(rr_ratio, 2)} : 1
                    </div>

                </div>
                """
            )


            st.html(
                f"""
                <div class="cb-stat">

                    <div class="cb-stat-left">

                        <div class="cb-stat-icon">
                            ↗
                        </div>

                        <div>

                            Potenzieller Gewinn

                            <div class="cb-stat-sub">
                                bei Take-Profit
                            </div>

                        </div>

                    </div>

                    <div
                        class="cb-stat-value"
                        style="color:#88B85F;"
                    >
                        {money(potential_profit)}
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
                        {money(margin_required)}
                    </span>

                </div>

                <div class="cb-margin-row">

                    <span>
                        Hebel
                    </span>

                    <span class="cb-margin-value">
                        1 : {number(leverage, 0)}
                    </span>

                </div>

                <div class="cb-margin-row">

                    <span>
                        Kontogröße
                    </span>

                    <span class="cb-margin-value">
                        {money(account_size)}
                    </span>

                </div>

                <div class="cb-margin-row">

                    <span>
                        Max. Risiko
                    </span>

                    <span class="cb-margin-value">
                        {money(max_risk)}
                    </span>

                </div>

            </div>
            """
        )


    else:

        st.html(
            f"""
            <div class="cb-warning">

                <div class="cb-warning-title">
                    Eingabe prüfen
                </div>

                {error_message}

            </div>
            """
        )


# ============================================================
# RISIKOHINWEIS
# ============================================================

st.html(
    """
    <div class="cb-warning">

        <div class="cb-warning-title">
            ⚠ Wichtiger Hinweis
        </div>

        Dieser Rechner dient zur Orientierung bei der
        Positions- und Risikoplanung.

        <br><br>

        Bei CFDs können Verluste schnell entstehen.
        Prüfe vor jedem Trade die aktuellen
        Produktspezifikationen, Kontraktgrößen,
        Pip-/Tick-Werte und Margin-Anforderungen
        des konkreten Instruments.

        <br><br>

        Die tatsächlichen Konditionen können je nach
        Instrument und Broker variieren.

        <br><br>

        <strong>Risk first. Profits second.</strong>

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

        &nbsp; • &nbsp;

        Trading Journal
        &nbsp; • &nbsp;
        Risk Management
        &nbsp; • &nbsp;
        Performance

    </div>
    """
)


# ============================================================
# ENDE
# ============================================================

st.html("</div>")
