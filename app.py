import math
from pathlib import Path

import streamlit as st


# ============================================================
# COUNT OR BREAK
# POSITIONSGRÖSSENRECHNER
# ============================================================

st.set_page_config(
    page_title="CountOrBreak – Positionsgrößenrechner",
    layout="wide",
    initial_sidebar_state="collapsed",
)


# ============================================================
# DATEIEN
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
LOGO_PATH = BASE_DIR / "countorbreak_logo.png"

STARTSEITE_URL = "https://countorbreak.streamlit.app"


# ============================================================
# COUNTORBREAK GOLD
# ============================================================

GOLD_DARK = "#8C6515"
GOLD = "#B88322"
GOLD_MAIN = "#C99A2E"
GOLD_LIGHT = "#D7B35A"
GOLD_BRIGHT = "#F1D27A"

BG = "#050505"
PANEL = "#0D0D0D"
BORDER = "#352A18"
TEXT = "#F1F1F1"
MUTED = "#B7B7B7"


# ============================================================
# STYLING
# ============================================================

st.markdown(
    f"""
<style>
.stApp {{
    background:
        radial-gradient(
            circle at 50% 0%,
            rgba(201,154,46,0.075),
            transparent 34%
        ),
        {BG};
    color: {TEXT};
}}

.block-container {{
    max-width: 1400px !important;
    padding: 1.2rem 2rem 4rem !important;
}}

header[data-testid="stHeader"] {{
    background: transparent !important;
}}


/* ---------------- ZURÜCK ---------------- */

.cb-back {{
    display: inline-flex;
    align-items: center;
    gap: 9px;

    padding: 10px 17px;

    border: 1px solid {GOLD_DARK};
    border-radius: 9px;

    background: #090909;

    color: {GOLD_MAIN} !important;
    text-decoration: none !important;

    font-family: Georgia, "Times New Roman", serif;
    font-size: 15px;
    font-weight: 700;
    letter-spacing: .7px;

    transition:
        color .2s ease,
        border-color .2s ease,
        box-shadow .2s ease,
        transform .2s ease;
}}

.cb-back:hover {{
    color: {GOLD_BRIGHT} !important;
    border-color: {GOLD_LIGHT};

    box-shadow:
        0 0 18px rgba(201,154,46,.30),
        inset 0 0 12px rgba(201,154,46,.05);

    transform: translateY(-1px);
}}


/* ---------------- LOGO ---------------- */

.cb-logo {{
    display: flex;
    justify-content: center;
    align-items: center;

    width: 100%;
    margin: 18px 0 20px;
}}

.cb-logo img {{
    display: block;
    width: 250px;
    max-width: 72vw;
    height: auto;

    filter:
        drop-shadow(0 0 12px rgba(201,154,46,.18));
}}


/* ---------------- TITEL ---------------- */

.cb-title-card {{
    width: 100%;
    box-sizing: border-box;

    padding: 1.35rem 1.4rem 1.25rem;

    border: 1px solid {GOLD_DARK};
    border-radius: 14px;

    background:
        linear-gradient(
            145deg,
            rgba(21,21,21,.97),
            rgba(7,7,7,.99)
        );

    box-shadow:
        0 0 20px rgba(140,101,21,.08);
}}

.cb-line {{
    height: 1px;
    width: 100%;

    margin: .2rem auto .75rem;

    background:
        linear-gradient(
            90deg,
            transparent,
            {GOLD_DARK},
            {GOLD_MAIN},
            {GOLD_DARK},
            transparent
        );
}}

.cb-title {{
    color: {GOLD_MAIN};

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: clamp(29px, 4vw, 46px);
    font-weight: 700;

    text-align: center;
    text-transform: uppercase;

    letter-spacing: 1.7px;

    text-shadow:
        0 0 10px rgba(201,154,46,.20);
}}

.cb-subtitle {{
    color: #D3BC87;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 18px;

    text-align: center;
    letter-spacing: .75px;

    margin-top: .45rem;
}}


/* ---------------- STREAMLIT PANELS ---------------- */

div[data-testid="stVerticalBlockBorderWrapper"] {{
    background:
        linear-gradient(
            145deg,
            rgba(18,18,18,.98),
            rgba(7,7,7,.99)
        ) !important;

    border: 1px solid {BORDER} !important;
    border-radius: 14px !important;

    box-shadow:
        inset 0 0 24px rgba(255,255,255,.008);
}}

.cb-panel-title {{
    color: {GOLD_MAIN};

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 21px;
    font-weight: 700;

    letter-spacing: .7px;
    text-transform: uppercase;

    margin-bottom: 1rem;
}}


/* ---------------- EINGABEN ---------------- */

label {{
    color: {TEXT} !important;
}}

div[data-baseweb="select"] > div {{
    background: #111111 !important;
    border-color: #4B3C1E !important;
}}

div[data-baseweb="select"] > div:hover {{
    border-color: {GOLD} !important;
}}

div[data-baseweb="select"] * {{
    color: {TEXT} !important;
}}

div[data-testid="stNumberInput"] input {{
    color: {TEXT} !important;
    background: #111111 !important;
}}

div[data-testid="stNumberInput"] > div {{
    border-color: #4B3C1E !important;
}}

div[data-testid="stNumberInput"] > div:focus-within {{
    border-color: {GOLD} !important;
    box-shadow: 0 0 0 1px rgba(201,154,46,.16) !important;
}}

div[data-testid="stRadio"] label,
div[data-testid="stRadio"] label p {{
    color: {TEXT} !important;
}}


/* ---------------- ERGEBNIS ---------------- */

.cb-result-caption {{
    color: {GOLD_MAIN};

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 20px;
    font-weight: 700;

    text-align: center;
    text-transform: uppercase;

    letter-spacing: .65px;
}}

.cb-lots {{
    color: {GOLD_BRIGHT};

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: clamp(48px, 6vw, 74px);
    font-weight: 700;

    line-height: 1;

    text-align: center;

    margin: .55rem 0 .25rem;

    text-shadow:
        0 0 11px rgba(241,210,122,.30),
        0 0 25px rgba(201,154,46,.15);
}}

.cb-units {{
    color: #DDDDDD;

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 19px;

    text-align: center;

    margin-bottom: 1rem;
}}

.cb-divider {{
    height: 1px;
    margin: .9rem 0;

    background:
        linear-gradient(
            90deg,
            transparent,
            rgba(201,154,46,.35),
            transparent
        );
}}

.cb-row {{
    display: flex;
    justify-content: space-between;
    gap: 20px;

    padding: .55rem 0;

    border-bottom:
        1px solid rgba(255,255,255,.065);

    color: {TEXT};

    font-size: 15px;
}}

.cb-value {{
    color: {GOLD_LIGHT};

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-weight: 600;
    text-align: right;
}}

.cb-section {{
    color: {GOLD_MAIN};

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 18px;
    font-weight: 700;

    letter-spacing: .55px;
    text-transform: uppercase;

    margin: 1.15rem 0 .35rem;
}}


/* ---------------- RISIKO ---------------- */

.cb-risk-number {{
    color: {GOLD_LIGHT};

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 29px;
    font-weight: 700;
}}

.cb-muted {{
    color: {MUTED};
    font-size: 14px;
}}

.cb-risk-track {{
    width: 100%;
    height: 10px;

    margin-top: 14px;

    background: #222222;
    border: 1px solid #333333;

    border-radius: 6px;

    overflow: hidden;
}}

.cb-risk-fill {{
    height: 100%;

    background:
        linear-gradient(
            90deg,
            {GOLD_DARK},
            {GOLD_MAIN},
            {GOLD_LIGHT}
        );

    box-shadow:
        0 0 10px rgba(201,154,46,.28);
}}


/* ---------------- HINWEIS ---------------- */

.cb-warning-title {{
    color: {GOLD_MAIN};

    font-family:
        Georgia,
        "Times New Roman",
        serif;

    font-size: 18px;
    font-weight: 700;

    letter-spacing: .5px;
    text-transform: uppercase;
}}

.cb-warning {{
    color: #D0D0D0;

    font-size: 14px;
    line-height: 1.65;
}}


/* ---------------- MOBIL ---------------- */

@media (max-width: 700px) {{
    .block-container {{
        padding-left: .85rem !important;
        padding-right: .85rem !important;
    }}

    .cb-logo img {{
        width: 205px;
    }}

    .cb-title-card {{
        padding: 1.1rem .75rem 1rem;
    }}

    .cb-title {{
        font-size: 26px;
        letter-spacing: 1px;
    }}

    .cb-subtitle {{
        font-size: 16px;
    }}

    .cb-lots {{
        font-size: 46px;
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
    <a class="cb-back" href="{STARTSEITE_URL}" target="_self">
        ←&nbsp;&nbsp;ZURÜCK ZUR STARTSEITE
    </a>
    """,
    unsafe_allow_html=True,
)

