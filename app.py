import streamlit as st
from pathlib import Path
from textwrap import dedent
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

BASE_DIR = Path(__file__).parent


def find_asset(names):
    for name in names:
        path = BASE_DIR / name
        if path.exists():
            return path
    return None


LOGO_PATH = find_asset([
    "logo.png",
    "Logo.png",
    "countorbreak_logo.png",
    "CountOrBreak_logo.png",
    "countorbreak.png",
    "CountOrBreak.png",
    "cb_logo.png",
    "CB_Logo.png",
])

CALCULATOR_PATH = find_asset([
    "rechner.png",
    "Rechner.png",
    "calculator.png",
    "Calculator.png",
    "icon_rechner.png",
    "positionsgroessenrechner.png",
    "positionsgrößenrechner.png",
    "positionsgroessenrechner_icon.png",
])


def image_base64(path):
    if path is None:
        return None

    try:
        return base64.b64encode(path.read_bytes()).decode("utf-8")
    except Exception:
        return None


logo_b64 = image_base64(LOGO_PATH)
calculator_b64 = image_base64(CALCULATOR_PATH)


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def number_de(value, decimals=2):
    try:
        return (
            f"{float(value):,.{decimals}f}"
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )
    except Exception:
        return "0,00"


def safe_div(a, b):
    if b == 0:
        return 0
    return a / b


# ============================================================
# DESIGN / CSS
# ============================================================

