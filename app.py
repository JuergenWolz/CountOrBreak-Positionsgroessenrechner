import streamlit as st
import math
import os


# ============================================================
# COUNT OR BREAK
# POSITIONSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# KONFIGURATION
# ============================================================

GOLD = "#D9A928"
GOLD_LIGHT = "#F5D36A"
GOLD_BRIGHT = "#FFE08A"
GOLD_DARK = "#8E6915"

BLACK = "#000000"
BLACK_SOFT = "#080808"
PANEL = "#0D0D0D"
PANEL_2 = "#111111"

WHITE = "#F2F2F2"
GREY = "#A9A9A9"
BORDER = "#353535"


# ============================================================
# ASSET-SUCHE
# ============================================================

def find_asset(candidates):
    """
    Sucht nach vorhandenen Bildern im Repository.
    Dadurch funktioniert die App auch dann, wenn die
    Dateiendung oder Groß-/Kleinschreibung abweicht.
    """

    search_dirs = [
        ".",
        "assets",
        "images",
        "icons",
        "static",
    ]

    all_files = []

    for directory in search_dirs:
        if os.path.isdir(directory):
            try:
                for filename in os.listdir(directory):
                    all_files.append(
                        os.path.join(directory, filename)
                    )
            except Exception:
                pass

    # zuerst exakte Treffer
    for candidate in candidates:
        for filepath in all_files:
            if os.path.basename(filepath).lower() == candidate.lower():
                return filepath

    # danach Treffer ohne Dateiendung
    for candidate in candidates:
        candidate_base = os.path.splitext(candidate)[0].lower()

        for filepath in all_files:
            file_base = os.path.splitext(
                os.path.basename(filepath)
            )[0].lower()

            if file_base == candidate_base:
                return filepath

    return None


LOGO_PATH = find_asset([
    "logo.png",
    "logo.jpg",
    "logo.jpeg",
    "CountOrBreak.png",
    "CountOrBreak.jpg",
    "countorbreak.png",
    "count_or_break.png",
])

CALCULATOR_PATH = find_asset([
    "rechner.png",
    "rechner.jpg",
    "rechner.jpeg",
    "calculator.png",
    "calculator.jpg",
    "positionsgroessenrechner.png",
    "positionsgrößenrechner.png",
    "icon_rechner.png",
])


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
<style>

@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@500;600;700&family=Montserrat:wght@400;500;600;700&display=swap');


/* ------------------------------------------------------------
   GRUNDLAYOUT
------------------------------------------------------------ */

html,
body,
[data-testid="stAppViewContainer"] {{
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(217,169,40,0.055),
            transparent 34%
        ),
        #000000 !important;
}}

[data-testid="stAppViewContainer"] {{
    color: {WHITE};
}}

[data-testid="stHeader"] {{
    background: transparent !important;
}}

.block-container {{
    max-width: 1450px !important;
    padding-top: 1.2rem !important;
    padding-bottom: 3rem !important;
    padding-left: 2rem !important;
    padding-right: 2rem !important;
}}


/* ------------------------------------------------------------
   ALLE STANDARD-STREAMLIT-ELEMENTE
------------------------------------------------------------ */

.stMarkdown {{
    color: {WHITE};
}}

label {{
    color: {WHITE} !important;
    font-family: 'Montserrat', Arial, sans-serif !important;
    font-size: 0.94rem !important;
}}

div[data-baseweb="select"] > div {{
    background: #111111 !important;
    border: 1px solid #5E4A1E !important;
    border-radius: 7px !important;
    color: white !important;
}}

div[data-baseweb="select"] span {{
    color: white !important;
}}

input,
textarea {{
    color: white !important;
}}

div[data-testid="stNumberInput"] input {{
    background: #111111 !important;
    color: white !important;
    border: none !important;
}}

div[data-testid="stTextInput"] input {{
    background: #111111 !important;
    color: white !important;
}}


/* ------------------------------------------------------------
   HEADER
------------------------------------------------------------ */