st.write("")


# ============================================================
# LOGO
# ============================================================

if LOGO_PATH.is_file():

    st.markdown('<div class="cb-logo">', unsafe_allow_html=True)

    st.image(
        str(LOGO_PATH),
        width=250,
    )

    st.markdown("</div>", unsafe_allow_html=True)

else:

    st.error(
        "Das Logo wurde nicht gefunden. "
        "Die Datei countorbreak_logo.png muss direkt "
        "neben app.py liegen."
    )


# ============================================================
# HEADER
# ============================================================

st.markdown(
    """
    <div class="cb-title-card">

        <div class="cb-line"></div>

        <div class="cb-title">
            POSITIONSGRÖSSENRECHNER
        </div>

        <div class="cb-subtitle">
            Risk first. Profits second.
        </div>

        <div class="cb-line"></div>

    </div>
    """,
    unsafe_allow_html=True,
)

st.write("")


# ============================================================
# EINGABEN
# ============================================================

left, right = st.columns(
    [1, 1.45],
    gap="large",
)


with left:

    with st.container(border=True):

        st.markdown(
            '<div class="cb-panel-title">⚖ &nbsp; TRADE-EINGABEN</div>',
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
        )

        direction = st.radio(
            "Richtung",
            ["↗ LONG", "↘ SHORT"],
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
            ["EUR", "USD", "GBP", "CHF"],
        )

        leverage = st.number_input(
            "Hebel",
            min_value=1,
            max_value=1000,
            value=30,
            step=1,
        )