st.markdown(
    dedent(
        """
        <style>

        @import url(
            'https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap'
        );

        :root {
            --cb-black: #020202;
            --cb-panel: #090909;
            --cb-panel-light: #111111;
            --cb-gold-dark: #79551B;
            --cb-gold: #C99525;
            --cb-gold-light: #E1B84F;
            --cb-gold-bright: #FFD66B;
            --cb-gold-white: #FFE7A0;
            --cb-text: #F1F1F1;
            --cb-muted: #999999;
        }


        /* ====================================================
           GLOBAL
           ==================================================== */

        .stApp {
            background:
                radial-gradient(
                    ellipse at 50% 0%,
                    rgba(210, 160, 50, 0.075),
                    transparent 35%
                ),
                radial-gradient(
                    ellipse at 50% 100%,
                    rgba(210, 160, 50, 0.035),
                    transparent 45%
                ),
                #020202;

            color: var(--cb-text);

            font-family:
                "Inter",
                Arial,
                sans-serif;
        }


        .block-container {
            max-width: 1320px;

            padding-top: 25px;
            padding-left: 25px;
            padding-right: 25px;
            padding-bottom: 50px;
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


        /* ====================================================
           HEADER
           ==================================================== */

        .cb-header {
            width: 100%;

            min-height: 145px;

            display: flex;
            align-items: center;
            justify-content: center;

            gap: 40px;

            margin-bottom: 18px;
        }


        .cb-logo {
            width: 190px;
            height: 135px;

            object-fit: contain;

            filter:
                drop-shadow(
                    0 0 8px rgba(225, 184, 79, 0.18)
                );
        }


        .cb-calculator-icon {
            width: 112px;
            height: 112px;

            display: flex;
            align-items: center;
            justify-content: center;

            border: 2px solid rgba(225, 184, 79, 0.85);

            border-radius: 15px;

            background:
                radial-gradient(
                    circle,
                    rgba(225, 184, 79, 0.13),
                    rgba(0, 0, 0, 0.25) 70%
                );

            box-shadow:
                0 0 8px rgba(225, 184, 79, 0.30),
                0 0 25px rgba(225, 184, 79, 0.10),
                inset 0 0 25px rgba(225, 184, 79, 0.05);
        }


        .cb-calculator-icon img {
            width: 88px;
            height: 88px;

            object-fit: contain;

            filter:
                drop-shadow(
                    0 0 8px rgba(255, 214, 107, 0.35)
                );
        }


        /* ====================================================
           TITEL
           ==================================================== */

        .cb-title-frame {
            position: relative;

            width: 100%;
            min-height: 105px;

            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;

            border: 2px solid rgba(201, 149, 37, 0.80);

            border-radius: 13px;

            background:
                linear-gradient(
                    180deg,
                    rgba(21, 21, 21, 0.90),
                    rgba(5, 5, 5, 0.97)
                );

            box-shadow:
                0 0 8px rgba(214, 162, 44, 0.20),
                inset 0 0 30px rgba(213, 164, 55, 0.035);

            margin-bottom: 25px;
        }


        .cb-title-line-left,
        .cb-title-line-right {
            position: absolute;

            top: 50%;

            width: 105px;
            height: 1px;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    var(--cb-gold-light)
                );

            box-shadow:
                0 0 6px rgba(255, 209, 92, 0.35);
        }


        .cb-title-line-left {
            left: 42px;
        }


        .cb-title-line-right {
            right: 42px;

            background:
                linear-gradient(
                    90deg,
                    var(--cb-gold-light),
                    transparent
                );
        }


        .cb-title {
            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: clamp(27px, 3.1vw, 43px);

            font-weight: 600;

            letter-spacing: 0.105em;

            line-height: 1.1;

            text-transform: uppercase;

            text-align: center;

            text-shadow:
                0 0 8px rgba(237, 185, 64, 0.22),
                0 0 22px rgba(237, 185, 64, 0.10);
        }


        .cb-subtitle {
            margin-top: 7px;

            color: #E8D08A;

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 20px;

            font-weight: 400;

            letter-spacing: 0.025em;
        }


        /* ====================================================
           HAUPTPANELS
           ==================================================== */

        .cb-panel {
            position: relative;

            height: 100%;

            min-height: 680px;

            padding: 26px;

            border: 1px solid rgba(126, 126, 126, 0.45);

            border-radius: 14px;

            background:
                linear-gradient(
                    145deg,
                    rgba(18, 18, 18, 0.97),
                    rgba(5, 5, 5, 0.99)
                );

            box-shadow:
                inset 0 0 35px rgba(255, 255, 255, 0.015),
                0 12px 35px rgba(0, 0, 0, 0.35);
        }


        .cb-panel-title {
            display: flex;

            align-items: center;

            gap: 12px;

            margin-bottom: 25px;

            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 21px;

            font-weight: 500;

            letter-spacing: 0.025em;

            text-transform: uppercase;
        }


        .cb-panel-icon {
            width: 32px;
            height: 32px;

            display: flex;
            align-items: center;
            justify-content: center;

            color: var(--cb-gold-light);

            font-size: 25px;

            text-shadow:
                0 0 9px rgba(255, 205, 91, 0.28);
        }


        /* ====================================================
           INPUTS
           ==================================================== */

        label {
            color: #E5E5E5 !important;

            font-family:
                "Inter",
                Arial,
                sans-serif !important;

            font-size: 15px !important;

            font-weight: 400 !important;
        }


        div[data-baseweb="input"] > div {
            background:
                linear-gradient(
                    180deg,
                    #111111,
                    #080808
                ) !important;

            border:
                1px solid rgba(164, 125, 51, 0.55) !important;

            border-radius: 7px !important;

            min-height: 54px !important;
        }


        div[data-baseweb="select"] > div {
            background:
                linear-gradient(
                    180deg,
                    #111111,
                    #080808
                ) !important;

            border:
                1px solid rgba(164, 125, 51, 0.55) !important;

            border-radius: 7px !important;

            min-height: 54px !important;
        }


        input {
            color: #F1F1F1 !important;

            font-family:
                "Inter",
                Arial,
                sans-serif !important;

            font-size: 16px !important;
        }


        [data-baseweb="select"] * {
            color: #F1F1F1 !important;
        }


        /* ====================================================
           RADIO
           ==================================================== */

        .stRadio > div {
            gap: 8px;
        }


        .stRadio [role="radiogroup"] {
            display: flex;

            width: 100%;

            gap: 8px;
        }


        .stRadio [role="radio"] {
            flex: 1;

            min-height: 51px;

            display: flex;
            align-items: center;
            justify-content: center;

            border:
                1px solid rgba(115, 115, 115, 0.55);

            border-radius: 7px;

            background:
                linear-gradient(
                    180deg,
                    #111111,
                    #080808
                );

            color: #EEEEEE;

            transition:
                all 0.2s ease;
        }


        .stRadio [role="radio"]:has(input:checked) {
            border-color:
                rgba(218, 170, 56, 0.90);

            background:
                linear-gradient(
                    180deg,
                    rgba(125, 88, 23, 0.65),
                    rgba(51, 36, 11, 0.75)
                );

            box-shadow:
                0 0 10px rgba(218, 170, 56, 0.12);
        }


        /* ====================================================
           ERGEBNIS
           ==================================================== */

        .cb-result-top {
            text-align: center;

            margin-top: 24px;
            margin-bottom: 18px;
        }


        .cb-result-label {
            display: flex;

            align-items: center;
            justify-content: center;

            gap: 18px;

            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 22px;

            font-weight: 500;

            letter-spacing: 0.035em;

            text-transform: uppercase;
        }


        .cb-result-label::before,
        .cb-result-label::after {
            content: "";

            width: 82px;
            height: 1px;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    rgba(225, 184, 79, 0.85)
                );
        }


        .cb-result-label::after {
            background:
                linear-gradient(
                    90deg,
                    rgba(225, 184, 79, 0.85),
                    transparent
                );
        }


        .cb-result-number {
            margin-top: 23px;

            color: var(--cb-gold-white);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: clamp(52px, 5vw, 77px);

            font-weight: 700;

            line-height: 1;

            letter-spacing: -0.025em;

            text-shadow:
                0 0 7px rgba(255, 216, 111, 0.55),
                0 0 20px rgba(255, 203, 73, 0.32),
                0 0 42px rgba(255, 203, 73, 0.16);
        }


        .cb-result-units {
            margin-top: 14px;

            color: #EEEEEE;

            font-family:
                "Inter",
                Arial,
                sans-serif;

            font-size: 25px;

            font-weight: 400;
        }


        .cb-gold-divider {
            width: 100%;

            height: 1px;

            margin: 20px 0 12px;

            background:
                linear-gradient(
                    90deg,
                    transparent,
                    rgba(201, 149, 37, 0.10),
                    rgba(235, 194, 89, 0.95),
                    rgba(201, 149, 37, 0.10),
                    transparent
                );

            box-shadow:
                0 0 8px rgba(225, 184, 79, 0.25);
        }


        /* ====================================================
           METRIKEN
           ==================================================== */

        .cb-metric {
            display: flex;

            justify-content: space-between;

            align-items: center;

            min-height: 47px;

            border-bottom:
                1px solid rgba(130, 130, 130, 0.19);

            color: #E6E6E6;

            font-family:
                "Inter",
                Arial,
                sans-serif;

            font-size: 16px;
        }


        .cb-metric-value {
            color: var(--cb-gold-light);

            font-size: 18px;

            font-weight: 500;
        }


        .cb-metric-unit {
            color: #E7E7E7;

            font-size: 14px;

            margin-left: 4px;
        }


        /* ====================================================
           MARGIN
           ==================================================== */

        .cb-margin-title {
            display: flex;

            align-items: center;

            gap: 10px;

            margin-top: 24px;
            margin-bottom: 10px;

            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 20px;

            font-weight: 500;

            text-transform: uppercase;

            letter-spacing: 0.025em;
        }


        /* ====================================================
           RISIKOÜBERSICHT
           ==================================================== */

        .cb-risk-panel {
            position: relative;

            overflow: hidden;

            margin-top: 20px;

            min-height: 195px;

            padding: 25px 28px;

            border:
                1px solid rgba(126, 126, 126, 0.48);

            border-radius: 14px;

            background:
                linear-gradient(
                    145deg,
                    rgba(16, 16, 16, 0.98),
                    rgba(5, 5, 5, 0.98)
                );
        }


        .cb-risk-title {
            display: flex;

            align-items: center;

            gap: 12px;

            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 20px;

            font-weight: 500;

            text-transform: uppercase;

            letter-spacing: 0.025em;
        }


        .cb-risk-content {
            display: flex;

            align-items: center;

            gap: 35px;

            margin-top: 15px;
        }


        .cb-risk-circle {
            width: 126px;
            height: 126px;

            flex: 0 0 126px;

            display: flex;
            align-items: center;
            justify-content: center;

            border-radius: 50%;

            position: relative;
        }


        .cb-risk-circle::after {
            content: "";

            position: absolute;

            inset: 11px;

            border-radius: 50%;

            background: #070707;
        }


        .cb-risk-circle-text {
            position: relative;

            z-index: 2;

            text-align: center;

            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 24px;

            font-weight: 500;
        }


        .cb-risk-money {
            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 24px;

            font-weight: 500;
        }


        .cb-risk-account {
            margin-top: 3px;

            color: #F0F0F0;

            font-size: 16px;
        }


        .cb-risk-blocks {
            display: flex;

            gap: 3px;

            margin-top: 18px;

            max-width: 530px;

            overflow: hidden;
        }


        .cb-risk-block {
            width: 11px;
            height: 25px;

            flex: 0 0 11px;

            border:
                1px solid rgba(110, 110, 110, 0.35);

            background:
                linear-gradient(
                    180deg,
                    #333333,
                    #191919
                );
        }


        .cb-risk-block.active {
            border-color:
                rgba(224, 182, 70, 0.95);

            background:
                linear-gradient(
                    180deg,
                    #E1B84F,
                    #8A611B
                );

            box-shadow:
                0 0 5px rgba(224, 182, 70, 0.24);
        }


        /* ====================================================
           RISIKOHINWEIS
           ==================================================== */

        .cb-warning-panel {
            position: relative;

            overflow: hidden;

            margin-top: 20px;

            padding: 22px 28px;

            border:
                1px solid rgba(170, 122, 22, 0.78);

            border-radius: 14px;

            background:
                linear-gradient(
                    145deg,
                    rgba(16, 16, 16, 0.97),
                    rgba(5, 5, 5, 0.99)
                );

            box-shadow:
                inset 0 0 30px rgba(200, 150, 40, 0.018);
        }


        .cb-warning-content {
            display: flex;

            gap: 22px;

            align-items: flex-start;
        }


        .cb-warning-icon {
            color: var(--cb-gold-light);

            font-size: 42px;

            line-height: 1;

            text-shadow:
                0 0 10px rgba(232, 190, 78, 0.22);
        }


        .cb-warning-title {
            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 19px;

            font-weight: 500;

            text-transform: uppercase;

            letter-spacing: 0.035em;

            margin-bottom: 8px;
        }


        .cb-warning-text {
            color: #E5E5E5;

            font-family:
                "Inter",
                Arial,
                sans-serif;

            font-size: 13px;

            line-height: 1.55;

            max-width: 1050px;
        }


        /* ====================================================
           BUTTON
           ==================================================== */

        .stButton > button {
            width: 100%;

            min-height: 50px;

            border:
                1px solid rgba(201, 149, 37, 0.65);

            border-radius: 7px;

            background:
                linear-gradient(
                    180deg,
                    #18130A,
                    #0B0A08
                );

            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-weight: 500;

            transition:
                all 0.2s ease;
        }


        .stButton > button:hover {
            border-color:
                var(--cb-gold-bright);

            box-shadow:
                0 0 13px rgba(221, 175, 64, 0.20);

            transform:
                translateY(-1px);
        }


        /* ====================================================
           FOOTER
           ==================================================== */

        .cb-footer {
            margin-top: 17px;

            text-align: center;

            color: var(--cb-gold-light);

            font-family:
                "Montserrat",
                Arial,
                sans-serif;

            font-size: 11px;

            letter-spacing: 0.30em;

            text-transform: uppercase;
        }


        /* ====================================================
           MOBILE
           ==================================================== */

        @media (max-width: 850px) {

            .block-container {
                padding-left: 12px;
                padding-right: 12px;
                padding-top: 15px;
            }

            .cb-header {
                min-height: 105px;
                gap: 18px;
            }

            .cb-logo {
                width: 150px;
                height: 100px;
            }

            .cb-calculator-icon {
                width: 78px;
                height: 78px;
            }

            .cb-calculator-icon img {
                width: 60px;
                height: 60px;
            }

            .cb-title-frame {
                min-height: 90px;
            }

            .cb-title {
                font-size: 23px;
                letter-spacing: 0.055em;
            }

            .cb-subtitle {
                font-size: 15px;
            }

            .cb-title-line-left,
            .cb-title-line-right {
                display: none;
            }

            .cb-panel {
                min-height: 0;
                padding: 19px;
            }

            .cb-result-number {
                font-size: 48px;
            }

            .cb-result-units {
                font-size: 20px;
            }

            .cb-risk-content {
                gap: 20px;
            }

            .cb-risk-circle {
                width: 105px;
                height: 105px;
                flex-basis: 105px;
            }

            .cb-risk-circle::after {
                inset: 9px;
            }

            .cb-risk-money {
                font-size: 19px;
            }

            .cb-risk-block {
                width: 7px;
                flex-basis: 7px;
            }

            .cb-warning-content {
                gap: 14px;
            }

            .cb-warning-icon {
                font-size: 31px;
            }

            .cb-warning-text {
                font-size: 12px;
            }

            .cb-footer {
                letter-spacing: 0.15em;
            }
        }

        </style>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

if logo_b64:
    logo_html = f"""
    <img
        class="cb-logo"
        src="data:image/png;base64,{logo_b64}"
        alt="Count Or Break"
    >
    """
else:
    logo_html = """
    <div
        style="
            color:#E1B84F;
            font-family:Montserrat,Arial,sans-serif;
            font-size:28px;
            font-weight:600;
            letter-spacing:3px;
        "
    >
        COUNT OR BREAK
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
    <div
        style="
            color:#E1B84F;
            font-size:50px;
        "
    >
        🧮
    </div>
    """


st.markdown(
    dedent(
        f"""
        <div class="cb-header">

            <div>
                {logo_html}
            </div>

            <div class="cb-calculator-icon">
                {calculator_html}
            </div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# TITEL
# ============================================================

st.markdown(
    dedent(
        """
        <div class="cb-title-frame">

            <div class="cb-title-line-left"></div>

            <div class="cb-title">
                Positionsgrößenrechner
            </div>

            <div class="cb-subtitle">
                Risk first. Profits second.
            </div>

            <div class="cb-title-line-right"></div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# HAUPTSPALTEN
# ============================================================

left_col, right_col = st.columns(
    [0.95, 1.35],
    gap="medium"
)


# ============================================================
# LINKE SPALTE
# ============================================================

with left_col:

    st.markdown(
        dedent(
            """
            <div class="cb-panel">

                <div class="cb-panel-title">

                    <div class="cb-panel-icon">
                        ⚖
                    </div>

                    <div>
                        Trade-Eingaben
                    </div>

                </div>

            </div>
            """
        ),
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
            "XAU/USD",
            "NAS100",
            "US30",
            "SPX500",
            "GER40",
            "BTC/USD",
            "ETH/USD",
        ]
    )


    direction = st.radio(
        "Richtung",
        [
            "↗ LONG",
            "↓ SHORT",
        ],
        horizontal=True,
    )


    is_long = direction.startswith("↗")


    account_col, currency_col = st.columns([3, 1])


    with account_col:

        account_size = st.number_input(
            "Kontogröße",
            min_value=1.0,
            value=10000.0,
            step=100.0,
            format="%.2f",
        )


    with currency_col:

        currency = st.selectbox(
            "Währung",
            ["EUR", "USD", "GBP"]
        )


    risk_col, risk_unit_col = st.columns([3, 1])


    with risk_col:

        risk_percent = st.number_input(
            "Risiko pro Trade",
            min_value=0.01,
            max_value=100.0,
            value=1.00,
            step=0.10,
            format="%.2f",
        )


    with risk_unit_col:

        st.markdown(
            dedent(
                """
                <div
                    style="
                        margin-top:29px;
                        height:54px;
                        border:1px solid rgba(164,125,51,0.55);
                        border-radius:7px;
                        display:flex;
                        align-items:center;
                        justify-content:center;
                        background:#090909;
                        color:#EEEEEE;
                        font-size:15px;
                    "
                >
                    %
                </div>
                """
            ),
            unsafe_allow_html=True,
        )


    # ========================================================
    # STANDARDWERTE
    # ========================================================

    if instrument in [
        "EUR/USD",
        "GBP/USD",
        "AUD/USD",
        "USD/CAD",
        "USD/CHF",
    ]:

        entry_default = 1.17000
        stop_default = 1.16500
        price_decimals = 5
        price_step = 0.00001

    elif instrument == "USD/JPY":

        entry_default = 150.000
        stop_default = 149.500
        price_decimals = 3
        price_step = 0.001

    elif instrument == "XAU/USD":

        entry_default = 3400.00
        stop_default = 3390.00
        price_decimals = 2
        price_step = 0.10

    elif instrument in [
        "NAS100",
        "US30",
        "SPX500",
        "GER40",
    ]:

        entry_default = 23000.00
        stop_default = 22900.00
        price_decimals = 2
        price_step = 1.0

    elif instrument == "BTC/USD":

        entry_default = 100000.00
        stop_default = 99000.00
        price_decimals = 2
        price_step = 10.0

    else:

        entry_default = 2500.00
        stop_default = 2450.00
        price_decimals = 2
        price_step = 1.0


    entry_price = st.number_input(
        "Einstiegskurs",
        min_value=0.00001,
        value=float(entry_default),
        step=float(price_step),
        format=f"%.{price_decimals}f",
    )


    stop_loss = st.number_input(
        "Stop-Loss Kurs",
        min_value=0.00001,
        value=float(stop_default),
        step=float(price_step),
        format=f"%.{price_decimals}f",
    )


    take_profit = st.number_input(
        "Take-Profit Kurs (optional)",
        min_value=0.0,
        value=0.0,
        step=float(price_step),
        format=f"%.{price_decimals}f",
    )


    leverage = st.number_input(
        "Verwendeter Hebel",
        min_value=1.0,
        max_value=1000.0,
        value=30.0,
        step=1.0,
        format="%.0f",
    )


# ============================================================
# BERECHNUNG
# ============================================================

max_risk = account_size * risk_percent / 100

price_distance = abs(entry_price - stop_loss)

valid_trade = True
error_message = ""


if price_distance <= 0:

    valid_trade = False

    error_message = (
        "Einstieg und Stop-Loss müssen unterschiedlich sein."
    )


if is_long and stop_loss >= entry_price:

    valid_trade = False

    error_message = (
        "Bei LONG muss der Stop-Loss unter dem Einstieg liegen."
    )


if not is_long and stop_loss <= entry_price:

    valid_trade = False

    error_message = (
        "Bei SHORT muss der Stop-Loss über dem Einstieg liegen."
    )


# ============================================================
# FOREX
# ============================================================

forex_pairs = [
    "EUR/USD",
    "GBP/USD",
    "USD/JPY",
    "AUD/USD",
    "USD/CAD",
    "USD/CHF",
]


if instrument in forex_pairs:

    pip_size = (
        0.01
        if instrument == "USD/JPY"
        else 0.0001
    )


    if instrument == "USD/JPY":

        pip_value_per_lot = 6.7

    elif instrument == "USD/CAD":

        pip_value_per_lot = 6.8

    elif instrument == "USD/CHF":

        pip_value_per_lot = 10.0

    else:

        pip_value_per_lot = 10.0


    stop_pips = safe_div(
        price_distance,
        pip_size
    )


    risk_per_lot = (
        stop_pips
        * pip_value_per_lot
    )


    lots = safe_div(
        max_risk,
        risk_per_lot
    )


    units = lots * 100000


    position_value = (
        units
        * entry_price
    )


    margin = safe_div(
        position_value,
        leverage
    )


    pip_value_total = (
        lots
        * pip_value_per_lot
    )


# ============================================================
# GOLD
# ============================================================

elif instrument == "XAU/USD":

    contract_size = 100.0

    risk_per_lot = (
        price_distance
        * contract_size
    )


    lots = safe_div(
        max_risk,
        risk_per_lot
    )


    units = lots * contract_size


    position_value = (
        lots
        * contract_size
        * entry_price
    )


    margin = safe_div(
        position_value,
        leverage
    )


    stop_pips = price_distance

    pip_value_total = (
        lots
        * contract_size
    )


# ============================================================
# INDIZES
# ============================================================

elif instrument in [
    "NAS100",
    "US30",
    "SPX500",
    "GER40",
]:

    value_per_point = 1.0

    risk_per_lot = (
        price_distance
        * value_per_point
    )


    lots = safe_div(
        max_risk,
        risk_per_lot
    )


    units = lots


    position_value = (
        lots
        * entry_price
    )


    margin = safe_div(
        position_value,
        leverage
    )


    stop_pips = price_distance

    pip_value_total = (
        lots
        * value_per_point
    )


# ============================================================
# KRYPTO
# ============================================================

elif instrument in [
    "BTC/USD",
    "ETH/USD",
]:

    risk_per_unit = price_distance

    units = safe_div(
        max_risk,
        risk_per_unit
    )


    lots = units


    position_value = (
        units
        * entry_price
    )


    margin = safe_div(
        position_value,
        leverage
    )


    stop_pips = price_distance

    pip_value_total = units


# ============================================================
# FALLBACK
# ============================================================

else:

    lots = safe_div(
        max_risk,
        price_distance
    )


    units = lots


    position_value = (
        units
        * entry_price
    )


    margin = safe_div(
        position_value,
        leverage
    )


    stop_pips = price_distance

    pip_value_total = lots


# ============================================================
# RECHTE SPALTE
# ============================================================

with right_col:

    st.markdown(
        dedent(
            """
            <div class="cb-panel">

                <div class="cb-panel-title">

                    <div class="cb-panel-icon">
                        ◎
                    </div>

                    <div>
                        Ergebnis
                    </div>

                </div>
            """
        ),
        unsafe_allow_html=True,
    )


    if not valid_trade:

        st.error(error_message)

    else:

        # ----------------------------------------------------
        # POSITION
        # ----------------------------------------------------

        st.markdown(
            dedent(
                f"""
                <div class="cb-result-top">

                    <div class="cb-result-label">
                        Empfohlene Position
                    </div>

                    <div class="cb-result-number">
                        {number_de(lots, 2)} LOTS
                    </div>

                    <div class="cb-result-units">
                        = {number_de(units, 0)} EINHEITEN
                    </div>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        st.markdown(
            dedent(
                """
                <div class="cb-gold-divider"></div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # MAX VERLUST
        # ----------------------------------------------------

        st.markdown(
            dedent(
                f"""
                <div class="cb-metric">

                    <span>
                        Max. Verlust
                    </span>

                    <span class="cb-metric-value">
                        {number_de(max_risk, 2)}
                        <span class="cb-metric-unit">
                            {currency}
                        </span>
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # STOP
        # ----------------------------------------------------

        if instrument in forex_pairs:

            stop_text = number_de(
                stop_pips,
                1
            )

            stop_unit = "Pips"

        else:

            stop_text = number_de(
                stop_pips,
                2
            )

            stop_unit = "Punkte"


        st.markdown(
            dedent(
                f"""
                <div class="cb-metric">

                    <span>
                        Stop-Abstand
                    </span>

                    <span class="cb-metric-value">
                        {stop_text}
                        <span class="cb-metric-unit">
                            {stop_unit}
                        </span>
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # POSITIONSWERT
        # ----------------------------------------------------

        st.markdown(
            dedent(
                f"""
                <div class="cb-metric">

                    <span>
                        Positionswert
                    </span>

                    <span class="cb-metric-value">
                        {number_de(position_value, 0)}
                        <span class="cb-metric-unit">
                            {currency}
                        </span>
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # PIP WERT
        # ----------------------------------------------------

        st.markdown(
            dedent(
                f"""
                <div class="cb-metric">

                    <span>
                        Pip-Wert
                    </span>

                    <span class="cb-metric-value">
                        {number_de(pip_value_total, 2)}
                        <span class="cb-metric-unit">
                            {currency}
                        </span>
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # RISIKO
        # ----------------------------------------------------

        st.markdown(
            dedent(
                f"""
                <div class="cb-metric">

                    <span>
                        Risikoprozent
                    </span>

                    <span class="cb-metric-value">
                        {number_de(risk_percent, 2)}
                        <span class="cb-metric-unit">
                            %
                        </span>
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # MARGIN
        # ----------------------------------------------------

        st.markdown(
            dedent(
                """
                <div class="cb-margin-title">

                    <span>
                        ⚖
                    </span>

                    <span>
                        Margin & Hebel
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # MARGIN
        # ----------------------------------------------------

        st.markdown(
            dedent(
                f"""
                <div class="cb-metric">

                    <span>
                        Erforderliche Margin
                    </span>

                    <span class="cb-metric-value">
                        {number_de(margin, 2)}
                        <span class="cb-metric-unit">
                            {currency}
                        </span>
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # HEBEL
        # ----------------------------------------------------

        st.markdown(
            dedent(
                f"""
                <div class="cb-metric">

                    <span>
                        Verwendeter Hebel
                    </span>

                    <span class="cb-metric-value">
                        1 : {number_de(leverage, 0)}
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # FREIE MARGIN
        # ----------------------------------------------------

        free_margin = max(
            account_size - margin,
            0
        )


        st.markdown(
            dedent(
                f"""
                <div class="cb-metric">

                    <span>
                        Freie Margin (geschätzt)
                    </span>

                    <span class="cb-metric-value">
                        {number_de(free_margin, 2)}
                        <span class="cb-metric-unit">
                            {currency}
                        </span>
                    </span>

                </div>
                """
            ),
            unsafe_allow_html=True,
        )


    st.markdown(
        dedent(
            """
            </div>
            """
        ),
        unsafe_allow_html=True,
    )


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

risk_blocks = 30

active_blocks = int(
    min(
        max(
            risk_percent / 5,
            0
        ),
        1
    )
    * risk_blocks
)


blocks_html = ""

for i in range(risk_blocks):

    if i < active_blocks:

        blocks_html += (
            '<div class="cb-risk-block active"></div>'
        )

    else:

        blocks_html += (
            '<div class="cb-risk-block"></div>'
        )


circle_progress = min(
    max(risk_percent / 5 * 100, 1),
    100
)


circle_degrees = circle_progress * 3.6


# ============================================================
# RISIKO PANEL
# ============================================================

st.markdown(
    dedent(
        f"""
        <div class="cb-risk-panel">

            <div class="cb-risk-title">

                <span style="font-size:28px;">
                    ♢
                </span>

                <span>
                    Risikoübersicht
                </span>

            </div>


            <div class="cb-risk-content">

                <div
                    class="cb-risk-circle"
                    style="
                        background:
                        conic-gradient(
                            #E1B84F
                            0deg
                            {circle_degrees}deg,
                            #343434
                            {circle_degrees}deg
                            360deg
                        );
                    "
                >

                    <div class="cb-risk-circle-text">
                        {number_de(risk_percent, 2)} %
                    </div>

                </div>


                <div class="cb-risk-details">

                    <div class="cb-risk-money">
                        {number_de(max_risk, 2)}
                        {currency}
                    </div>

                    <div class="cb-risk-account">
                        von {number_de(account_size, 2)}
                        {currency}
                    </div>

                    <div class="cb-risk-blocks">
                        {blocks_html}
                    </div>

                </div>

            </div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# RISIKOHINWEIS
# ============================================================

st.markdown(
    dedent(
        """
        <div class="cb-warning-panel">

            <div class="cb-warning-content">

                <div class="cb-warning-icon">
                    △
                </div>

                <div>

                    <div class="cb-warning-title">
                        Risikohinweis
                    </div>

                    <div class="cb-warning-text">

                        CFDs sind komplexe Instrumente und bergen
                        aufgrund der Hebelwirkung ein hohes Risiko,
                        schnell Geld zu verlieren. 74–89 % der
                        Kleinanlegerkonten verlieren Geld beim
                        CFD-Handel mit diesem Anbieter.

                        <br><br>

                        Überlegen Sie, ob Sie verstehen, wie CFDs
                        funktionieren und ob Sie es sich leisten
                        können, das hohe Risiko einzugehen, Ihr Geld
                        zu verlieren.

                    </div>

                </div>

            </div>

        </div>
        """
    ),
    unsafe_allow_html=True,
)


# ============================================================
# FOOTER
# ============================================================

st.markdown(
    dedent(
        """
        <div class="cb-footer">
            COUNT OR BREAK
            &nbsp; · &nbsp;
            PLAN. EXECUTE. SUCCEED.
        </div>
        """
    ),
    unsafe_allow_html=True,
)
