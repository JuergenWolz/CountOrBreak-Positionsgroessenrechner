import streamlit as st
import os
import math


# ============================================================
# COUNT OR BREAK
# POSITIONSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    page_icon="📐",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# DESIGN
# ============================================================

GOLD = "#D7AD3A"
GOLD_LIGHT = "#F3D77A"
GOLD_BRIGHT = "#FFE08A"
GOLD_DARK = "#9C741C"

BLACK = "#030303"
BLACK_PANEL = "#0B0B0B"

WHITE = "#F4F4F4"
MUTED = "#B9B9B9"


# ============================================================
# ASSET-SUCHE
# ============================================================

def find_asset(names):

    directories = [
        ".",
        "assets",
        "images",
        "icons",
        "static",
    ]

    for directory in directories:

        for name in names:

            path = os.path.join(directory, name)

            if os.path.exists(path):
                return path

    return None


calculator_icon = find_asset([
    "calculator.png",
    "rechner.png",
    "icon_calculator.png",
    "icon_rechner.png",
    "positionsgroessenrechner.png",
    "positionsgrößenrechner.png",
    "positionsgroessenrechner_icon.png",
    "calculator_icon.png",
])


# ============================================================
# ZAHLENFORMATIERUNG
# ============================================================

def de_number(value, decimals=2):

    try:

        text = f"{value:,.{decimals}f}"

        return (
            text
            .replace(",", "TEMP")
            .replace(".", ",")
            .replace("TEMP", ".")
        )

    except Exception:

        return "0"


def de_integer(value):

    try:

        text = f"{int(round(value)):,}"

        return text.replace(",", ".")

    except Exception:

        return "0"


# ============================================================
# BERECHNUNG
# ============================================================

