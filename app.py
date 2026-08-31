import math
import os

import streamlit as st


# ============================================================
# COUNT OR BREAK
# POSITIONSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    page_icon=None,
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# KONFIGURATION
# ============================================================

STARTSEITE_URL = "https://countorbreak.streamlit.app"

LOGO_FILE = "countorbreak_logo.png"

# Goldtöne an das CountOrBreak-Logo angelehnt
GOLD = "#B88624"
GOLD_DARK = "#8A6417"
GOLD_DEEP = "#6F4F12"
GOLD_LIGHT = "#D4A83A"
GOLD_HIGHLIGHT = "#E7C15A"

BACKGROUND = "#050505"
PANEL = "#0C0C0C"
PANEL_LIGHT = "#111111"
BORDER = "#302A1C"

TEXT = "#F2F0EA"
TEXT_MUTED = "#B7B2A7"


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* ========================================================
       GLOBAL
       ======================================================== */

    html,
    body,
    [data-testid="stAppViewContainer"],
    [data-testid="stApp"] {{
        background: {BACKGROUND} !important;
    }}

    html,
    body,
    [class*="css"] {{
        font-family:
            -apple-system,
            BlinkMacSystemFont,
            "Segoe UI",
            Arial,
            Helvetica,
            sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(184, 134, 36, 0.075),
                transparent 34%
            ),
            {BACKGROUND} !important;

        color: {TEXT};
    }}

    [data-testid="stHeader"] {{
        background: transparent !important;
    }}

    [data-testid="stToolbar"] {{
        background: transparent !important;
    }}

    .block-container {{
        max-width: 1450px !important;

        padding-top: 1.25rem !important;
        padding-bottom: 4rem !important;

        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }}


    /* ========================================================
       ZURÜCK ZUR STARTSEITE
       ======================================================== */

    .back-area {{
        margin-bottom: 30px;
    }}

    .back-link {{
        display: inline-flex;
        align-items: center;
        justify-content: center;

        gap: 10px;

        padding: 11px 19px;

        border: 1px solid {GOLD_DARK};
        border-radius: 9px;

        background:
            linear-gradient(
                145deg,
                rgba(22, 22, 22, 0.98),
                rgba(7, 7, 7, 0.98)
            );

        color: {GOLD} !important;

        text-decoration: none !important;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 15px;
        font-weight: 700;

        letter-spacing: 0.8px;

        box-shadow:
            0 0 0 rgba(184, 134, 36, 0);

        transition:
            color 0.22s ease,
            border-color 0.22s ease,
            box-shadow 0.22s ease,
            transform 0.22s ease;

        cursor: pointer;
    }}

    .back-link:visited {{
        color: {GOLD} !important;
    }}

    .back-link:hover {{
        color: {GOLD_HIGHLIGHT} !important;

        border-color: {GOLD_LIGHT};

        box-shadow:
            0 0 18px rgba(184, 134, 36, 0.34),
            inset 0 0 14px rgba(184, 134, 36, 0.06);

        transform: translateY(-1px);
    }}

    .back-arrow {{
        font-family: Arial, sans-serif;
        font-size: 19px;
        line-height: 1;
    }}


    /* ========================================================
       LOGO
       ======================================================== */

    .logo-area {{
        display: flex;
        justify-content: center;
        align-items: center;

        width: 100%;

        margin-top: 5px;
        margin-bottom: 28px;
    }}

    .logo-frame {{
        display: flex;
        justify-content: center;
        align-items: center;

        width: 100%;
    }}

    .logo-frame img {{
        width: 330px;
        max-width: 72vw;
        height: auto;

        display: block;

        filter:
            drop-shadow(0 0 12px rgba(184, 134, 36, 0.18));
    }}


    /* ========================================================
       HAUPTTITEL
       ======================================================== */

    .title-card {{
        position: relative;

        width: 100%;

        margin-bottom: 28px;

        padding: 27px 32px 24px;

        border: 1px solid {GOLD_DARK};
        border-radius: 15px;

        background:
            linear-gradient(
                145deg,
                rgba(19, 19, 19, 0.97),
                rgba(6, 6, 6, 0.99)
            );

        box-shadow:
            0 0 18px rgba(184, 134, 36, 0.08),
            inset 0 0 28px rgba(255, 255, 255, 0.012);

        text-align: center;

        overflow: hidden;
    }}

    .title-card::before {{
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
                rgba(184, 134, 36, 0.30),
                transparent
            );

        pointer-events: none;
    }}

    .title-row {{
        position: relative;

        display: flex;
        align-items: center;
        justify-content: center;

        gap: 25px;

        z-index: 1;
    }}

    .title-line {{
        flex: 1;

        max-width: 180px;

        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD}
            );

        box-shadow:
            0 0 8px rgba(184, 134, 36, 0.25);
    }}

    .title-line-right {{
        background:
            linear-gradient(
                90deg,
                {GOLD},
                transparent
            );
    }}

    .main-title {{
        color: {GOLD_LIGHT};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: clamp(28px, 4vw, 48px);

        font-weight: 700;

        letter-spacing: 2px;

        text-transform: uppercase;

        text-shadow:
            0 0 9px rgba(184, 134, 36, 0.18);
    }}

    .subtitle {{
        position: relative;

        margin-top: 8px;

        color: #C7AD70;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 19px;

        letter-spacing: 0.8px;

        z-index: 1;
    }}


    /* ========================================================
       STREAMLIT COLUMNS
       ======================================================== */

    [data-testid="stHorizontalBlock"] {{
        gap: 1.4rem;
    }}


    /* ========================================================
       PANELS
       ======================================================== */

    .panel-card {{
        width: 100%;

        min-height: 700px;

        padding: 25px 28px;

        border: 1px solid {BORDER};
        border-radius: 15px;

        background:
            linear-gradient(
                145deg,
                rgba(17, 17, 17, 0.97),
                rgba(7, 7, 7, 0.99)
            );

        box-shadow:
            inset 0 0 30px rgba(255, 255, 255, 0.008),
            0 8px 30px rgba(0, 0, 0, 0.28);
    }}

    .panel-header {{
        display: flex;
        align-items: center;

        gap: 12px;

        margin-bottom: 25px;

        color: {GOLD};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 23px;

        font-weight: 700;

        letter-spacing: 0.7px;

        text-transform: uppercase;
    }}

    .panel-header-symbol {{
        color: {GOLD};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 23px;

        text-shadow:
            0 0 8px rgba(184, 134, 36, 0.45);
    }}


    /* ========================================================
       STREAMLIT INPUT LABELS
       ======================================================== */

    [data-testid="stWidgetLabel"] p {{
        color: {TEXT} !important;

        font-size: 14px !important;

        font-weight: 500 !important;
    }}


    /* ========================================================
       SELECTBOX
       ======================================================== */

    div[data-baseweb="select"] > div {{
        background-color: #111111 !important;

        border: 1px solid #40361F !important;

        border-radius: 8px !important;

        color: {TEXT} !important;
    }}

    div[data-baseweb="select"] > div:hover {{
        border-color: {GOLD_DARK} !important;
    }}

    div[data-baseweb="select"] > div:focus-within {{
        border-color: {GOLD} !important;

        box-shadow:
            0 0 0 1px {GOLD} !important;
    }}


    /* ========================================================
       NUMBER INPUT
       ======================================================== */

    div[data-baseweb="input"] > div {{
        background-color: #111111 !important;

        border: 1px solid #40361F !important;

        border-radius: 8px !important;
    }}

    div[data-baseweb="input"] > div:focus-within {{
        border-color: {GOLD} !important;

        box-shadow:
            0 0 0 1px {GOLD} !important;
    }}

    input {{
        color: {TEXT} !important;
    }}


    /* ========================================================
       RADIO BUTTON
       ======================================================== */

    div[role="radiogroup"] {{
        gap: 10px !important;
    }}

    div[role="radiogroup"] label {{
        color: {TEXT} !important;
    }}


    /* ========================================================
       BUTTONS
       ======================================================== */

    .stButton > button {{
        width: 100% !important;

        min-height: 44px !important;

        background:
            linear-gradient(
                145deg,
                #151515,
                #090909
            ) !important;

        color: {TEXT} !important;

        border: 1px solid #454545 !important;

        border-radius: 8px !important;

        font-weight: 600 !important;

        transition:
            all 0.22s ease !important;
    }}

    .stButton > button:hover {{
        color: {GOLD_HIGHLIGHT} !important;

        border-color: {GOLD} !important;

        box-shadow:
            0 0 13px rgba(184, 134, 36, 0.24) !important;
    }}


    /* ========================================================
       ERGEBNIS
       ======================================================== */

    .result-title {{
        display: flex;
        align-items: center;
        justify-content: center;

        gap: 18px;

        margin-top: 8px;
        margin-bottom: 8px;

        color: {GOLD_LIGHT};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 22px;

        font-weight: 700;

        letter-spacing: 0.5px;

        text-transform: uppercase;

        text-align: center;
    }}

    .result-line {{
        width: 90px;

        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD}
            );
    }}

    .result-line-right {{
        background:
            linear-gradient(
                90deg,
                {GOLD},
                transparent
            );
    }}

    .result-lots {{
        margin-top: 18px;

        color: {GOLD_HIGHLIGHT};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: clamp(50px, 6vw, 76px);

        font-weight: 700;

        line-height: 1.05;

        letter-spacing: 0.5px;

        text-align: center;

        text-shadow:
            0 0 12px rgba(231, 193, 90, 0.28),
            0 0 30px rgba(184, 134, 36, 0.16);
    }}

    .result-units {{
        margin-top: 8px;
        margin-bottom: 25px;

        color: #D4D0C8;

        font-size: 21px;

        text-align: center;
    }}

    .result-divider {{
        height: 1px;

        margin: 16px 0;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(184, 134, 36, 0.28),
                transparent
            );
    }}

    .result-row {{
        display: flex;

        align-items: center;
        justify-content: space-between;

        padding: 12px 0;

        border-bottom:
            1px solid rgba(255, 255, 255, 0.07);

        color: {TEXT};

        font-size: 15px;
    }}

    .result-value {{
        color: {GOLD_LIGHT};

        font-weight: 600;

        text-align: right;
    }}

    .result-section {{
        margin-top: 27px;
        margin-bottom: 9px;

        color: {GOLD};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 19px;

        font-weight: 700;

        letter-spacing: 0.4px;

        text-transform: uppercase;
    }}


    /* ========================================================
       RISIKOÜBERSICHT
       ======================================================== */

    .risk-card {{
        margin-top: 25px;

        padding: 24px 28px;

        border: 1px solid {BORDER};
        border-radius: 15px;

        background:
            linear-gradient(
                145deg,
                rgba(17, 17, 17, 0.97),
                rgba(7, 7, 7, 0.99)
            );

        box-shadow:
            inset 0 0 25px rgba(255, 255, 255, 0.008);
    }}

    .risk-title {{
        color: {GOLD};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 20px;

        font-weight: 700;

        letter-spacing: 0.6px;

        text-transform: uppercase;

        margin-bottom: 16px;
    }}

    .risk-number {{
        color: {GOLD_LIGHT};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 28px;

        font-weight: 700;
    }}

    .risk-sub {{
        color: {TEXT_MUTED};

        font-size: 14px;

        margin-top: 2px;
    }}

    .risk-bar-background {{
        width: 100%;

        height: 11px;

        margin-top: 18px;

        border: 1px solid #343434;
        border-radius: 6px;

        background: #202020;

        overflow: hidden;
    }}

    .risk-bar {{
        height: 100%;

        border-radius: 5px;

        background:
            linear-gradient(
                90deg,
                {GOLD_DARK},
                {GOLD_LIGHT}
            );

        box-shadow:
            0 0 12px rgba(184, 134, 36, 0.30);
    }}

    .risk-percent {{
        margin-top: 8px;

        color: {GOLD_LIGHT};

        font-size: 14px;
    }}


    /* ========================================================
       RISIKOHINWEIS
       ======================================================== */

    .warning-card {{
        margin-top: 20px;

        padding: 20px 24px;

        border: 1px solid {GOLD_DEEP};
        border-radius: 14px;

        background:
            linear-gradient(
                145deg,
                rgba(23, 19, 10, 0.82),
                rgba(8, 8, 8, 0.97)
            );
    }}

    .warning-title {{
        color: {GOLD_LIGHT};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 19px;

        font-weight: 700;

        margin-bottom: 8px;
    }}

    .warning-text {{
        color: #D1CEC7;

        font-size: 13px;

        line-height: 1.65;
    }}


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 900px) {{

        .block-container {{
            padding-left: 1rem !important;
            padding-right: 1rem !important;
        }}

        .logo-frame img {{
            width: 290px;
            max-width: 80vw;
        }}

        .title-line {{
            display: none;
        }}

        .title-card {{
            padding-left: 18px;
            padding-right: 18px;
        }}

        .panel-card {{
            min-height: auto;
        }}

        .result-lots {{
            font-size: 55px;
        }}
    }}


    @media (max-width: 600px) {{

        .block-container {{
            padding-top: 0.75rem !important;
        }}

        .back-link {{
            padding: 10px 15px;

            font-size: 14px;
        }}

        .logo-frame img {{
            width: 240px;
            max-width: 82vw;
        }}

        .main-title {{
            font-size: 28px;

            letter-spacing: 1px;
        }}

        .subtitle {{
            font-size: 16px;
        }}

        .panel-card {{
            padding: 21px 18px;
        }}

        .result-lots {{
            font-size: 46px;
        }}

        .result-units {{
            font-size: 18px;
        }}

        .result-line {{
            display: none;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ZURÜCK ZUR STARTSEITE
# ============================================================

st.markdown(
    f"""
    <div class="back-area">
        <a
            class="back-link"
            href="{STARTSEITE_URL}"
            target="_self"
            rel="noopener"
        >
            <span class="back-arrow">←</span>
            <span>ZURÜCK ZUR STARTSEITE</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# COUNTORBREAK LOGO
# ============================================================

if os.path.exists(LOGO_FILE):
    st.markdown('<div class="logo-area">', unsafe_allow_html=True)

    st.markdown(
        '<div class="logo-frame">',
        unsafe_allow_html=True,
    )

    st.image(
        LOGO_FILE,
        width=330,
    )

    st.markdown('</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

else:
    st.warning(
        f"Die Datei '{LOGO_FILE}' wurde nicht gefunden. "
        "Bitte stelle sicher, dass sie im Repository neben app.py liegt."
    )


# ============================================================
# TITEL
# ============================================================

st.markdown(
    """
    <div class="title-card">

        <div class="title-row">

            <div class="title-line"></div>

            <div class="main-title">
                POSITIONSGRÖSSENRECHNER
            </div>

            <div class="title-line title-line-right"></div>

        </div>

        <div class="subtitle">
            Risk first. Profits second.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HAUPTBEREICH
# ============================================================

left, right = st.columns(
    [1, 1.45],
    gap="large",
)


# ============================================================
# LINKES PANEL
# TRADE-EINGABEN
# ============================================================

with left:

    st.markdown(
        """
        <div class="panel-card">

            <div class="panel-header">
                <span class="panel-header-symbol">⚖</span>
                <span>TRADE-EINGABEN</span>
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
            "XAU/USD",
            "US30",
            "NAS100",
            "GER40",
            "SPX500",
            "UK100",
        ],
        index=0,
    )

    direction = st.radio(
        "Richtung",
        [
            "↗ LONG",
            "↘ SHORT",
        ],
        horizontal=True,
    )

    account_size = st.number_input(
        "Kontogröße",
        min_value=0.0,
        value=10000.0,
        step=100.0,
        format="%.2f",
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

    leverage = st.number_input(
        "Hebel",
        min_value=1,
        max_value=1000,
        value=30,
        step=1,
    )


# ============================================================
# INSTRUMENT PARAMETER
# ============================================================

if instrument in [
    "EUR/USD",
    "GBP/USD",
    "AUD/USD",
    "NZD/USD",
]:

    contract_size = 100000
    pip_size = 0.0001
    pip_value_per_lot = 10.0

elif instrument == "USD/JPY":

    contract_size = 100000
    pip_size = 0.01
    pip_value_per_lot = 6.8

elif instrument in [
    "USD/CAD",
    "USD/CHF",
]:

    contract_size = 100000
    pip_size = 0.0001
    pip_value_per_lot = 7.2

elif instrument == "XAU/USD":

    contract_size = 100
    pip_size = 0.01
    pip_value_per_lot = 1.0

elif instrument in [
    "US30",
    "NAS100",
    "GER40",
    "SPX500",
    "UK100",
]:

    contract_size = 1
    pip_size = 1.0
    pip_value_per_lot = 1.0

else:

    contract_size = 100000
    pip_size = 0.0001
    pip_value_per_lot = 10.0


# ============================================================
# BERECHNUNG
# ============================================================

risk_amount = account_size * (risk_percent / 100.0)

stop_distance = abs(entry_price - stop_price)

if stop_distance <= 0:
    stop_distance = pip_size

stop_pips = stop_distance / pip_size

if stop_pips <= 0:
    stop_pips = 1.0

raw_lots = risk_amount / (
    stop_pips * pip_value_per_lot
)

raw_lots = max(0.0, raw_lots)

# Auf 0,01 Lot abrunden
lots_rounded = math.floor(
    raw_lots / 0.01
) * 0.01

if lots_rounded < 0.01:
    lots_rounded = 0.01

units = lots_rounded * contract_size

position_value = units * entry_price

if leverage > 0:
    margin = position_value / leverage
else:
    margin = position_value

free_margin = max(
    0.0,
    account_size - margin,
)

if account_size > 0:
    used_leverage = (
        position_value / account_size
    )
else:
    used_leverage = 0.0


# ============================================================
# RECHTES PANEL
# ERGEBNIS
# ============================================================

with right:

    st.markdown(
        """
        <div class="panel-card">

            <div class="panel-header">
                <span class="panel-header-symbol">◎</span>
                <span>ERGEBNIS</span>
            </div>

            <div class="result-title">

                <div class="result-line"></div>

                <div>
                    EMPFOHLENE POSITION
                </div>

                <div class="result-line result-line-right"></div>

            </div>

        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="result-lots">
            {lots_rounded:.2f} LOTS
        </div>

        <div class="result-units">
            = {units:,.0f} EINHEITEN
        </div>

        <div class="result-divider"></div>

        <div class="result-row">
            <span>Max. Verlust</span>
            <span class="result-value">
                {risk_amount:,.2f} {account_currency}
            </span>
        </div>

        <div class="result-row">
            <span>Stop-Abstand</span>
            <span class="result-value">
                {stop_pips:,.1f} Pips
            </span>
        </div>

        <div class="result-row">
            <span>Positionswert</span>
            <span class="result-value">
                {position_value:,.2f} {account_currency}
            </span>
        </div>

        <div class="result-row">
            <span>Pip-Wert</span>
            <span class="result-value">
                {pip_value_per_lot:,.2f} {account_currency}
            </span>
        </div>

        <div class="result-row">
            <span>Risikoprozent</span>
            <span class="result-value">
                {risk_percent:.2f} %
            </span>
        </div>

        <div class="result-section">
            MARGIN &amp; HEBEL
        </div>

        <div class="result-row">
            <span>Erforderliche Margin</span>
            <span class="result-value">
                {margin:,.2f} {account_currency}
            </span>
        </div>

        <div class="result-row">
            <span>Verwendeter Hebel</span>
            <span class="result-value">
                1 : {leverage}
            </span>
        </div>

        <div class="result-row">
            <span>Freie Margin (geschätzt)</span>
            <span class="result-value">
                {free_margin:,.2f} {account_currency}
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

risk_ratio = min(
    max(risk_percent / 5.0, 0.0),
    1.0,
)

risk_width = risk_ratio * 100.0

st.markdown(
    f"""
    <div class="risk-card">

        <div class="risk-title">
            RISIKOÜBERSICHT
        </div>

        <div class="risk-number">
            {risk_amount:,.2f} {account_currency}
        </div>

        <div class="risk-sub">
            von {account_size:,.2f} {account_currency}
        </div>

        <div class="risk-bar-background">
            <div
                class="risk-bar"
                style="width: {risk_width:.1f}%"
            ></div>
        </div>

        <div class="risk-percent">
            Risiko: {risk_percent:.2f} %
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
    <div class="warning-card">

        <div class="warning-title">
            ⚠ &nbsp; RISIKOHINWEIS
        </div>

        <div class="warning-text">
            CFDs sind komplexe Instrumente und bergen aufgrund
            der Hebelwirkung ein hohes Risiko, schnell Geld zu
            verlieren. 74–89 % der Kleinanlegerkonten verlieren
            Geld beim CFD-Handel mit diesem Anbieter.
            Überlegen Sie, ob Sie verstehen, wie CFDs
            funktionieren und ob Sie es sich leisten können,
            das hohe Risiko einzugehen, Ihr Geld zu verlieren.
        </div>

    </div>
    """,
    unsafe_allow_html=True,
)