.cb-header {{
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 32px;
    min-height: 150px;
    margin-bottom: 22px;
}}

.cb-logo {{
    display: flex;
    justify-content: center;
    align-items: center;
}}

.cb-logo img {{
    max-width: 190px;
    max-height: 130px;
    object-fit: contain;
}}

.cb-calculator {{
    width: 92px;
    height: 92px;

    display: flex;
    justify-content: center;
    align-items: center;

    border: 1px solid {GOLD};
    border-radius: 18px;

    background:
        radial-gradient(
            circle at 50% 50%,
            rgba(217,169,40,0.18),
            rgba(0,0,0,0.92) 65%
        );

    box-shadow:
        0 0 12px rgba(217,169,40,0.32),
        inset 0 0 18px rgba(217,169,40,0.06);

    transition:
        transform 0.25s ease,
        box-shadow 0.25s ease;
}}

.cb-calculator:hover {{
    transform: scale(1.045);

    box-shadow:
        0 0 24px rgba(217,169,40,0.55),
        inset 0 0 22px rgba(217,169,40,0.12);
}}

.cb-calculator img {{
    width: 68px;
    height: 68px;
    object-fit: contain;
}}


/* ------------------------------------------------------------
   TITEL
------------------------------------------------------------ */

.cb-title-box {{
    width: 100%;

    min-height: 112px;

    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;

    position: relative;

    border: 1px solid {GOLD};
    border-radius: 14px;

    background:
        linear-gradient(
            180deg,
            rgba(25,25,25,0.94),
            rgba(5,5,5,0.98)
        );

    box-shadow:
        0 0 10px rgba(217,169,40,0.18),
        inset 0 0 20px rgba(217,169,40,0.025);

    margin-bottom: 25px;

    overflow: hidden;
}}

.cb-title-box::before {{
    content: "";
    position: absolute;

    width: 34%;
    height: 1px;

    left: 5%;
    top: 50%;

    background:
        linear-gradient(
            90deg,
            transparent,
            {GOLD}
        );

    opacity: 0.8;
}}

.cb-title-box::after {{
    content: "";
    position: absolute;

    width: 34%;
    height: 1px;

    right: 5%;
    top: 50%;

    background:
        linear-gradient(
            90deg,
            {GOLD},
            transparent
        );

    opacity: 0.8;
}}

.cb-title {{
    position: relative;
    z-index: 2;

    font-family: 'Cinzel', Georgia, serif !important;

    font-size: clamp(2rem, 4vw, 3.15rem);

    font-weight: 600;

    letter-spacing: 2px;

    color: {GOLD_LIGHT};

    text-shadow:
        0 0 5px rgba(217,169,40,0.35),
        0 0 14px rgba(217,169,40,0.12);

    text-align: center;
}}

.cb-subtitle {{
    position: relative;
    z-index: 2;

    margin-top: 1px;

    font-family: 'Montserrat', Arial, sans-serif;

    font-size: 1.25rem;

    color: #E7D8A4;

    letter-spacing: 0.8px;

    text-align: center;
}}


/* ------------------------------------------------------------
   PANELS
------------------------------------------------------------ */

.cb-panel {{
    background:
        linear-gradient(
            145deg,
            rgba(20,20,20,0.98),
            rgba(5,5,5,0.98)
        );

    border: 1px solid #353535;

    border-radius: 15px;

    padding: 27px 25px 25px 25px;

    min-height: 100%;

    box-shadow:
        inset 0 0 30px rgba(255,255,255,0.012),
        0 0 2px rgba(217,169,40,0.08);

    position: relative;

    overflow: hidden;
}}

.cb-panel::before {{
    content: "";

    position: absolute;

    left: 0;
    top: 0;

    width: 100%;
    height: 1px;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(217,169,40,0.35),
            transparent
        );
}}

.cb-panel-title {{
    display: flex;
    align-items: center;

    gap: 12px;

    margin-bottom: 25px;

    font-family: 'Montserrat', Arial, sans-serif;

    font-size: 1.45rem;

    font-weight: 500;

    color: {GOLD_LIGHT};

    letter-spacing: 0.5px;
}}