# ============================================================
# CFD-PARAMETER
# ============================================================

if instrument in {
    "EUR/USD",
    "GBP/USD",
    "AUD/USD",
    "NZD/USD",
}:
    contract_size = 100000
    pip_size = 0.0001
    pip_value_per_lot = 10.0

elif instrument == "USD/JPY":
    contract_size = 100000
    pip_size = 0.01
    pip_value_per_lot = 6.8

elif instrument in {
    "USD/CAD",
    "USD/CHF",
}:
    contract_size = 100000
    pip_size = 0.0001
    pip_value_per_lot = 7.2

elif instrument == "XAU/USD":
    contract_size = 100
    pip_size = 0.01
    pip_value_per_lot = 1.0

else:
    contract_size = 1
    pip_size = 1.0
    pip_value_per_lot = 1.0


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

lots_raw = risk_amount / (stop_pips * pip_value_per_lot)

lots_rounded = (
    math.floor(lots_raw / 0.01)
    * 0.01
)

if risk_amount <= 0:
    lots_rounded = 0.0

units = lots_rounded * contract_size

position_value = units * entry_price

margin = (
    position_value / leverage
    if leverage > 0
    else 0.0
)

free_margin = max(
    0.0,
    account_size - margin,
)


# ============================================================
# ERGEBNIS
# ============================================================

with right:

    with st.container(border=True):

        st.markdown(
            '<div class="cb-panel-title">◎ &nbsp; ERGEBNIS</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="cb-result-caption">'
            'EMPFOHLENE POSITION'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="cb-lots">'
            f'{lots_rounded:.2f} LOTS'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="cb-units">'
            f'= {units:,.0f} EINHEITEN'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            '<div class="cb-divider"></div>',
            unsafe_allow_html=True,
        )

        rows = [
            (
                "Richtung",
                direction.replace("↗ ", "").replace("↘ ", ""),
            ),
            (
                "Max. Verlust",
                f"{risk_amount:,.2f} {account_currency}",
            ),
            (
                "Stop-Abstand",
                f"{stop_pips:,.1f} Pips",
            ),
            (
                "Positionswert",
                f"{position_value:,.2f} {account_currency}",
            ),
            (
                "Pip-Wert / Lot",
                f"{pip_value_per_lot:,.2f}",
            ),
            (
                "Risiko",
                f"{risk_percent:.2f} %",
            ),
        ]

        for label, value in rows:

            st.markdown(
                f"""
                <div class="cb-row">
                    <span>{label}</span>
                    <span class="cb-value">{value}</span>
                </div>
                """,
                unsafe_allow_html=True,
            )

        st.markdown(
            '<div class="cb-section">⚖ &nbsp; MARGIN &amp; HEBEL</div>',
            unsafe_allow_html=True,
        )

        margin_rows = [
            (
                "Erforderliche Margin",
                f"{margin:,.2f} {account_currency}",
            ),
            (
                "Hebel",
                f"1 : {leverage}",
            ),
            (
                "Freie Margin",
                f"{free_margin:,.2f} {account_currency}",
            ),
        ]

        for label, value in margin_rows:

            st.markdown(
                f"""
                <div class="cb-row">
                    <span>{label}</span>
                    <span class="cb-value">{value}</span>
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

with st.container(border=True):

    st.markdown(
        '<div class="cb-panel-title">🛡 &nbsp; RISIKOÜBERSICHT</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="cb-risk-number">
            {risk_amount:,.2f} {account_currency}
        </div>

        <div class="cb-muted">
            von {account_size:,.2f} {account_currency}
        </div>

        <div class="cb-risk-track">
            <div
                class="cb-risk-fill"
                style="width:{risk_ratio * 100:.1f}%"
            ></div>
        </div>

        <div class="cb-muted" style="margin-top:7px;">
            Risiko: {risk_percent:.2f} %
        </div>
        """,
        unsafe_allow_html=True,
    )


# ============================================================
# RISIKOHINWEIS
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="cb-warning-title">⚠ &nbsp; RISIKOHINWEIS</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="cb-warning">
            CFDs sind komplexe Instrumente und bergen aufgrund
            der Hebelwirkung ein hohes Risiko, schnell Geld zu
            verlieren. Überlegen Sie, ob Sie verstehen, wie CFDs
            funktionieren und ob Sie es sich leisten können,
            das hohe Risiko einzugehen, Ihr Geld zu verlieren.
        </div>
        """,
        unsafe_allow_html=True,
    )