def calculate_position(
    account_size,
    risk_percent,
    entry_price,
    stop_price,
    contract_size,
    pip_size,
    conversion_rate,
):

    if account_size <= 0:
        return None

    if risk_percent <= 0:
        return None

    if entry_price <= 0:
        return None

    if stop_price <= 0:
        return None

    if contract_size <= 0:
        return None

    if pip_size <= 0:
        return None

    if conversion_rate <= 0:
        return None

    stop_distance = abs(entry_price - stop_price)

    if stop_distance <= 0:
        return None

    stop_pips = stop_distance / pip_size

    max_loss = account_size * risk_percent / 100

    pip_value_per_lot = (
        contract_size
        * pip_size
        * conversion_rate
    )

    if pip_value_per_lot <= 0:
        return None

    lots = max_loss / (
        stop_pips * pip_value_per_lot
    )

    units = lots * contract_size

    position_value_quote = units * entry_price

    position_value_account = (
        position_value_quote
        * conversion_rate
    )

    total_pip_value = (
        pip_value_per_lot
        * lots
    )

    return {
        "lots": lots,
        "units": units,
        "stop_pips": stop_pips,
        "max_loss": max_loss,
        "pip_value": total_pip_value,
        "position_value": position_value_account,
    }


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ========================================================
       GRUNDLAYOUT
       ======================================================== */

    @import url(
        'https://fonts.googleapis.com/css2?family=Cinzel:wght@400;500;600;700&family=Montserrat:wght@300;400;500;600&display=swap'
    );

    html,
    body,
    [class*="css"] {{

        font-family: 'Montserrat', sans-serif;

    }}

    .stApp {{

        background:

            radial-gradient(
                circle at 50% 8%,
                rgba(215,173,58,0.075),
                transparent 30%
            ),

            radial-gradient(
                circle at 50% 100%,
                rgba(215,173,58,0.025),
                transparent 35%
            ),

            #030303;

        color: {WHITE};

    }}


    .block-container {{

        max-width: 1500px;

        padding-top: 1.4rem;
        padding-bottom: 3rem;

    }}


    /* ========================================================
       STREAMLIT CONTAINER
       ======================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {{

        background:
            linear-gradient(
                145deg,
                rgba(18,18,18,0.98),
                rgba(5,5,5,0.98)
            ) !important;

        border:
            1px solid #353535 !important;

        border-radius:
            15px !important;

        box-shadow:
            inset 0 0 35px rgba(255,255,255,0.012),
            0 0 10px rgba(0,0,0,0.75);

        padding:
            4px !important;

    }}


    /* ========================================================
       HEADER
       ======================================================== */

    .cb-header {{

        display: flex;

        justify-content: center;

        align-items: center;

        margin-bottom: 20px;

    }}


    .cb-calculator-box {{

        width: 92px;
        height: 92px;

        border:
            1px solid rgba(215,173,58,0.95);

        border-radius: 18px;

        display: flex;

        justify-content: center;

        align-items: center;

        background:

            radial-gradient(
                circle at center,
                rgba(215,173,58,0.12),
                rgba(0,0,0,0.9) 72%
            );

        box-shadow:

            0 0 12px
            rgba(215,173,58,0.28),

            inset 0 0 20px
            rgba(215,173,58,0.06);

    }}


    .cb-calculator-box img {{

        width: 68px;
        height: 68px;

        object-fit: contain;

    }}


    /* ========================================================
       TITEL
       ======================================================== */

    .cb-title-box {{

        position: relative;

        min-height: 125px;

        display: flex;

        flex-direction: column;

        justify-content: center;

        align-items: center;

        text-align: center;

        border:
            1px solid {GOLD};

        border-radius: 15px;

        background:

            linear-gradient(
                180deg,
                rgba(20,20,20,0.96),
                rgba(5,5,5,0.99)
            );

        box-shadow:

            0 0 10px
            rgba(215,173,58,0.22),

            inset 0 0 35px
            rgba(215,173,58,0.025);

        overflow: hidden;

        margin-bottom: 26px;

    }}


    .cb-title-box::before {{

        content: "";

        position: absolute;

        left: 5%;
        width: 14%;

        height: 1px;

        top: 50%;

        background:

            linear-gradient(
                90deg,
                transparent,
                {GOLD},
                transparent
            );

    }}


    .cb-title-box::after {{

        content: "";

        position: absolute;

        right: 5%;
        width: 14%;

        height: 1px;

        top: 50%;

        background:

            linear-gradient(
                90deg,
                transparent,
                {GOLD},
                transparent
            );

    }}


    .cb-title {{

        position: relative;
        z-index: 2;

        font-family:
            'Cinzel',
            Georgia,
            serif;

        font-size:
            clamp(28px, 4vw, 47px);

        font-weight:
            600;

        letter-spacing:
            3px;

        background:

            linear-gradient(
                180deg,
                {GOLD_BRIGHT},
                {GOLD_LIGHT},
                {GOLD},
                {GOLD_DARK}
            );

        -webkit-background-clip:
            text;

        -webkit-text-fill-color:
            transparent;

        text-shadow:
            0 0 18px
            rgba(215,173,58,0.22);

    }}


    .cb-subtitle {{

        position: relative;
        z-index: 2;

        margin-top: 3px;

        font-family:
            'Montserrat',
            sans-serif;

        font-size: 20px;

        font-weight: 400;

        letter-spacing: 1px;

        color: #E9D58B;

    }}


    /* ========================================================
       PANEL TITEL
       ======================================================== */

    .cb-panel-title {{

        display: flex;

        align-items: center;

        gap: 12px;

        padding:
            8px 12px 16px 12px;

        font-family:
            'Cinzel',
            Georgia,
            serif;

        font-size: 22px;

        font-weight: 500;

        letter-spacing: 1px;

        color: {GOLD_LIGHT};

    }}


    .cb-panel-icon {{

        width: 30px;
        height: 30px;

        display: flex;

        align-items: center;
        justify-content: center;

        color: {GOLD_LIGHT};

        font-size: 25px;

        text-shadow:
            0 0 9px
            rgba(215,173,58,0.42);

    }}


    /* ========================================================
       INPUTS
       ======================================================== */

    .stSelectbox label,
    .stNumberInput label {{

        color: #E7E7E7 !important;

        font-family:
            'Montserrat',
            sans-serif !important;

        font-size: 15px !important;

        font-weight: 400 !important;

    }}


    div[data-baseweb="select"] > div {{

        background: #101010 !important;

        border:
            1px solid #55451F !important;

        border-radius:
            8px !important;

        min-height:
            49px !important;

        color:
            white !important;

    }}


    div[data-baseweb="select"] span {{

        color:
            #F1F1F1 !important;

    }}


    div[data-testid="stNumberInput"] input {{

        color:
            #F1F1F1 !important;

        background:
            transparent !important;

    }}


    div[data-baseweb="input"] {{

        background:
            #101010 !important;

        border:
            1px solid #484848 !important;

        border-radius:
            8px !important;

        min-height:
            49px !important;

    }}


    div[data-baseweb="input"]:focus-within {{

        border-color:
            {GOLD} !important;

        box-shadow:
            0 0 9px
            rgba(215,173,58,0.17) !important;

    }}


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {{

        width: 100%;

        min-height: 49px;

        border-radius:
            8px;

        background:
            linear-gradient(
                180deg,
                #151515,
                #0B0B0B
            );

        border:
            1px solid #505050;

        color:
            #EEEEEE;

        font-family:
            'Montserrat',
            sans-serif;

        font-size:
            16px;

        transition:
            all 0.18s ease;

    }}


    .stButton > button:hover {{

        border-color:
            {GOLD};

        color:
            {GOLD_LIGHT};

        transform:
            translateY(-1px);

        box-shadow:
            0 0 12px
            rgba(215,173,58,0.18);

    }}


    /* ========================================================
       ERGEBNIS
       ======================================================== */

    .cb-result-title {{

        text-align:
            center;

        font-family:
            'Cinzel',
            Georgia,
            serif;

        font-size:
            24px;

        font-weight:
            500;

        letter-spacing:
            1px;

        color:
            {GOLD_LIGHT};

        margin:
            10px 0 12px 0;

    }}


    .cb-result-value {{

        text-align:
            center;

        font-family:
            'Montserrat',
            sans-serif;

        font-size:
            clamp(48px, 5vw, 72px);

        line-height:
            1;

        font-weight:
            700;

        background:

            linear-gradient(
                180deg,
                #FFF0A8,
                {GOLD_LIGHT},
                {GOLD}
            );

        -webkit-background-clip:
            text;

        -webkit-text-fill-color:
            transparent;

        text-shadow:

            0 0 15px
            rgba(255,220,100,0.28),

            0 0 30px
            rgba(215,173,58,0.16);

        margin:
            22px 0 13px 0;

    }}


    .cb-units {{

        text-align:
            center;

        color:
            #F0F0F0;

        font-size:
            24px;

        margin-bottom:
            25px;

    }}


    .cb-result-line {{

        height:
            1px;

        background:

            linear-gradient(
                90deg,
                transparent,
                rgba(215,173,58,0.55),
                transparent
            );

        margin:
            13px 0;

    }}


    /* ========================================================
       ERGEBNIS-ZEILEN
       ======================================================== */

    .cb-row {{

        display:
            flex;

        justify-content:
            space-between;

        align-items:
            center;

        padding:
            11px 4px;

        border-bottom:
            1px solid
            rgba(255,255,255,0.075);

        font-size:
            16px;

    }}


    .cb-row-label {{

        color:
            #E6E6E6;

    }}


    .cb-row-value {{

        color:
            {GOLD_LIGHT};

        font-weight:
            500;

        text-align:
            right;

    }}


    /* ========================================================
       ABSCHNITTSÜBERSCHRIFTEN
       ======================================================== */

    .cb-section-title {{

        display:
            flex;

        align-items:
            center;

        gap:
            9px;

        margin:
            25px 4px 10px 4px;

        font-family:
            'Cinzel',
            Georgia,
            serif;

        font-size:
            20px;

        letter-spacing:
            0.5px;

        color:
            {GOLD_LIGHT};

    }}


    /* ========================================================
       RISIKOÜBERSICHT
       ======================================================== */

    .cb-risk-title {{

        font-family:
            'Cinzel',
            Georgia,
            serif;

        color:
            {GOLD_LIGHT};

        font-size:
            21px;

        letter-spacing:
            1px;

        margin:
            4px 10px 15px 10px;

    }}


    .cb-risk-content {{

        display:
            flex;

        align-items:
            center;

        gap:
            30px;

        padding:
            5px 12px 15px 12px;

    }}


    .cb-risk-circle {{

        width:
            120px;

        height:
            120px;

        min-width:
            120px;

        border-radius:
            50%;

        display:
            flex;

        flex-direction:
            column;

        justify-content:
            center;

        align-items:
            center;

        border:
            9px solid #3C3C3C;

        box-shadow:
            inset 0 0 20px rgba(0,0,0,0.8);

    }}


    .cb-risk-percent {{

        color:
            {GOLD_LIGHT};

        font-size:
            25px;

        font-weight:
            500;

    }}


    .cb-risk-money {{

        color:
            {GOLD_LIGHT};

        font-size:
            22px;

        font-weight:
            500;

        margin-bottom:
            3px;

    }}


    .cb-risk-description {{

        color:
            #EEEEEE;

        font-size:
            17px;

    }}


    /* ========================================================
       RISIKOHINWEIS
       ======================================================== */

    .cb-warning-title {{

        font-family:
            'Cinzel',
            Georgia,
            serif;

        color:
            {GOLD_LIGHT};

        font-size:
            20px;

        letter-spacing:
            0.7px;

        margin:
            4px 10px 9px 10px;

    }}


    .cb-warning-text {{

        color:
            #DFDFDF;

        font-size:
            14px;

        line-height:
            1.65;

        padding:
            0 10px 8px 10px;

    }}


    /* ========================================================
       HINWEISTEXT
       ======================================================== */

    .cb-small-info {{

        color:
            #777777;

        font-size:
            11px;

        line-height:
            1.5;

        margin:
            4px 10px 10px 10px;

    }}


    /* ========================================================
       FOOTER
       ======================================================== */

    .cb-footer {{

        text-align:
            center;

        color:
            #686868;

        font-size:
            11px;

        letter-spacing:
            1.2px;

        margin-top:
            25px;

    }}


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 900px) {{

        .block-container {{

            padding-left:
                0.8rem;

            padding-right:
                0.8rem;

        }}

        .cb-title-box::before,
        .cb-title-box::after {{

            display:
                none;

        }}

        .cb-title {{

            font-size:
                28px;

            letter-spacing:
                1.5px;

        }}

        .cb-subtitle {{

            font-size:
                16px;

        }}

        .cb-result-value {{

            font-size:
                50px;

        }}

        .cb-risk-content {{

            flex-direction:
                column;

            align-items:
                flex-start;

        }}

    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HEADER – NUR RECHNER-ICON
# ============================================================

st.markdown(
    '<div class="cb-header">',
    unsafe_allow_html=True,
)

if calculator_icon:

    st.image(
        calculator_icon,
        width=92,
    )

else:

    st.markdown(
        """
        <div class="cb-calculator-box">
            <span style="
                font-size:42px;
                color:#F3D77A;
            ">▦</span>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    '</div>',
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
# ============================================================

left_column, right_column = st.columns(
    [0.95, 1.25],
    gap="large",
)


# ============================================================
# LINKES PANEL
# ============================================================

with left_column:

    with st.container(border=True):

        st.markdown(
            """
            <div class="cb-panel-title">

                <div class="cb-panel-icon">
                    ⚖
                </div>

                <div>
                    TRADE-EINGABEN
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )

        # ----------------------------------------------------
        # INSTRUMENT
        # ----------------------------------------------------

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

        # ----------------------------------------------------
        # RICHTUNG
        # ----------------------------------------------------

        st.markdown(
            """
            <div style="
                color:#E7E7E7;
                font-size:15px;
                margin-top:10px;
                margin-bottom:7px;
            ">
                Richtung
            </div>
            """,
            unsafe_allow_html=True,
        )

        direction_left, direction_right = st.columns(2)

        if "direction" not in st.session_state:
            st.session_state.direction = "LONG"

        with direction_left:

            if st.button(
                "↗  LONG",
                key="direction_long",
                use_container_width=True,
            ):

                st.session_state.direction = "LONG"

        with direction_right:

            if st.button(
                "↓  SHORT",
                key="direction_short",
                use_container_width=True,
            ):

                st.session_state.direction = "SHORT"

        st.markdown(
            f"""
            <div style="
                text-align:center;
                color:{GOLD};
                font-size:11px;
                letter-spacing:0.8px;
                margin-top:2px;
                margin-bottom:10px;
            ">
                AKTUELLE RICHTUNG: {st.session_state.direction}
            </div>
            """,
            unsafe_allow_html=True,
        )

        # ----------------------------------------------------
        # KONTOGRÖSSE
        # ----------------------------------------------------

        account_size = st.number_input(
            "Kontogröße",
            min_value=1.0,
            value=10000.0,
            step=100.0,
            format="%.2f",
        )

        # ----------------------------------------------------
        # RISIKO
        # ----------------------------------------------------

        risk_percent = st.number_input(
            "Risiko pro Trade",
            min_value=0.01,
            max_value=100.0,
            value=1.0,
            step=0.1,
            format="%.2f",
        )

        # ----------------------------------------------------
        # EINSTIEG
        # ----------------------------------------------------

        entry_price = st.number_input(
            "Einstiegskurs",
            min_value=0.000001,
            value=1.17000,
            step=0.00001,
            format="%.5f",
        )

        # ----------------------------------------------------
        # STOP LOSS
        # ----------------------------------------------------

        stop_price = st.number_input(
            "Stop-Loss Kurs",
            min_value=0.000001,
            value=1.16500,
            step=0.00001,
            format="%.5f",
        )

        # ----------------------------------------------------
        # KONTO-WÄHRUNG
        # ----------------------------------------------------

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

        # ----------------------------------------------------
        # TECHNISCHE PARAMETER
        # ----------------------------------------------------

        if instrument == "XAU/USD – Gold":

            default_contract = 100.0
            default_pip = 0.01

        elif instrument in [
            "US500",
            "NAS100",
            "GER40",
            "UK100",
        ]:

            default_contract = 1.0
            default_pip = 1.0

        elif instrument in [
            "BTC/USD",
            "ETH/USD",
        ]:

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
            step=float(default_pip),
            format="%.6f",
        )

        conversion_rate = st.number_input(
            "Umrechnung in Kontowährung",
            min_value=0.000001,
            value=0.8550,
            step=0.001,
            format="%.4f",
        )

        st.markdown(
            """
            <div class="cb-small-info">

                Die technischen Parameter können bei Bedarf
                an das jeweilige Pepperstone-CFD-Instrument
                angepasst werden.

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# BERECHNUNG
# ============================================================

result = calculate_position(
    account_size=account_size,
    risk_percent=risk_percent,
    entry_price=entry_price,
    stop_price=stop_price,
    contract_size=contract_size,
    pip_size=pip_size,
    conversion_rate=conversion_rate,
)


# ============================================================
# RECHTES PANEL
# ============================================================

with right_column:

    with st.container(border=True):

        st.markdown(
            """
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

        if result is None:

            st.markdown(
                """
                <div style="
                    text-align:center;
                    padding:90px 20px;
                    color:#999;
                    font-size:17px;
                ">
                    Bitte überprüfe deine Eingaben.
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

            # ------------------------------------------------
            # POSITION
            # ------------------------------------------------

            st.markdown(
                """
                <div class="cb-result-title">
                    ─── &nbsp; EMPFOHLENE POSITION &nbsp; ───
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                f"""
                <div class="cb-result-value">
                    {de_number(lots, 2)} LOTS
                </div>

                <div class="cb-units">
                    = {de_integer(units)} EINHEITEN
                </div>

                <div class="cb-result-line"></div>
                """,
                unsafe_allow_html=True,
            )

            # ------------------------------------------------
            # RESULTAT
            # ------------------------------------------------

            st.markdown(
                f"""
                <div class="cb-row">

                    <div class="cb-row-label">
                        Max. Verlust
                    </div>

                    <div class="cb-row-value">
                        {de_number(max_loss, 2)}
                        {account_currency}
                    </div>

                </div>

                <div class="cb-row">

                    <div class="cb-row-label">
                        Stop-Abstand
                    </div>

                    <div class="cb-row-value">
                        {de_number(stop_pips, 1)}
                        Pips
                    </div>

                </div>

                <div class="cb-row">

                    <div class="cb-row-label">
                        Positionswert
                    </div>

                    <div class="cb-row-value">
                        {de_number(position_value, 2)}
                        {account_currency}
                    </div>

                </div>

                <div class="cb-row">

                    <div class="cb-row-label">
                        Pip-Wert
                    </div>

                    <div class="cb-row-value">
                        {de_number(pip_value, 2)}
                        {account_currency}
                    </div>

                </div>

                <div class="cb-row">

                    <div class="cb-row-label">
                        Risikoprozent
                    </div>

                    <div class="cb-row-value">
                        {de_number(risk_percent, 2)} %
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

            # ------------------------------------------------
            # MARGIN / HEBEL
            # ------------------------------------------------

            st.markdown(
                """
                <div class="cb-section-title">
                    ⚖ &nbsp; MARGIN &amp; HEBEL
                </div>
                """,
                unsafe_allow_html=True,
            )

            st.markdown(
                """
                <div class="cb-row">

                    <div class="cb-row-label">
                        Erforderliche Margin
                    </div>

                    <div class="cb-row-value">
                        abhängig vom Hebel
                    </div>

                </div>

                <div class="cb-row">

                    <div class="cb-row-label">
                        Verwendeter Hebel
                    </div>

                    <div class="cb-row-value">
                        Pepperstone
                    </div>

                </div>

                <div class="cb-row">

                    <div class="cb-row-label">
                        Freie Margin
                    </div>

                    <div class="cb-row-value">
                        abhängig vom Konto
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

if result:

    with st.container(border=True):

        st.markdown(
            """
            <div class="cb-risk-title">
                ◇ &nbsp; RISIKOÜBERSICHT
            </div>
            """,
            unsafe_allow_html=True,
        )

        risk_col_1, risk_col_2 = st.columns(
            [0.25, 0.75]
        )

        with risk_col_1:

            st.markdown(
                f"""
                <div class="cb-risk-content">

                    <div class="cb-risk-circle">

                        <div class="cb-risk-percent">
                            {de_number(risk_percent, 2)} %
                        </div>

                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )

        with risk_col_2:

            st.markdown(
                f"""
                <div style="
                    padding-top:18px;
                ">

                    <div class="cb-risk-money">
                        {de_number(max_loss, 2)}
                        {account_currency}
                    </div>

                    <div class="cb-risk-description">
                        von {de_number(account_size, 2)}
                        {account_currency}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


# ============================================================
# RISIKOHINWEIS
# ============================================================

with st.container(border=True):

    st.markdown(
        """
        <div class="cb-warning-title">
            ⚠ &nbsp; RISIKOHINWEIS
        </div>

        <div class="cb-warning-text">

            CFDs sind komplexe Instrumente und bergen aufgrund
            der Hebelwirkung ein hohes Risiko, schnell Geld zu
            verlieren. Ein Verlust kann den eingesetzten
            Kapitalbetrag erheblich reduzieren.

            Bitte stellen Sie sicher, dass Sie die Funktionsweise
            von CFDs, Hebelwirkung, Margin und Stop-Loss verstehen
            und dass Sie das damit verbundene Risiko tragen können.

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
        RISK FIRST. PROFITS SECOND.
    </div>
    """,
    unsafe_allow_html=True,
)