.cb-panel-icon {{
    color: {GOLD_LIGHT};

    width: 30px;
    height: 30px;

    display: flex;
    align-items: center;
    justify-content: center;

    font-size: 1.55rem;

    text-shadow:
        0 0 7px rgba(217,169,40,0.45);
}}


/* ------------------------------------------------------------
   ERGEBNIS
------------------------------------------------------------ */

.cb-result-heading {{
    display: flex;
    align-items: center;
    justify-content: center;

    gap: 20px;

    margin-top: 4px;
    margin-bottom: 18px;

    color: {GOLD_LIGHT};

    font-family: 'Montserrat', Arial, sans-serif;

    font-size: 1.42rem;

    font-weight: 500;

    letter-spacing: 0.5px;
}}

.cb-result-heading::before,
.cb-result-heading::after {{
    content: "";

    height: 1px;

    flex: 1;

    max-width: 125px;

    background:
        linear-gradient(
            90deg,
            transparent,
            {GOLD}
        );
}}

.cb-result-heading::after {{
    background:
        linear-gradient(
            90deg,
            {GOLD},
            transparent
        );
}}

.cb-result {{
    text-align: center;

    padding: 4px 0 24px 0;
}}

.cb-result-value {{
    font-family: 'Montserrat', Arial, sans-serif;

    font-size: clamp(3.4rem, 6vw, 5.5rem);

    line-height: 1;

    font-weight: 700;

    color: {GOLD_BRIGHT};

    letter-spacing: -1px;

    text-shadow:
        0 0 7px rgba(255,224,138,0.65),
        0 0 22px rgba(217,169,40,0.32);

    margin-bottom: 17px;
}}

.cb-result-units {{
    font-family: 'Montserrat', Arial, sans-serif;

    font-size: 1.6rem;

    color: #E8E8E8;

    letter-spacing: 0.5px;
}}


/* ------------------------------------------------------------
   DETAIL ZEILEN
------------------------------------------------------------ */

.cb-detail {{
    border-top: 1px solid #252525;

    padding: 12px 0;

    display: flex;
    justify-content: space-between;
    align-items: center;

    font-family: 'Montserrat', Arial, sans-serif;

    font-size: 1rem;
}}

.cb-detail-label {{
    color: #E0E0E0;
}}

.cb-detail-value {{
    color: {GOLD_LIGHT};

    font-weight: 500;

    text-align: right;
}}


/* ------------------------------------------------------------
   SEKTION
------------------------------------------------------------ */

.cb-section-title {{
    display: flex;
    align-items: center;

    gap: 11px;

    margin-top: 25px;
    margin-bottom: 10px;

    padding-top: 16px;

    border-top: 1px solid #272727;

    font-family: 'Montserrat', Arial, sans-serif;

    font-size: 1.3rem;

    font-weight: 500;

    color: {GOLD_LIGHT};
}}


/* ------------------------------------------------------------
   LONG / SHORT BUTTONS
------------------------------------------------------------ */

div.stButton > button {{
    width: 100% !important;

    min-height: 50px !important;

    background:
        linear-gradient(
            180deg,
            #161616,
            #0D0D0D
        ) !important;

    color: white !important;

    border: 1px solid #464646 !important;

    border-radius: 7px !important;

    font-family: 'Montserrat', Arial, sans-serif !important;

    font-size: 0.98rem !important;

    transition:
        all 0.2s ease !important;
}}

div.stButton > button:hover {{
    border-color: {GOLD} !important;

    color: {GOLD_LIGHT} !important;

    box-shadow:
        0 0 14px rgba(217,169,40,0.2) !important;

    transform: translateY(-1px);
}}

div.stButton > button:focus {{
    border-color: {GOLD} !important;
    box-shadow:
        0 0 12px rgba(217,169,40,0.25) !important;
}}


/* ------------------------------------------------------------
   RISIKOÜBERSICHT
------------------------------------------------------------ */

