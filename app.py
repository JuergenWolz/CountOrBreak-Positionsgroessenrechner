import streamlit as st
import math


# ============================================================
# COUNT OR BREAK
# POSITIONSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    page_icon="🧮",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# KONFIGURATION
# ============================================================

STARTSEITE_URL = "https://countorbreak.streamlit.app"

GOLD = "#C99A2E"
GOLD_LIGHT = "#E4B84A"
GOLD_BRIGHT = "#FFD66B"
GOLD_DARK = "#9B7018"

BG = "#050505"
PANEL = "#0D0D0D"
PANEL_2 = "#111111"
BORDER = "#343434"
TEXT = "#F1F1F1"
TEXT_MUTED = "#B8B8B8"


# ============================================================
# CSS
# ============================================================

st.markdown(
    f"""
    <style>

    /* --------------------------------------------------------
       GLOBAL
    -------------------------------------------------------- */

    html, body, [class*="css"] {{
        font-family: "Arial", "Helvetica Neue", sans-serif;
    }}

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(201,154,46,0.10),
                transparent 32%
            ),
            #050505;
        color: {TEXT};
    }}

    .main {{
        background: transparent;
    }}

    .block-container {{
        max-width: 1450px;
        padding-top: 1.5rem;
        padding-bottom: 4rem;
        padding-left: 2rem;
        padding-right: 2rem;
    }}

    /* Streamlit Header entfernen */

    header[data-testid="stHeader"] {{
        background: transparent;
    }}

    /* --------------------------------------------------------
       ZURÜCK BUTTON
    -------------------------------------------------------- */

    .back-wrapper {{
        margin-bottom: 30px;
    }}

    .back-button {{
        display: inline-flex;
        align-items: center;
        gap: 10px;

        padding: 12px 20px;

        border: 1px solid {GOLD_DARK};
        border-radius: 9px;

        background:
            linear-gradient(
                145deg,
                rgba(25,25,25,0.98),
                rgba(8,8,8,0.98)
            );

        color: {GOLD};
        text-decoration: none;

        font-family: "Arial", sans-serif;
        font-size: 15px;
        font-weight: 700;
        letter-spacing: 1px;

        transition:
            all 0.22s ease;

        box-shadow:
            0 0 0 rgba(201,154,46,0);
    }}

    .back-button:hover {{
        color: {GOLD_BRIGHT};
        border-color: {GOLD_LIGHT};

        box-shadow:
            0 0 18px rgba(201,154,46,0.30),
            inset 0 0 15px rgba(201,154,46,0.06);

        transform: translateY(-1px);
    }}

    .back-arrow {{
        font-size: 20px;
        line-height: 1;
    }}


    /* --------------------------------------------------------
       LOGO BEREICH
    -------------------------------------------------------- */

    .brand-row {{
        display: flex;
        align-items: center;
        justify-content: center;

        gap: 35px;

        margin-top: 5px;
        margin-bottom: 28px;
    }}

    .brand-logo {{
        display: flex;
        align-items: center;
        justify-content: center;
    }}

    .brand-logo img {{
        width: 230px;
        max-width: 100%;
        height: auto;

        display: block;

        filter:
            drop-shadow(0 0 10px rgba(201,154,46,0.15));
    }}

    .calculator-logo {{
        width: 100px;
        height: 100px;

        display: flex;
        align-items: center;
        justify-content: center;

        border: 1px solid {GOLD_DARK};
        border-radius: 17px;

        background:
            radial-gradient(
                circle,
                rgba(201,154,46,0.10),
                rgba(0,0,0,0.65)
            );

        box-shadow:
            0 0 16px rgba(201,154,46,0.20),
            inset 0 0 20px rgba(201,154,46,0.05);
    }}

    .calculator-logo img {{
        width: 75px;
        height: 75px;
        object-fit: contain;

        filter:
            drop-shadow(0 0 8px rgba(201,154,46,0.35));
    }}


    /* --------------------------------------------------------
       TITEL
    -------------------------------------------------------- */

    .title-card {{
        position: relative;

        width: 100%;

        padding: 26px 35px 22px;

        margin-bottom: 25px;

        border: 1px solid {GOLD_DARK};
        border-radius: 14px;

        background:
            linear-gradient(
                145deg,
                rgba(24,24,24,0.96),
                rgba(7,7,7,0.98)
            );

        box-shadow:
            0 0 16px rgba(201,154,46,0.10),
            inset 0 0 25px rgba(255,255,255,0.015);

        text-align: center;

        overflow: hidden;
    }}

    .title-card::before {{
        content: "";
        position: absolute;

        left: 0;
        right: 0;
        top: 50%;

        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(201,154,46,0.45),
                transparent
            );

        z-index: 0;
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
            0 0 8px rgba(201,154,46,0.35);
    }}

    .title-line.right {{
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
            "Georgia",
            "Times New Roman",
            serif;

        font-size: clamp(28px, 4vw, 46px);

        font-weight: 700;

        letter-spacing: 2px;

        text-transform: uppercase;

        text-shadow:
            0 0 10px rgba(201,154,46,0.20);
    }}

    .subtitle {{
        position: relative;

        margin-top: 5px;

        color: #D7C18A;

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 20px;

        letter-spacing: 1px;

        z-index: 1;
    }}


    /* --------------------------------------------------------
       PANELS
    -------------------------------------------------------- */

    .panel {{
        position: relative;

        background:
            linear-gradient(
                145deg,
                rgba(19,19,19,0.97),
                rgba(7,7,7,0.99)
            );

        border: 1px solid {BORDER};

        border-radius: 15px;

        padding: 25px 28px;

        min-height: 720px;

        box-shadow:
            inset 0 0 30px rgba(255,255,255,0.008),
            0 8px 30px rgba(0,0,0,0.30);
    }}

    .panel:hover {{
        border-color: #4A4A4A;
    }}

    .panel-title {{
        display: flex;
        align-items: center;

        gap: 12px;

        margin-bottom: 28px;

        color: {GOLD};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 23px;

        font-weight: 600;

        letter-spacing: 0.7px;

        text-transform: uppercase;
    }}

    .panel-icon {{
        width: 28px;
        height: 28px;

        display: flex;
        align-items: center;
        justify-content: center;

        color: {GOLD};

        font-size: 22px;

        text-shadow:
            0 0 9px rgba(201,154,46,0.45);
    }}


    /* --------------------------------------------------------
       INPUT BEREICH
    -------------------------------------------------------- */

    .field-label {{
        color: {TEXT};

        font-size: 15px;

        margin-top: 15px;
        margin-bottom: 7px;
    }}

    div[data-baseweb="select"] > div {{
        background-color: #111111 !important;

        border: 1px solid #514421 !important;

        border-radius: 8px !important;

        color: {TEXT} !important;
    }}

    div[data-baseweb="select"] > div:hover {{
        border-color: {GOLD} !important;
    }}

    div[data-baseweb="input"] > div {{
        background-color: #111111 !important;

        border: 1px solid #514421 !important;

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

    /* --------------------------------------------------------
       RICHTUNG
    -------------------------------------------------------- */

    .direction-label {{
        color: {TEXT};

        font-size: 15px;

        margin-top: 15px;
        margin-bottom: 8px;
    }}

    .stButton > button {{
        width: 100%;

        min-height: 44px;

        background:
            linear-gradient(
                145deg,
                #141414,
                #0A0A0A
            ) !important;

        color: {TEXT} !important;

        border: 1px solid #444444 !important;

        border-radius: 8px !important;

        font-weight: 600 !important;

        transition:
            all 0.20s ease !important;
    }}

    .stButton > button:hover {{
        border-color: {GOLD} !important;

        color: {GOLD_LIGHT} !important;

        box-shadow:
            0 0 12px rgba(201,154,46,0.20) !important;
    }}


    /* --------------------------------------------------------
       ERGEBNIS
    -------------------------------------------------------- */

    .result-heading {{
        display: flex;
        align-items: center;

        gap: 12px;

        margin-bottom: 25px;

        color: {GOLD};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 23px;

        text-transform: uppercase;
    }}

    .result-title {{
        display: flex;
        align-items: center;
        justify-content: center;

        gap: 20px;

        margin-top: 15px;
        margin-bottom: 8px;

        color: {GOLD_LIGHT};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 23px;

        font-weight: 600;

        text-transform: uppercase;

        letter-spacing: 0.5px;
    }}

    .result-title-line {{
        width: 90px;
        height: 1px;

        background:
            linear-gradient(
                90deg,
                transparent,
                {GOLD}
            );
    }}

    .result-title-line.right {{
        background:
            linear-gradient(
                90deg,
                {GOLD},
                transparent
            );
    }}

    .result-lots {{
        text-align: center;

        margin-top: 18px;

        color: {GOLD_BRIGHT};

        font-family:
            "Arial",
            sans-serif;

        font-size: clamp(48px, 7vw, 76px);

        font-weight: 800;

        letter-spacing: -1px;

        text-shadow:
            0 0 10px rgba(255,214,107,0.35),
            0 0 28px rgba(201,154,46,0.20);
    }}

    .result-units {{
        text-align: center;

        color: #EAEAEA;

        font-size: 25px;

        margin-bottom: 25px;
    }}

    .result-divider {{
        height: 1px;

        margin: 15px 0;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(201,154,46,0.25),
                transparent
            );
    }}

    .result-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;

        padding: 13px 0;

        border-bottom: 1px solid rgba(255,255,255,0.08);

        color: {TEXT};

        font-size: 16px;
    }}

    .result-value {{
        color: {GOLD_LIGHT};

        font-weight: 600;

        text-align: right;
    }}

    .result-section {{
        margin-top: 28px;
        margin-bottom: 10px;

        color: {GOLD};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 20px;

        text-transform: uppercase;
    }}


    /* --------------------------------------------------------
       RISIKO ÜBERSICHT
    -------------------------------------------------------- */

    .risk-panel {{
        margin-top: 25px;

        padding: 25px 28px;

        border: 1px solid {BORDER};

        border-radius: 15px;

        background:
            linear-gradient(
                145deg,
                rgba(19,19,19,0.97),
                rgba(7,7,7,0.99)
            );
    }}

    .risk-title {{
        color: {GOLD};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 21px;

        text-transform: uppercase;

        margin-bottom: 18px;
    }}

    .risk-number {{
        color: {GOLD_LIGHT};

        font-size: 28px;

        font-weight: 700;
    }}

    .risk-sub {{
        color: {TEXT};

        font-size: 15px;
    }}


    /* --------------------------------------------------------
       RISIKOHINWEIS
    -------------------------------------------------------- */

    .warning {{
        margin-top: 20px;

        padding: 20px 24px;

        border: 1px solid {GOLD_DARK};

        border-radius: 14px;

        background:
            linear-gradient(
                145deg,
                rgba(24,20,10,0.85),
                rgba(8,8,8,0.96)
            );
    }}

    .warning-title {{
        color: {GOLD_LIGHT};

        font-family:
            "Georgia",
            "Times New Roman",
            serif;

        font-size: 20px;

        font-weight: 600;

        margin-bottom: 8px;
    }}

    .warning-text {{
        color: #D6D6D6;

        font-size: 14px;

        line-height: 1.6;
    }}


    /* --------------------------------------------------------
       RESPONSIVE
    -------------------------------------------------------- */

    @media (max-width: 900px) {{

        .block-container {{
            padding-left: 1rem;
            padding-right: 1rem;
        }}

        .brand-row {{
            gap: 20px;
        }}

        .brand-logo img {{
            width: 180px;
        }}

        .calculator-logo {{
            width: 80px;
            height: 80px;
        }}

        .calculator-logo img {{
            width: 60px;
            height: 60px;
        }}

        .title-line {{
            display: none;
        }}

        .panel {{
            min-height: auto;
        }}

        .result-lots {{
            font-size: 52px;
        }}
    }}

    @media (max-width: 600px) {{

        .brand-row {{
            gap: 12px;
        }}

        .brand-logo img {{
            width: 150px;
        }}

        .calculator-logo {{
            width: 68px;
            height: 68px;
        }}

        .calculator-logo img {{
            width: 50px;
            height: 50px;
        }}

        .main-title {{
            font-size: 27px;
        }}

        .subtitle {{
            font-size: 16px;
        }}

        .panel {{
            padding: 20px 18px;
        }}

        .result-lots {{
            font-size: 45px;
        }}

        .result-units {{
            font-size: 20px;
        }}
    }}

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# ZURÜCK ZUR STARTSEITE
# ============================================================

st.markdown(
    f"""
    <div class="back-wrapper">
        <a
            class="back-button"
            href="{STARTSEITE_URL}"
            target="_self"
        >
            <span class="back-arrow">←</span>
            <span>ZURÜCK ZUR STARTSEITE</span>
        </a>
    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOGO + RECHNER ICON
# ============================================================

st.markdown(
    """
    <div class="brand-row">

        <div class="brand-logo">
            <img
                src="logo.png"
                alt="CountOrBreak Logo"
            >
        </div>

        <div class="calculator-logo">
            <img
                src="rechner.png"
                alt="Positionsgrößenrechner"
            >
        </div>

    </div>
    """,
    unsafe_allow_html=True
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

            <div class="title-line right"></div>

        </div>

        <div class="subtitle">
            Risk first. Profits second.
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# HAUPTBEREICH
# ============================================================

left, right = st.columns([1, 1.45], gap="large")


# ============================================================
# LINKES PANEL – TRADE EINGABEN
# ============================================================

with left:

    st.markdown(
        """
        <div class="panel">

            <div class="panel-title">

                <div class="panel-icon">
                    ⚖
                </div>

                <div>
                    TRADE-EINGABEN
                </div>

            </div>

        </div>
        """,
        unsafe_allow_html=True
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
            "UK100"
        ],
        index=0
    )

    direction = st.radio(
        "Richtung",
        ["↗ LONG", "↘ SHORT"],
        horizontal=True
    )

    account_size = st.number_input(
        "Kontogröße",
        min_value=0.0,
        value=10000.0,
        step=100.0,
        format="%.2f"
    )

    risk_percent = st.number_input(
        "Risiko pro Trade",
        min_value=0.01,
        max_value=100.0,
        value=1.0,
        step=0.1,
        format="%.2f"
    )

    entry_price = st.number_input(
        "Einstiegskurs",
        min_value=0.00001,
        value=1.17000,
        step=0.00001,
        format="%.5f"
    )

    stop_price = st.number_input(
        "Stop-Loss Kurs",
        min_value=0.00001,
        value=1.16500,
        step=0.00001,
        format="%.5f"
    )

    account_currency = st.selectbox(
        "Kontowährung",
        ["EUR", "USD", "GBP", "CHF"],
        index=0
    )

    leverage = st.number_input(
        "Hebel",
        min_value=1,
        max_value=1000,
        value=30,
        step=1
    )

    # ========================================================
    # CFD PARAMETER
    # ========================================================

    if instrument in [
        "EUR/USD",
        "GBP/USD",
        "AUD/USD",
        "NZD/USD"
    ]:
        contract_size = 100000
        pip_size = 0.0001

        # Standard-FX-Pip-Wert pro Standard-Lot
        if instrument in ["EUR/USD", "GBP/USD", "AUD/USD", "NZD/USD"]:
            pip_value_per_lot = 10.0

    elif instrument in ["USD/JPY"]:
        contract_size = 100000
        pip_size = 0.01
        pip_value_per_lot = 6.8

    elif instrument in ["USD/CAD", "USD/CHF"]:
        contract_size = 100000
        pip_size = 0.0001
        pip_value_per_lot = 7.2

    elif instrument == "XAU/USD":
        contract_size = 100
        pip_size = 0.01
        pip_value_per_lot = 1.0

    elif instrument in ["US30", "NAS100", "GER40", "SPX500", "UK100"]:
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

    risk_amount = account_size * (risk_percent / 100)

    stop_distance = abs(entry_price - stop_price)

    if stop_distance <= 0:
        stop_distance = pip_size

    stop_pips = stop_distance / pip_size

    if stop_pips <= 0:
        stop_pips = 1

    lots = risk_amount / (stop_pips * pip_value_per_lot)

    # sinnvolle Begrenzung
    lots = max(0.0, lots)

    # Pepperstone typische Lotschritte
    lots_rounded = math.floor(lots / 0.01) * 0.01

    if lots_rounded < 0.01:
        lots_rounded = 0.01

    units = lots_rounded * contract_size

    position_value = units * entry_price

    margin = position_value / leverage

    free_margin = max(0.0, account_size - margin)

    used_leverage = (
        position_value / account_size
        if account_size > 0
        else 0
    )


# ============================================================
# RECHTES PANEL – ERGEBNIS
# ============================================================

with right:

    st.markdown(
        """
        <div class="panel">

            <div class="result-heading">

                <div class="panel-icon">
                    ◎
                </div>

                <div>
                    ERGEBNIS
                </div>

            </div>

            <div class="result-title">

                <div class="result-title-line"></div>

                <div>
                    EMPFOHLENE POSITION
                </div>

                <div class="result-title-line right"></div>

            </div>
        """,
        unsafe_allow_html=True
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
                ⚖ &nbsp; MARGIN &amp; HEBEL
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

        </div>
        """,
        unsafe_allow_html=True
    )


# ============================================================
# RISIKOÜBERSICHT
# ============================================================

risk_ratio = min(risk_percent / 5.0, 1.0)

st.markdown(
    f"""
    <div class="risk-panel">

        <div class="risk-title">
            🛡 &nbsp; RISIKOÜBERSICHT
        </div>

        <div class="risk-number">
            {risk_amount:,.2f} {account_currency}
        </div>

        <div class="risk-sub">
            von {account_size:,.2f} {account_currency}
        </div>

        <div style="
            margin-top:18px;
            height:12px;
            width:100%;
            border-radius:6px;
            background:#242424;
            overflow:hidden;
            border:1px solid #333333;
        ">

            <div style="
                width:{risk_ratio * 100:.1f}%;
                height:100%;
                background:linear-gradient(
                    90deg,
                    {GOLD_DARK},
                    {GOLD_LIGHT}
                );
                box-shadow:
                    0 0 12px rgba(201,154,46,0.35);
            ">
            </div>

        </div>

        <div style="
            margin-top:8px;
            color:{GOLD_LIGHT};
            font-size:14px;
        ">
            Risiko: {risk_percent:.2f} %
        </div>

    </div>
    """,
    unsafe_allow_html=True
)


# ============================================================
# RISIKOHINWEIS
# ============================================================

st.markdown(
    """
    <div class="warning">

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
    unsafe_allow_html=True
)


# ============================================================
# ENDE
# ============================================================
