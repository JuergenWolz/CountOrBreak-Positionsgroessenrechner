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
# COUNTORBREAK FARBEN
# ============================================================

GOLD_DARK = "#8C6515"
GOLD = "#B88322"
GOLD_MAIN = "#C99A2E"
GOLD_LIGHT = "#D7B35A"
GOLD_BRIGHT = "#F1D27A"

BACKGROUND = "#050505"
PANEL = "#0D0D0D"
BORDER = "#352A18"
TEXT = "#F1F1F1"
MUTED = "#B7B7B7"


# ============================================================
# DESIGN
# ============================================================
#
# WICHTIG:
# Der sichtbare Seiteninhalt wird bewusst NICHT mit HTML
# aufgebaut. Überschriften, Logo und Buttons sind native
# Streamlit-Komponenten.
#
# Dadurch können keine <div>, <span> usw. als sichtbarer Text
# auf der Seite erscheinen.
# ============================================================

st.markdown(
    f"""
    <style>

    .stApp {{
        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(201, 154, 46, 0.075),
                transparent 34%
            ),
            {BACKGROUND};

        color: {TEXT};
    }}

    .block-container {{
        max-width: 1400px !important;
        padding-top: 1.2rem !important;
        padding-bottom: 4rem !important;
        padding-left: 2rem !important;
        padding-right: 2rem !important;
    }}

    header[data-testid="stHeader"] {{
        background: transparent !important;
    }}


    /* ========================================================
       ALLGEMEINE SCHRIFT
       ======================================================== */

    html,
    body,
    [class*="css"] {{
        font-family:
            Georgia,
            "Times New Roman",
            serif;
    }}


    /* ========================================================
       ZURÜCK-BUTTON
       ======================================================== */

    div[data-testid="stLinkButton"] a {{
        color: {GOLD_MAIN} !important;
        background: #090909 !important;

        border: 1px solid {GOLD_DARK} !important;
        border-radius: 9px !important;

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        font-size: 15px !important;
        font-weight: 700 !important;

        letter-spacing: 0.7px !important;

        transition:
            color 0.2s ease,
            border-color 0.2s ease,
            box-shadow 0.2s ease,
            transform 0.2s ease !important;
    }}

    div[data-testid="stLinkButton"] a:hover {{
        color: {GOLD_BRIGHT} !important;
        border-color: {GOLD_LIGHT} !important;

        box-shadow:
            0 0 18px rgba(201,154,46,0.30),
            inset 0 0 12px rgba(201,154,46,0.05) !important;

        transform: translateY(-1px) !important;
    }}


    /* ========================================================
       LOGO
       ======================================================== */

    div[data-testid="stImage"] {{
        display: flex;
        justify-content: center;
    }}

    div[data-testid="stImage"] img {{
        filter:
            drop-shadow(
                0 0 12px rgba(201,154,46,0.18)
            );
    }}


    /* ========================================================
       TITEL
       ======================================================== */

    h1 {{
        color: {GOLD_MAIN} !important;

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        font-size: clamp(29px, 4vw, 46px) !important;
        font-weight: 700 !important;

        letter-spacing: 1.7px !important;

        text-align: center !important;
        text-transform: uppercase !important;

        text-shadow:
            0 0 10px rgba(201,154,46,0.20);
    }}

    h3 {{
        color: {GOLD_MAIN} !important;

        font-family:
            Georgia,
            "Times New Roman",
            serif !important;

        font-size: 21px !important;
        font-weight: 700 !important;

        letter-spacing: 0.7px !important;
        text-transform: uppercase !important;
    }}


    /* ========================================================
       TEXT / LABELS
       ======================================================== */

    p,
    label {{
        color: {TEXT};
    }}

    div[data-testid="stMarkdownContainer"] p {{
        color: {TEXT};
    }}


    /* ========================================================
       PANELS
       ======================================================== */

    div[data-testid="stVerticalBlockBorderWrapper"] {{
        background:
            linear-gradient(
                145deg,
                rgba(18,18,18,0.98),
                rgba(7,7,7,0.99)
            ) !important;

        border:
            1px solid {BORDER} !important;

        border-radius: 14px !important;

        box-shadow:
            inset 0 0 24px rgba(255,255,255,0.008);
    }}


    /* ========================================================
       EINGABEFELDER
       ======================================================== */

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

        box-shadow:
            0 0 0 1px rgba(201,154,46,0.16) !important;
    }}

    div[data-testid="stRadio"] label,
    div[data-testid="stRadio"] label p {{
        color: {TEXT} !important;
    }}


    /* ========================================================
       ERGEBNIS
       ======================================================== */

    .cb-result-label {{
        color: {GOLD_MAIN};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 20px;
        font-weight: 700;

        text-align: center;
        text-transform: uppercase;

        letter-spacing: 0.65px;
    }}

    .cb-result-lots {{
        color: {GOLD_BRIGHT};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: clamp(48px, 6vw, 74px);
        font-weight: 700;

        line-height: 1;

        text-align: center;

        margin: 0.55rem 0 0.25rem;

        text-shadow:
            0 0 11px rgba(241,210,122,0.30),
            0 0 25px rgba(201,154,46,0.15);
    }}

    .cb-result-units {{
        color: #DDDDDD;

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 19px;

        text-align: center;

        margin-bottom: 1rem;
    }}


    /* ========================================================
       GOLDENE TRENNLINIE
       ======================================================== */

    hr {{
        border: none !important;
        height: 1px !important;

        background:
            linear-gradient(
                90deg,
                transparent,
                rgba(201,154,46,0.40),
                transparent
            ) !important;

        margin: 0.9rem 0 !important;
    }}


    /* ========================================================
       ERGEBNISWERTE
       ======================================================== */

    .cb-value {{
        color: {GOLD_LIGHT};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-weight: 600;
    }}

    .cb-section-title {{
        color: {GOLD_MAIN};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 18px;
        font-weight: 700;

        letter-spacing: 0.55px;
        text-transform: uppercase;
    }}


    /* ========================================================
       RISIKO
       ======================================================== */

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
            0 0 10px rgba(201,154,46,0.28);
    }}


    /* ========================================================
       HINWEIS
       ======================================================== */

    .cb-warning-title {{
        color: {GOLD_MAIN};

        font-family:
            Georgia,
            "Times New Roman",
            serif;

        font-size: 18px;
        font-weight: 700;

        letter-spacing: 0.5px;
        text-transform: uppercase;
    }}

    .cb-warning-text {{
        color: #D0D0D0;

        font-size: 14px;
        line-height: 1.65;
    }}


    /* ========================================================
       MOBIL
       ======================================================== */

    @media (max-width: 700px) {{

        .block-container {{
            padding-left: 0.85rem !important;
            padding-right: 0.85rem !important;
        }}

        h1 {{
            font-size: 27px !important;
            letter-spacing: 1px !important;
        }}

        .cb-result-lots {{
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

st.link_button(
    "←  ZURÜCK ZUR STARTSEITE",
    STARTSEITE_URL,
)

st.write("")


# ============================================================
# COUNTORBREAK LOGO
# ============================================================

if LOGO_PATH.is_file():

    logo_left, logo_center, logo_right = st.columns(
        [1, 2, 1],
        vertical_alignment="center",
    )

    with logo_center:
        st.image(
            str(LOGO_PATH),
            width=250,
        )

else:

    st.error(
        "countorbreak_logo.png wurde nicht gefunden. "
        "Die Datei muss direkt neben app.py liegen."
    )


# ============================================================
# HEADER
# ============================================================
#
# ABSICHTLICH native Streamlit-Komponenten.
# Kein <div>, kein <span>, kein HTML-Header.
# ============================================================

st.title("POSITIONSGRÖSSENRECHNER")

st.caption("Risk first. Profits second.")

st.divider()

st.write("")


# ============================================================
# TRADE-EINGABEN
# ============================================================

left, right = st.columns(
    [1, 1.45],
    gap="large",
)


with left:

    with st.container(border=True):

        st.subheader("⚖  TRADE-EINGABEN")

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
            [
                "LONG",
                "SHORT",
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

stop_distance = abs(
    entry_price - stop_price
)

if stop_distance <= 0:
    stop_distance = pip_size

stop_pips = stop_distance / pip_size

if stop_pips <= 0:
    stop_pips = 1.0

lots_raw = (
    risk_amount
    / (
        stop_pips
        * pip_value_per_lot
    )
)

lots_rounded = (
    math.floor(
        lots_raw / 0.01
    )
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

        st.subheader("◎  ERGEBNIS")

        st.markdown(
            '<div class="cb-result-label">'
            'EMPFOHLENE POSITION'
            '</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="cb-result-lots">'
            f'{lots_rounded:.2f} LOTS'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.markdown(
            f'<div class="cb-result-units">'
            f'= {units:,.0f} EINHEITEN'
            f'</div>',
            unsafe_allow_html=True,
        )

        st.divider()

        result_rows = [
            (
                "Richtung",
                direction,
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

        for label, value in result_rows:

            row_left, row_right = st.columns(
                [1.15, 1]
            )

            with row_left:
                st.write(label)

            with row_right:
                st.markdown(
                    f'<div class="cb-value">{value}</div>',
                    unsafe_allow_html=True,
                )

        st.markdown(
            '<div class="cb-section-title">'
            '⚖  MARGIN &amp; HEBEL'
            '</div>',
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

            row_left, row_right = st.columns(
                [1.15, 1]
            )

            with row_left:
                st.write(label)

            with row_right:
                st.markdown(
                    f'<div class="cb-value">{value}</div>',
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

    st.subheader("🛡  RISIKOÜBERSICHT")

    st.markdown(
        f'<div class="cb-risk-number">'
        f'{risk_amount:,.2f} {account_currency}'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="cb-muted">'
        f'von {account_size:,.2f} {account_currency}'
        f'</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        f"""
        <div class="cb-risk-track">
            <div
                class="cb-risk-fill"
                style="width:{risk_ratio * 100:.1f}%"
            ></div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.markdown(
        f'<div class="cb-muted">'
        f'Risiko: {risk_percent:.2f} %'
        f'</div>',
        unsafe_allow_html=True,
    )


# ============================================================
# RISIKOHINWEIS
# ============================================================

with st.container(border=True):

    st.markdown(
        '<div class="cb-warning-title">'
        '⚠  RISIKOHINWEIS'
        '</div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        """
        <div class="cb-warning-text">
            CFDs sind komplexe Instrumente und bergen aufgrund
            der Hebelwirkung ein hohes Risiko, schnell Geld zu
            verlieren. Überlegen Sie, ob Sie verstehen, wie CFDs
            funktionieren und ob Sie es sich leisten können,
            das hohe Risiko einzugehen, Ihr Geld zu verlieren.
        </div>
        """,
        unsafe_allow_html=True,
    )