.cb-risk-panel {{
    margin-top: 20px;

    border: 1px solid #343434;

    border-radius: 15px;

    padding: 23px 26px;

    background:
        linear-gradient(
            145deg,
            #111111,
            #050505
        );
}}

.cb-risk-title {{
    color: {GOLD_LIGHT};

    font-family: 'Montserrat', Arial, sans-serif;

    font-size: 1.25rem;

    margin-bottom: 18px;
}}

.cb-risk-number {{
    color: {GOLD_LIGHT};

    font-size: 1.7rem;

    font-family: 'Montserrat', Arial, sans-serif;
}}

.cb-risk-sub {{
    color: #E3E3E3;

    font-size: 0.98rem;
}}


/* ------------------------------------------------------------
   WARNHINWEIS
------------------------------------------------------------ */

.cb-warning {{
    margin-top: 20px;

    border: 1px solid #72570E;

    border-radius: 14px;

    padding: 21px 24px;

    background:
        linear-gradient(
            145deg,
            rgba(20,20,20,0.98),
            rgba(5,5,5,0.98)
        );

    box-shadow:
        inset 0 0 18px rgba(217,169,40,0.025);
}}

.cb-warning-title {{
    color: {GOLD_LIGHT};

    font-family: 'Montserrat', Arial, sans-serif;

    font-size: 1.25rem;

    margin-bottom: 9px;
}}

.cb-warning-text {{
    color: #DCDCDC;

    font-family: 'Montserrat', Arial, sans-serif;

    line-height: 1.55;

    font-size: 0.92rem;
}}


/* ------------------------------------------------------------
   FOOTER
------------------------------------------------------------ */

.cb-footer {{
    text-align: center;

    margin-top: 28px;

    color: #666666;

    font-size: 0.75rem;

    letter-spacing: 0.5px;
}}


/* ------------------------------------------------------------
   MOBILE
------------------------------------------------------------ */

@media (max-width: 900px) {{

    .block-container {{
        padding-left: 1rem !important;
        padding-right: 1rem !important;
    }}

    .cb-header {{
        gap: 18px;
        min-height: 110px;
    }}

    .cb-logo img {{
        max-width: 150px;
        max-height: 100px;
    }}

    .cb-calculator {{
        width: 75px;
        height: 75px;
    }}

    .cb-calculator img {{
        width: 55px;
        height: 55px;
    }}

    .cb-title-box {{
        min-height: 105px;
    }}

    .cb-title {{
        font-size: 1.75rem;
        letter-spacing: 1px;
    }}

    .cb-subtitle {{
        font-size: 0.95rem;
    }}

    .cb-panel {{
        padding: 21px 17px;
    }}

    .cb-result-value {{
        font-size: 3.3rem;
    }}

    .cb-result-units {{
        font-size: 1.15rem;
    }}
}}

</style>
""",
    unsafe_allow_html=True,
)


# ============================================================
# HEADER
# ============================================================

logo_html = ""

if LOGO_PATH:
    logo_html = f"""
        <div class="cb-logo">
            <img src="{LOGO_PATH}" />
        </div>
    """
else:
    logo_html = """
        <div class="cb-logo">
            <div style="
                color:#F5D36A;
                font-family:Georgia,serif;
                font-size:28px;
                font-weight:bold;
            ">
                COUNT OR BREAK
            </div>
        </div>
    """


calculator_html = ""

if CALCULATOR_PATH:
    calculator_html = f"""
        <div class="cb-calculator">
            <img src="{CALCULATOR_PATH}" />
        </div>
    """
else:
    calculator_html = """
        <div class="cb-calculator">
            <div style="
                font-size:42px;
                color:#F5D36A;
                text-shadow:0 0 12px rgba(217,169,40,0.55);
            ">
                🧮
            </div>
        </div>
    """


st.markdown(
    f"""
    <div class="cb-header">
        {logo_html}
        {calculator_html}
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
# SESSION STATE
# ============================================================

if "direction" not in st.session_state:
    st.session_state.direction = "LONG"


