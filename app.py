import streamlit as st
from pathlib import Path
import base64
import math


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
# DATEIPFADE
# ============================================================

BASE_DIR = Path(__file__).resolve().parent


def find_file(possible_names):
    for filename in possible_names:
        file_path = BASE_DIR / filename
        if file_path.exists() and file_path.is_file():
            return file_path
    return None


LOGO_PATH = find_file([
    "logo.png",
    "Logo.png",
    "countorbreak_logo.png",
    "CountOrBreak_logo.png",
    "countorbreak.png",
    "CountOrBreak.png",
    "cb_logo.png",
    "CB_Logo.png",
    "logo.jpg",
    "Logo.jpg",
    "logo.webp",
])


CALCULATOR_PATH = find_file([
    "rechner.png",
    "Rechner.png",
    "calculator.png",
    "Calculator.png",
    "icon_rechner.png",
    "Icon_Rechner.png",
    "positionsgroessenrechner.png",
    "Positionsgroessenrechner.png",
    "positionsgrößenrechner.png",
    "Positionsgrößenrechner.png",
    "positionsgroessenrechner_icon.png",
    "calculator.jpg",
    "rechner.jpg",
    "rechner.webp",
])


# ============================================================
# BILD IN BASE64
# ============================================================

def image_to_base64(path):
    if path is None:
        return None

    try:
        return base64.b64encode(path.read_bytes()).decode("utf-8")
    except Exception:
        return None


logo_base64 = image_to_base64(LOGO_PATH)
calculator_base64 = image_to_base64(CALCULATOR_PATH)


# ============================================================
# HTML RENDERER
#
# Wichtig:
# Wir benutzen st.html(), damit HTML niemals von Markdown
# als Codeblock interpretiert werden kann.
# ============================================================

def render_html(html):
    html = html.strip()

    if hasattr(st, "html"):
        st.html(html)
    else:
        st.markdown(
            html,
            unsafe_allow_html=True,
        )


# ============================================================
# ZAHLENFORMAT
# ============================================================

def format_number(value, decimals=2):
    try:
        number = float(value)

        formatted = f"{number:,.{decimals}f}"

        formatted = (
            formatted
            .replace(",", "X")
            .replace(".", ",")
            .replace("X", ".")
        )

        return formatted

    except Exception:
        return "0,00"


def safe_division(a, b):
    if b == 0:
        return 0.0

    return a / b


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
<style>

@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Montserrat:wght@400;500;600;700&display=swap');


/* ==========================================================
   GRUNDLAYOUT
   ========================================================== */

.stApp {
    background:
        radial-gradient(
            ellipse at 50% 0%,
            rgba(205, 157, 45, 0.075),
            transparent 38%
        ),
        radial-gradient(
            ellipse at 50% 100%,
            rgba(205, 157, 45, 0.035),
            transparent 48%
        ),
        #020202;

    color: #F2F2F2;

    font-family:
        "Inter",
        Arial,
        sans-serif;
}