# ============================================================
# HAUPTBEREICH
# ============================================================

left, right = st.columns(
    [1, 1.35],
    gap="large"
)


# ============================================================
# LINKES PANEL – TRADE EINGABEN
# ============================================================

with left:

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
            "USD/CHF",
            "AUD/USD",
            "NZD/USD",
            "US30",
            "NAS100",
            "GER40",
            "UK100",
            "XAU/USD",
            "BTC/USD",
            "Benutzerdefiniert",
        ],
        index=0,
    )


    # --------------------------------------------------------
    # RICHTUNG
    # --------------------------------------------------------

    col_long, col_short = st.columns(2)

    with col_long:
        if st.button(
            "↗  LONG",
            key="long_button",
            use_container_width=True,
        ):
            st.session_state.direction = "LONG"

    with col_short:
        if st.button(
            "↘  SHORT",
            key="short_button",
            use_container_width=True,
        ):
            st.session_state.direction = "SHORT"


    direction = st.session_state.direction


    # aktuelle Richtung
    direction_text = (
        "AKTUELLE RICHTUNG: LONG"
        if direction == "LONG"
        else
        "AKTUELLE RICHTUNG: SHORT"
    )

    st.markdown(
        f"""
        <div style="
            text-align:center;
            margin:10px 0 18px 0;
            color:{GOLD_LIGHT};
            font-family:'Montserrat',Arial,sans-serif;
            font-size:0.78rem;
            letter-spacing:0.6px;
        ">
            {direction_text}
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
        step=500.0,
        format="%.2f",
    )


    # --------------------------------------------------------
    # RISIKO
    # --------------------------------------------------------

    risk_percent = st.number_input(
        "Risiko pro Trade",
        min_value=0.01,
        max_value=100.0,
        value=1.0,
        step=0.1,
        format="%.2f",
    )


    # --------------------------------------------------------
    # EINSTIEG
    # --------------------------------------------------------

    default_entry = {
        "EUR/USD": 1.17000,
        "GBP/USD": 1.35000,
        "USD/JPY": 148.000,
        "USD/CHF": 0.80000,
        "AUD/USD": 0.65000,
        "NZD/USD": 0.59000,
        "US30": 46000.0,
        "NAS100": 23500.0,
        "GER40": 24000.0,
        "UK100": 9000.0,
        "XAU/USD": 3400.0,
        "BTC/USD": 110000.0,
        "Benutzerdefiniert": 1.00000,
    }

    entry_price = st.number_input(
        "Einstiegskurs",
        min_value=0.000001,
        value=float(default_entry[instrument]),
        step=0.00001,
        format="%.5f",
    )


    # --------------------------------------------------------
    # STOP LOSS
    # --------------------------------------------------------

    default_stop = {
        "EUR/USD": 1.16500,
        "GBP/USD": 1.34500,
        "USD/JPY": 147.500,
        "USD/CHF": 0.79500,
        "AUD/USD": 0.64500,
        "NZD/USD": 0.58500,
        "US30": 45750.0,
        "NAS100": 23200.0,
        "GER40": 23750.0,
        "UK100": 8950.0,
        "XAU/USD": 3375.0,
        "BTC/USD": 108000.0,
        "Benutzerdefiniert": 0.99500,
    }

    stop_price = st.number_input(
        "Stop-Loss Kurs",
        min_value=0.000001,
        value=float(default_stop[instrument]),
        step=0.00001,
        format="%.5f",
    )


    # --------------------------------------------------------
    # KONTO-WÄHRUNG
    # --------------------------------------------------------

    account_currency = st.selectbox(
        "Kontowährung",
        [
            "EUR",
            "USD",
            "GBP",
            "CHF",
        ],
        index=0,
    )


    # --------------------------------------------------------
    # OPTIONALE CFD-EINSTELLUNGEN
    # --------------------------------------------------------

    with st.expander(
        "CFD-Einstellungen",
        expanded=False,
    ):

        contract_size = st.number_input(
            "Kontraktgröße pro Lot",
            min_value=0.0001,
            value=100000.0,
            step=1000.0,
            format="%.2f",
        )

        leverage = st.number_input(
            "Hebel",
            min_value=1.0,
            value=30.0,
            step=1.0,
            format="%.0f",
        )

        pip_size = st.number_input(
            "Pip-Größe",
            min_value=0.00000001,
            value=0.0001,
            step=0.0001,
            format="%.8f",
        )


# ============================================================
# BERECHNUNG
# ============================================================

risk_amount = account_size * (risk_percent / 100.0)

price_distance = abs(
    entry_price - stop_price
)


# ------------------------------------------------------------
# Pip-/Punkt-Abstand
# ------------------------------------------------------------

if instrument == "USD/JPY":
    pip_size_effective = 0.01
elif instrument in [
    "US30",
    "NAS100",
    "GER40",
    "UK100",
]:
    pip_size_effective = 1.0
elif instrument == "XAU/USD":
    pip_size_effective = 0.10
elif instrument == "BTC/USD":
    pip_size_effective = 1.0
else:
    pip_size_effective = 0.0001


distance_units = (
    price_distance / pip_size_effective
)


# ------------------------------------------------------------
# Pip-Wert
# ------------------------------------------------------------

if instrument in [
    "EUR/USD",
    "GBP/USD",
    "AUD/USD",
    "NZD/USD",
]:

    # ca. 10 USD pro Pip je Standard-Lot
    pip_value_per_lot = 10.0

elif instrument == "USD/JPY":

    pip_value_per_lot = (
        100000 * 0.01 / entry_price
    )

elif instrument == "USD/CHF":

    pip_value_per_lot = 10.0

elif instrument == "XAU/USD":

    # konservative Standardannahme:
    # 1 Lot = 100 oz, $0.10 Bewegung ≈ $10
    pip_value_per_lot = 10.0

elif instrument in [
    "US30",
    "NAS100",
    "GER40",
    "UK100",
]:

    # Index-CFD:
    # 1 Lot ≈ 1 Währungseinheit pro Punkt
    pip_value_per_lot = 1.0

elif instrument == "BTC/USD":

    # vereinfachte CFD-Annahme
    pip_value_per_lot = 1.0

else:

    pip_value_per_lot = (
        contract_size * pip_size_effective
    )


# ------------------------------------------------------------
# Positionsgröße
# ------------------------------------------------------------

if (
    distance_units > 0
    and pip_value_per_lot > 0
):

    raw_lots = (
        risk_amount
        /
        (
            distance_units
            * pip_value_per_lot
        )
    )

else:

    raw_lots = 0.0


# ------------------------------------------------------------
# sinnvolle Lot-Schritte
# ------------------------------------------------------------

if raw_lots >= 10:
    lot_step = 0.10

elif raw_lots >= 1:
    lot_step = 0.01

else:
    lot_step = 0.01


lots = math.floor(
    raw_lots / lot_step
) * lot_step


lots = max(
    0.0,
    lots
)


# Einheiten
units = lots * contract_size


# ------------------------------------------------------------
# Positionswert
# ------------------------------------------------------------

position_value = (
    lots * contract_size * entry_price
)


# ------------------------------------------------------------
# Margin
# ------------------------------------------------------------

if leverage > 0:

    margin_required = (
        position_value / leverage
    )

else:

    margin_required = 0.0


free_margin = max(
    0.0,
    account_size - margin_required
)


# ============================================================
# RECHTES PANEL – ERGEBNIS
# ============================================================

with right:

    st.markdown(
        """
        <div class="cb-panel">

            <div class="cb-panel-title">

                <div class="cb-panel-icon">
                    ◎
                </div>

                <div>
                    ERGEBNIS
                </div>

            </div>

        """,
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # EMPFOHLENE POSITION
    # --------------------------------------------------------

    st.markdown(
        """
        <div class="cb-result-heading">
            EMPFOHLENE POSITION
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        f"""
        <div class="cb-result">

            <div class="cb-result-value">
                {lots:.2f} LOTS
            </div>

            <div class="cb-result-units">
                = {units:,.0f} EINHEITEN
            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # DETAILS
    # --------------------------------------------------------

    st.markdown(
        f"""
        <div class="cb-detail">
            <div class="cb-detail-label">
                Max. Verlust
            </div>
            <div class="cb-detail-value">
                {risk_amount:,.2f} {account_currency}
            </div>
        </div>

        <div class="cb-detail">
            <div class="cb-detail-label">
                Stop-Abstand
            </div>
            <div class="cb-detail-value">
                {distance_units:,.1f} Pips
            </div>
        </div>

        <div class="cb-detail">
            <div class="cb-detail-label">
                Positionswert
            </div>
            <div class="cb-detail-value">
                {position_value:,.2f} {account_currency}
            </div>
        </div>

        <div class="cb-detail">
            <div class="cb-detail-label">
                Pip-Wert
            </div>
            <div class="cb-detail-value">
                {pip_value_per_lot * lots:,.2f} {account_currency}
            </div>
        </div>

        <div class="cb-detail">
            <div class="cb-detail-label">
                Risikoprozent
            </div>
            <div class="cb-detail-value">
                {risk_percent:.2f} %
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
            ⚖ &nbsp; MARGIN & HEBEL
        </div>
        """,
        unsafe_allow_html=True,
    )


    st.markdown(
        f"""
        <div class="cb-detail">
            <div class="cb-detail-label">
                Erforderliche Margin
            </div>
            <div class="cb-detail-value">
                {margin_required:,.2f} {account_currency}
            </div>
        </div>

        <div class="cb-detail">
            <div class="cb-detail-label">
                Verwendeter Hebel
            </div>
            <div class="cb-detail-value">
                1 : {leverage:.0f}
            </div>
        </div>

        <div class="cb-detail">
            <div class="cb-detail-label">
                Freie Margin (geschätzt)
            </div>
            <div class="cb-detail-value">
                {free_margin:,.2f} {account_currency}
            </div>
        </div>

        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

risk_ratio = min(
    max(risk_percent / 5.0, 0.0),
    1.0
)

filled_blocks = int(
    risk_ratio * 20
)

blocks = ""

for i in range(20):

    if i < filled_blocks:
        blocks += "▮"

    else:
        blocks += "▮"


st.markdown(
    f"""
    <div class="cb-risk-panel">

        <div class="cb-risk-title">
            🛡 &nbsp; RISIKOÜBERSICHT
        </div>

        <div style="
            display:flex;
            align-items:center;
            gap:28px;
            flex-wrap:wrap;
        ">

            <div style="
                width:110px;
                height:110px;
                border-radius:50%;
                border:10px solid #353535;
                display:flex;
                align-items:center;
                justify-content:center;
                flex-direction:column;
                box-shadow:
                    inset 0 0 15px rgba(217,169,40,0.08);
            ">

                <div class="cb-risk-number">
                    {risk_percent:.2f}%
                </div>

            </div>

            <div>

                <div class="cb-risk-number">
                    {risk_amount:,.2f} {account_currency}
                </div>

                <div class="cb-risk-sub">
                    von {account_size:,.2f} {account_currency}
                </div>

                <div style="
                    margin-top:14px;
                    color:#625B4A;
                    letter-spacing:3px;
                    font-size:20px;
                    white-space:nowrap;
                    overflow:hidden;
                    max-width:720px;
                ">
                    {blocks}
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
            der Hebelwirkung ein hohes Risiko, schnell Geld zu
            verlieren. Ein hoher Anteil der Kleinanlegerkonten
            verliert beim CFD-Handel Geld. Überlegen Sie sorgfältig,
            ob Sie verstehen, wie CFDs funktionieren und ob Sie es
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
    """
    <div class="cb-footer">
        COUNT OR BREAK &nbsp;•&nbsp;
        PLAN. EXECUTE. SUCCEED.
    </div>
    """,
    unsafe_allow_html=True,
)