.block-container {
    max-width: 1320px;

    padding-top: 22px;
    padding-bottom: 45px;
    padding-left: 24px;
    padding-right: 24px;
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


/* ==========================================================
   HEADER
   ========================================================== */

.cb-header {
    width: 100%;

    min-height: 145px;

    display: flex;

    align-items: center;

    justify-content: center;

    gap: 42px;

    margin-bottom: 15px;
}


.cb-logo {
    width: 195px;

    height: 135px;

    object-fit: contain;

    display: block;

    filter:
        drop-shadow(
            0 0 9px rgba(225, 184, 79, 0.18)
        );
}


.cb-calculator {
    width: 112px;

    height: 112px;

    display: flex;

    align-items: center;

    justify-content: center;

    border:
        2px solid rgba(225, 184, 79, 0.90);

    border-radius: 15px;

    background:
        radial-gradient(
            circle,
            rgba(225, 184, 79, 0.14),
            rgba(0, 0, 0, 0.25) 72%
        );

    box-shadow:
        0 0 8px rgba(225, 184, 79, 0.34),
        0 0 25px rgba(225, 184, 79, 0.11),
        inset 0 0 25px rgba(225, 184, 79, 0.05);
}


.cb-calculator img {
    width: 88px;

    height: 88px;

    object-fit: contain;

    display: block;

    filter:
        drop-shadow(
            0 0 8px rgba(255, 214, 107, 0.40)
        );
}


.cb-calculator-fallback {
    color: #E1B84F;

    font-size: 52px;

    line-height: 1;

    text-shadow:
        0 0 12px rgba(255, 211, 101, 0.30);
}


/* ==========================================================
   TITEL
   ========================================================== */

.cb-title-frame {
    position: relative;

    width: 100%;

    min-height: 105px;

    display: flex;

    flex-direction: column;

    align-items: center;

    justify-content: center;

    box-sizing: border-box;

    border:
        2px solid rgba(201, 149, 37, 0.82);

    border-radius: 13px;

    background:
        linear-gradient(
            180deg,
            rgba(20, 20, 20, 0.96),
            rgba(5, 5, 5, 0.98)
        );

    box-shadow:
        0 0 8px rgba(214, 162, 44, 0.22),
        inset 0 0 30px rgba(213, 164, 55, 0.035);

    margin-bottom: 24px;
}


.cb-title {
    color: #E1B84F;

    font-family:
        "Montserrat",
        Arial,
        sans-serif;

    font-size:
        clamp(28px, 3.2vw, 43px);

    font-weight: 600;

    letter-spacing: 0.105em;

    line-height: 1.1;

    text-align: center;

    text-transform: uppercase;

    text-shadow:
        0 0 8px rgba(237, 185, 64, 0.24),
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

    text-align: center;
}


.cb-title-line-left,
.cb-title-line-right {
    position: absolute;

    top: 50%;

    width: 105px;

    height: 1px;

    transform: translateY(-50%);

    box-shadow:
        0 0 7px rgba(255, 209, 92, 0.35);
}


.cb-title-line-left {
    left: 42px;

    background:
        linear-gradient(
            90deg,
            transparent,
            #E1B84F
        );
}


.cb-title-line-right {
    right: 42px;

    background:
        linear-gradient(
            90deg,
            #E1B84F,
            transparent
        );
}


/* ==========================================================
   PANELS
   ========================================================== */

.cb-panel {
    box-sizing: border-box;

    width: 100%;

    min-height: 680px;

    padding: 26px;

    border:
        1px solid rgba(126, 126, 126, 0.48);

    border-radius: 14px;

    background:
        linear-gradient(
            145deg,
            rgba(18, 18, 18, 0.98),
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

    margin-bottom: 24px;

    color: #E1B84F;

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

    color: #E1B84F;

    font-size: 26px;

    text-shadow:
        0 0 9px rgba(255, 205, 91, 0.30);
}


/* ==========================================================
   STREAMLIT INPUTS
   ========================================================== */

div[data-baseweb="input"] > div {
    background:
        linear-gradient(
            180deg,
            #111111,
            #080808
        ) !important;

    border:
        1px solid rgba(164, 125, 51, 0.58) !important;

    border-radius: 7px !important;

    min-height: 52px !important;
}


div[data-baseweb="select"] > div {
    background:
        linear-gradient(
            180deg,
            #111111,
            #080808
        ) !important;

    border:
        1px solid rgba(164, 125, 51, 0.58) !important;

    border-radius: 7px !important;

    min-height: 52px !important;
}


input {
    color: #F2F2F2 !important;

    font-family:
        "Inter",
        Arial,
        sans-serif !important;

    font-size: 16px !important;
}


label {
    color: #E6E6E6 !important;

    font-family:
        "Inter",
        Arial,
        sans-serif !important;

    font-size: 15px !important;
}


[data-baseweb="select"] * {
    color: #F2F2F2 !important;
}


/* ==========================================================
   RADIO BUTTONS
   ========================================================== */

.stRadio > div {
    width: 100%;
}


.stRadio [role="radiogroup"] {
    width: 100%;

    display: flex;

    gap: 8px;
}


.stRadio [role="radio"] {
    flex: 1;

    min-height: 51px;

    display: flex;

    align-items: center;

    justify-content: center;

    box-sizing: border-box;

    border:
        1px solid rgba(115, 115, 115, 0.58);

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


.stRadio [role="radio"]:hover {
    border-color:
        rgba(225, 184, 79, 0.70);
}


.stRadio [role="radio"]:has(input:checked) {
    border-color:
        rgba(218, 170, 56, 0.95);

    background:
        linear-gradient(
            180deg,
            rgba(125, 88, 23, 0.68),
            rgba(51, 36, 11, 0.78)
        );

    box-shadow:
        0 0 10px rgba(218, 170, 56, 0.14);
}


/* ==========================================================
   ERGEBNIS
   ========================================================== */

.cb-result {
    width: 100%;

    text-align: center;

    padding-top: 8px;

    padding-bottom: 4px;
}


.cb-result-label {
    display: flex;

    align-items: center;

    justify-content: center;

    gap: 18px;

    color: #E1B84F;

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

    flex-shrink: 0;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(225, 184, 79, 0.90)
        );
}


.cb-result-label::after {
    background:
        linear-gradient(
            90deg,
            rgba(225, 184, 79, 0.90),
            transparent
        );
}


.cb-result-number {
    margin-top: 24px;

    color: #FFE7A0;

    font-family:
        "Montserrat",
        Arial,
        sans-serif;

    font-size:
        clamp(50px, 5vw, 76px);

    font-weight: 700;

    line-height: 1;

    letter-spacing: -0.025em;

    text-shadow:
        0 0 7px rgba(255, 216, 111, 0.60),
        0 0 20px rgba(255, 203, 73, 0.34),
        0 0 42px rgba(255, 203, 73, 0.17);
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

    margin-top: 21px;

    margin-bottom: 9px;

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


/* ==========================================================
   METRIKEN
   ========================================================== */

.cb-metric {
    width: 100%;

    min-height: 47px;

    display: flex;

    align-items: center;

    justify-content: space-between;

    box-sizing: border-box;

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
    color: #E1B84F;

    font-size: 18px;

    font-weight: 500;

    text-align: right;
}


.cb-metric-unit {
    color: #E7E7E7;

    font-size: 14px;

    margin-left: 4px;
}


/* ==========================================================
   MARGIN
   ========================================================== */

.cb-margin-title {
    display: flex;

    align-items: center;

    gap: 10px;

    margin-top: 24px;

    margin-bottom: 10px;

    color: #E1B84F;

    font-family:
        "Montserrat",
        Arial,
        sans-serif;

    font-size: 20px;

    font-weight: 500;

    letter-spacing: 0.025em;

    text-transform: uppercase;
}


/* ==========================================================
   RISIKOÜBERSICHT
   ========================================================== */

.cb-risk-panel {
    width: 100%;

    min-height: 195px;

    box-sizing: border-box;

    margin-top: 20px;

    padding: 25px 28px;

    overflow: hidden;

    border:
        1px solid rgba(126, 126, 126, 0.48);

    border-radius: 14px;

    background:
        linear-gradient(
            145deg,
            rgba(16, 16, 16, 0.98),
            rgba(5, 5, 5, 0.98)
        );

    box-shadow:
        inset 0 0 35px rgba(255, 255, 255, 0.012);
}


.cb-risk-title {
    display: flex;

    align-items: center;

    gap: 12px;

    color: #E1B84F;

    font-family:
        "Montserrat",
        Arial,
        sans-serif;

    font-size: 20px;

    font-weight: 500;

    letter-spacing: 0.025em;

    text-transform: uppercase;
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

    position: relative;

    display: flex;

    align-items: center;

    justify-content: center;

    border-radius: 50%;
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

    color: #E1B84F;

    font-family:
        "Montserrat",
        Arial,
        sans-serif;

    font-size: 24px;

    font-weight: 500;

    text-align: center;
}


.cb-risk-money {
    color: #E1B84F;

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

    box-sizing: border-box;

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


/* ==========================================================
   RISIKOHINWEIS
   ========================================================== */

.cb-warning-panel {
    width: 100%;

    box-sizing: border-box;

    margin-top: 20px;

    padding: 22px 28px;

    overflow: hidden;

    border:
        1px solid rgba(170, 122, 22, 0.80);

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

    align-items: flex-start;

    gap: 22px;
}


.cb-warning-icon {
    color: #E1B84F;

    font-size: 42px;

    line-height: 1;

    text-shadow:
        0 0 10px rgba(232, 190, 78, 0.22);
}


.cb-warning-title {
    margin-bottom: 8px;

    color: #E1B84F;

    font-family:
        "Montserrat",
        Arial,
        sans-serif;

    font-size: 19px;

    font-weight: 500;

    letter-spacing: 0.035em;

    text-transform: uppercase;
}


.cb-warning-text {
    max-width: 1050px;

    color: #E5E5E5;

    font-family:
        "Inter",
        Arial,
        sans-serif;

    font-size: 13px;

    line-height: 1.55;
}


/* ==========================================================
   FEHLERMELDUNG
   ========================================================== */

.cb-error {
    margin-top: 15px;

    padding: 13px 16px;

    border:
        1px solid rgba(190, 80, 60, 0.65);

    border-radius: 8px;

    background:
        rgba(70, 20, 15, 0.25);

    color: #F0B0A0;

    font-size: 14px;
}


/* ==========================================================
   FOOTER
   ========================================================== */

.cb-footer {
    margin-top: 18px;

    color: #C99525;

    font-family:
        "Montserrat",
        Arial,
        sans-serif;

    font-size: 11px;

    letter-spacing: 0.30em;

    text-align: center;

    text-transform: uppercase;
}


/* ==========================================================
   MOBILE
   ========================================================== */

@media (max-width: 850px) {

    .block-container {
        padding-left: 12px;
        padding-right: 12px;
        padding-top: 14px;
    }

    .cb-header {
        min-height: 105px;
        gap: 18px;
    }

    .cb-logo {
        width: 150px;
        height: 100px;
    }

    .cb-calculator {
        width: 78px;
        height: 78px;
    }

    .cb-calculator img {
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
""",
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

if logo_base64:

    logo_html = (
        '<img class="cb-logo" '
        'src="data:image/png;base64,'
        + logo_base64
        + '" '
        'alt="Count Or Break">'
    )

else:

    logo_html = (
        '<div style="'
        'color:#E1B84F;'
        'font-family:Montserrat,Arial,sans-serif;'
        'font-size:26px;'
        'font-weight:600;'
        'letter-spacing:3px;'
        'text-align:center;'
        '">'
        'COUNT OR BREAK'
        '</div>'
    )


if calculator_base64:

    calculator_html = (
        '<img '
        'src="data:image/png;base64,'
        + calculator_base64
        + '" '
        'alt="Positionsgrößenrechner">'
    )

else:

    calculator_html = (
        '<div class="cb-calculator-fallback">'
        '🧮'
        '</div>'
    )


render_html(
    '<div class="cb-header">'
    '<div>'
    + logo_html
    + '</div>'
    '<div class="cb-calculator">'
    + calculator_html
    + '</div>'
    '</div>'
)


# ============================================================
# TITEL
# ============================================================

render_html(
    '<div class="cb-title-frame">'
    '<div class="cb-title-line-left"></div>'
    '<div class="cb-title">'
    'POSITIONSGRÖSSENRECHNER'
    '</div>'
    '<div class="cb-subtitle">'
    'Risk first. Profits second.'
    '</div>'
    '<div class="cb-title-line-right"></div>'
    '</div>'
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

    render_html(
        '<div class="cb-panel">'
        '<div class="cb-panel-title">'
        '<div class="cb-panel-icon">⚖</div>'
        '<div>TRADE-EINGABEN</div>'
        '</div>'
        '</div>'
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
            "XAU/USD",
            "NAS100",
            "US30",
            "SPX500",
            "GER40",
            "BTC/USD",
            "ETH/USD",
        ],
    )


    # --------------------------------------------------------
    # RICHTUNG
    # --------------------------------------------------------

    direction = st.radio(
        "Richtung",
        [
            "↗ LONG",
            "↓ SHORT",
        ],
        horizontal=True,
    )


    is_long = direction.startswith("↗")


    # --------------------------------------------------------
    # KONTOGRÖSSE
    # --------------------------------------------------------

    account_col, currency_col = st.columns(
        [3, 1]
    )


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
            [
                "EUR",
                "USD",
                "GBP",
            ],
        )


    # --------------------------------------------------------
    # RISIKO
    # --------------------------------------------------------

    risk_col, risk_unit_col = st.columns(
        [3, 1]
    )


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

        render_html(
            '<div style="'
            'margin-top:29px;'
            'height:52px;'
            'box-sizing:border-box;'
            'border:1px solid rgba(164,125,51,0.58);'
            'border-radius:7px;'
            'display:flex;'
            'align-items:center;'
            'justify-content:center;'
            'background:#090909;'
            'color:#EEEEEE;'
            'font-size:15px;'
            '">'
            '%'
            '</div>'
        )


    # --------------------------------------------------------
    # DEFAULT-WERTE
    # --------------------------------------------------------

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


    # --------------------------------------------------------
    # EINSTIEG
    # --------------------------------------------------------

    entry_price = st.number_input(
        "Einstiegskurs",
        min_value=0.00001,
        value=float(entry_default),
        step=float(price_step),
        format=f"%.{price_decimals}f",
    )


    # --------------------------------------------------------
    # STOP LOSS
    # --------------------------------------------------------

    stop_loss = st.number_input(
        "Stop-Loss Kurs",
        min_value=0.00001,
        value=float(stop_default),
        step=float(price_step),
        format=f"%.{price_decimals}f",
    )


    # --------------------------------------------------------
    # TAKE PROFIT
    # --------------------------------------------------------

    take_profit = st.number_input(
        "Take-Profit Kurs (optional)",
        min_value=0.0,
        value=0.0,
        step=float(price_step),
        format=f"%.{price_decimals}f",
    )


    # --------------------------------------------------------
    # HEBEL
    # --------------------------------------------------------

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

max_risk = (
    account_size
    * risk_percent
    / 100.0
)


price_distance = abs(
    entry_price - stop_loss
)


valid_trade = True

error_message = ""


if price_distance <= 0:

    valid_trade = False

    error_message = (
        "Einstiegskurs und Stop-Loss Kurs "
        "dürfen nicht identisch sein."
    )


if is_long and stop_loss >= entry_price:

    valid_trade = False

    error_message = (
        "Bei einem LONG-Trade muss der "
        "Stop-Loss unter dem Einstiegskurs liegen."
    )


if not is_long and stop_loss <= entry_price:

    valid_trade = False

    error_message = (
        "Bei einem SHORT-Trade muss der "
        "Stop-Loss über dem Einstiegskurs liegen."
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

        pip_value_per_lot = 6.70

    elif instrument == "USD/CAD":

        pip_value_per_lot = 6.80

    else:

        pip_value_per_lot = 10.00


    stop_pips = safe_division(
        price_distance,
        pip_size
    )


    risk_per_lot = (
        stop_pips
        * pip_value_per_lot
    )


    lots = safe_division(
        max_risk,
        risk_per_lot
    )


    units = (
        lots
        * 100000
    )


    position_value = (
        units
        * entry_price
    )


    margin = safe_division(
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


    lots = safe_division(
        max_risk,
        risk_per_lot
    )


    units = (
        lots
        * contract_size
    )


    position_value = (
        lots
        * contract_size
        * entry_price
    )


    margin = safe_division(
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


    lots = safe_division(
        max_risk,
        risk_per_lot
    )


    units = lots


    position_value = (
        lots
        * entry_price
    )


    margin = safe_division(
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


    units = safe_division(
        max_risk,
        risk_per_unit
    )


    lots = units


    position_value = (
        units
        * entry_price
    )


    margin = safe_division(
        position_value,
        leverage
    )


    stop_pips = price_distance


    pip_value_total = units


# ============================================================
# FALLBACK
# ============================================================

else:

    lots = safe_division(
        max_risk,
        price_distance
    )


    units = lots


    position_value = (
        units
        * entry_price
    )


    margin = safe_division(
        position_value,
        leverage
    )


    stop_pips = price_distance


    pip_value_total = lots


# ============================================================
# RECHTE SPALTE
# ============================================================

with right_col:

    render_html(
        '<div class="cb-panel">'
        '<div class="cb-panel-title">'
        '<div class="cb-panel-icon">◎</div>'
        '<div>ERGEBNIS</div>'
        '</div>'
        '<div class="cb-result">'
        '<div class="cb-result-label">'
        'EMPFOHLENE POSITION'
        '</div>'
        + (
            '<div class="cb-result-number">'
            + format_number(lots, 2)
            + ' LOTS'
            + '</div>'
            + '<div class="cb-result-units">'
            + '= '
            + format_number(units, 0)
            + ' EINHEITEN'
            + '</div>'
            if valid_trade
            else
            '<div class="cb-error">'
            + error_message
            + '</div>'
        )
        + '</div>'
        + '<div class="cb-gold-divider"></div>'
        + (
            '<div class="cb-metric">'
            '<span>Max. Verlust</span>'
            '<span class="cb-metric-value">'
            + format_number(max_risk, 2)
            + ' <span class="cb-metric-unit">'
            + currency
            + '</span></span>'
            '</div>'
            +
            '<div class="cb-metric">'
            '<span>Stop-Abstand</span>'
            '<span class="cb-metric-value">'
            + (
                format_number(stop_pips, 1)
                if instrument in forex_pairs
                else format_number(stop_pips, 2)
            )
            + ' <span class="cb-metric-unit">'
            + (
                'Pips'
                if instrument in forex_pairs
                else 'Punkte'
            )
            + '</span></span>'
            '</div>'
            +
            '<div class="cb-metric">'
            '<span>Positionswert</span>'
            '<span class="cb-metric-value">'
            + format_number(position_value, 0)
            + ' <span class="cb-metric-unit">'
            + currency
            + '</span></span>'
            '</div>'
            +
            '<div class="cb-metric">'
            '<span>Pip-Wert</span>'
            '<span class="cb-metric-value">'
            + format_number(pip_value_total, 2)
            + ' <span class="cb-metric-unit">'
            + currency
            + '</span></span>'
            '</div>'
            +
            '<div class="cb-metric">'
            '<span>Risikoprozent</span>'
            '<span class="cb-metric-value">'
            + format_number(risk_percent, 2)
            + ' <span class="cb-metric-unit">%</span>'
            '</span>'
            '</div>'
            +
            '<div class="cb-margin-title">'
            '<span>⚖</span>'
            '<span>MARGIN & HEBEL</span>'
            '</div>'
            +
            '<div class="cb-metric">'
            '<span>Erforderliche Margin</span>'
            '<span class="cb-metric-value">'
            + format_number(margin, 2)
            + ' <span class="cb-metric-unit">'
            + currency
            + '</span></span>'
            '</div>'
            +
            '<div class="cb-metric">'
            '<span>Verwendeter Hebel</span>'
            '<span class="cb-metric-value">'
            '1 : '
            + format_number(leverage, 0)
            + '</span>'
            '</div>'
            +
            '<div class="cb-metric">'
            '<span>Freie Margin (geschätzt)</span>'
            '<span class="cb-metric-value">'
            + format_number(
                max(account_size - margin, 0),
                2
            )
            + ' <span class="cb-metric-unit">'
            + currency
            + '</span></span>'
            '</div>'
            if valid_trade
            else ''
        )
        + '</div>'
    )


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

risk_percentage_for_bar = min(
    max(
        risk_percent,
        0.0
    ),
    5.0
)


circle_progress = (
    risk_percentage_for_bar
    / 5.0
    * 360.0
)


active_blocks = int(
    round(
        risk_percentage_for_bar
        / 5.0
        * 30
    )
)


risk_blocks_html = ""


for index in range(30):

    if index < active_blocks:

        risk_blocks_html += (
            '<div class="cb-risk-block active"></div>'
        )

    else:

        risk_blocks_html += (
            '<div class="cb-risk-block"></div>'
        )


# ============================================================
# RISIKOÜBERSICHT RENDERN
# ============================================================

render_html(
    '<div class="cb-risk-panel">'
    '<div class="cb-risk-title">'
    '<span style="font-size:28px;">♢</span>'
    '<span>RISIKOÜBERSICHT</span>'
    '</div>'
    '<div class="cb-risk-content">'
    '<div class="cb-risk-circle" style="'
    'background:conic-gradient('
    '#E1B84F 0deg '
    + str(circle_progress)
    + 'deg, '
    '#343434 '
    + str(circle_progress)
    + 'deg 360deg'
    ');'
    '">'
    '<div class="cb-risk-circle-text">'
    + format_number(risk_percent, 2)
    + ' %'
    + '</div>'
    '</div>'
    '<div>'
    '<div class="cb-risk-money">'
    + format_number(max_risk, 2)
    + ' '
    + currency
    + '</div>'
    '<div class="cb-risk-account">'
    'von '
    + format_number(account_size, 2)
    + ' '
    + currency
    + '</div>'
    '<div class="cb-risk-blocks">'
    + risk_blocks_html
    + '</div>'
    '</div>'
    '</div>'
    '</div>'
)


# ============================================================
# RISIKOHINWEIS
# ============================================================

render_html(
    '<div class="cb-warning-panel">'
    '<div class="cb-warning-content">'
    '<div class="cb-warning-icon">△</div>'
    '<div>'
    '<div class="cb-warning-title">'
    'RISIKOHINWEIS'
    '</div>'
    '<div class="cb-warning-text">'
    'CFDs sind komplexe Instrumente und bergen aufgrund '
    'der Hebelwirkung ein hohes Risiko, schnell Geld zu '
    'verlieren. 74–89 % der Kleinanlegerkonten verlieren '
    'Geld beim CFD-Handel mit diesem Anbieter.'
    '<br><br>'
    'Überlegen Sie, ob Sie verstehen, wie CFDs funktionieren '
    'und ob Sie es sich leisten können, das hohe Risiko '
    'einzugehen, Ihr Geld zu verlieren.'
    '</div>'
    '</div>'
    '</div>'
    '</div>'
)


# ============================================================
# FOOTER
# ============================================================

render_html(
    '<div class="cb-footer">'
    'COUNT OR BREAK'
    '&nbsp;&nbsp;·&nbsp;&nbsp;'
    'PLAN. EXECUTE. SUCCEED.'
    '</div>'
)
