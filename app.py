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

BASE_PATH = Path(__file__).parent


def find_asset(possible_names):
    """
    Sucht nach einem Bild unter mehreren möglichen Dateinamen.
    Dadurch funktioniert die App auch dann, wenn das hochgeladene
    Icon leicht anders benannt wurde.
    """
    for name in possible_names:
        path = BASE_PATH / name
        if path.exists():
            return path

    return None


logo_path = find_asset([
    "countorbreak_logo.png",
    "CountOrBreak_logo.png",
    "logo.png",
    "Logo.png",
])

calculator_path = find_asset([
    "icon_rechner.png",
    "rechner.png",
    "calculator.png",
    "positionsgroessenrechner.png",
    "positionsgrößenrechner.png",
])


# ============================================================
# BILD → BASE64
# ============================================================

def image_to_base64(path):
    if path is None or not path.exists():
        return None

    return base64.b64encode(path.read_bytes()).decode("utf-8")


logo_data = image_to_base64(logo_path)
calculator_data = image_to_base64(calculator_path)


# ============================================================
# CSS
# ============================================================

st.markdown(
    """
    <style>

    /* ========================================================
       FARBPALETTE
       ======================================================== */

    :root {
        --gold-main: #C9A35A;
        --gold-light: #D8B66A;
        --gold-bright: #E8CB87;
        --gold-dark: #76521A;
        --gold-border: #A77D35;

        --background: #040404;
        --panel: #0A0A0A;
        --panel-2: #101010;

        --text: #F0E6D2;
        --muted: #AAA197;

        --green: #86B85C;
        --red: #C66B61;
    }


    /* ========================================================
       HAUPTSEITE
       ======================================================== */

    .stApp {

        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(201, 163, 90, 0.085),
                transparent 32%
            ),

            radial-gradient(
                circle at 50% 55%,
                rgba(130, 88, 23, 0.025),
                transparent 50%
            ),

            #040404;

        color: var(--text);
    }


    .block-container {

        max-width: 1450px;

        padding-top: 1.5rem;
        padding-bottom: 3rem;
    }


    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }


    /* ========================================================
       HEADER
       ======================================================== */

    .cb-header {

        width: 100%;

        display: flex;

        align-items: center;

        justify-content: space-between;

        margin-bottom: 18px;
    }


    .cb-brand {

        display: flex;

        align-items: center;

        gap: 22px;
    }


    .cb-brand-icon {

        width: 82px;

        height: 82px;

        display: flex;

        align-items: center;

        justify-content: center;

        border: 1px solid rgba(167, 125, 53, 0.75);

        border-radius: 18px;

        background:
            linear-gradient(
                145deg,
                rgba(24, 24, 24, 0.98),
                rgba(5, 5, 5, 0.98)
            );

        box-shadow:
            inset 0 0 20px
            rgba(201, 163, 90, 0.035),

            0 0 12px
            rgba(201, 163, 90, 0.09);
    }


    .cb-brand-icon img {

        width: 62px;

        height: 62px;

        object-fit: contain;

        filter:
            drop-shadow(
                0 0 8px
                rgba(201, 163, 90, 0.22)
            );
    }


    .cb-brand-fallback {

        color: var(--gold-light);

        font-size: 42px;

        line-height: 1;
    }


    .cb-title-main {

        color: var(--gold-light);

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            "Palatino Linotype",
            "Book Antiqua",
            Palatino,
            Georgia,
            serif;

        font-size: clamp(30px, 4vw, 52px);

        font-weight: 500;

        letter-spacing: 0.075em;

        line-height: 1.05;

        text-shadow:
            0 0 8px
            rgba(201, 163, 90, 0.20),

            0 0 22px
            rgba(201, 163, 90, 0.08);
    }


    .cb-title-sub {

        color: #CFC5B5;

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            "Palatino Linotype",
            Georgia,
            serif;

        font-size: clamp(14px, 1.5vw, 21px);

        letter-spacing: 0.18em;

        margin-top: 7px;

        text-transform: uppercase;
    }


    /* ========================================================
       ANLEITUNG
       ======================================================== */

    .cb-info-box {

        display: inline-flex;

        align-items: center;

        gap: 9px;

        padding: 12px 18px;

        border: 1px solid
            rgba(167, 125, 53, 0.72);

        border-radius: 8px;

        color: var(--gold-light);

        background:
            rgba(10, 10, 10, 0.82);

        font-family:
            "Baskerville",
            Georgia,
            serif;

        font-size: 15px;

        letter-spacing: 0.05em;
    }


    /* ========================================================
       TRENNLINIE
       ======================================================== */

    .cb-line {

        height: 1px;

        width: 100%;

        margin: 10px 0 27px 0;

        background:
            linear-gradient(
                90deg,
                transparent,
                #594016,
                #A77D35,
                #D8B66A,
                #A77D35,
                #594016,
                transparent
            );

        box-shadow:
            0 0 10px
            rgba(201, 163, 90, 0.22);
    }


    /* ========================================================
       HAUPTCONTAINER
       ======================================================== */

    .cb-main-shell {

        width: 100%;

        border:
            1px solid
            rgba(167, 125, 53, 0.72);

        border-radius: 12px;

        padding: 26px;

        background:
            linear-gradient(
                135deg,
                rgba(13, 13, 13, 0.98),
                rgba(5, 5, 5, 0.99)
            );

        box-shadow:

            inset
            0 0 45px
            rgba(201, 163, 90, 0.025),

            0 14px 45px
            rgba(0, 0, 0, 0.55);
    }


    /* ========================================================
       SECTION TITEL
       ======================================================== */

    .cb-section-title {

        color: var(--gold-light);

        font-family:
            "Baskerville",
            "Baskerville Old Face",
            "Palatino Linotype",
            Georgia,
            serif;

        font-size: 23px;

        font-weight: 500;

        letter-spacing: 0.065em;

        margin-bottom: 13px;

        text-shadow:
            0 0 8px
            rgba(201, 163, 90, 0.15);
    }


    .cb-section-divider {

        width: 100%;

        height: 1px;

        margin: 18px 0 23px 0;

        background:
            linear-gradient(
                90deg,
                rgba(167,125,53,0.55),
                rgba(167,125,53,0.08)
            );
    }


    /* ========================================================
       STREAMLIT INPUTS
       ======================================================== */

    div[data-baseweb="select"] > div {

        background:
            linear-gradient(
                145deg,
                #121212,
                #080808
            ) !important;

        border:
            1px solid
            rgba(167, 125, 53, 0.58) !important;

        border-radius: 7px !important;

        color: var(--text) !important;
    }


    div[data-baseweb="input"] {

        background: transparent !important;
    }


    div[data-baseweb="input"] > div {

        background:
            linear-gradient(
                145deg,
                #121212,
                #080808
            ) !important;

        border:
            1px solid
            rgba(167, 125, 53, 0.58) !important;

        border-radius: 7px !important;
    }


    input {

        color: var(--text) !important;
    }


    label {

        color: #CFC5B5 !important;

        font-size: 13px !important;
    }


    /* ========================================================
       LONG / SHORT
       ======================================================== */

    .cb-direction-info {

        padding: 12px 15px;

        border: 1px solid
            rgba(167, 125, 53, 0.45);

        border-radius: 7px;

        background:
            rgba(201, 163, 90, 0.025);

        color: #BDB4A6;

        font-size: 13px;

        margin-top: 4px;
    }


    /* ========================================================
       ERGEBNISSE
       ======================================================== */

    .cb-results-title {

        display: flex;

        align-items: center;

        gap: 12px;

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


    .cb-result-main {

        border:
            1px solid
            rgba(201, 163, 90, 0.82);

        border-radius: 11px;

        padding: 24px;

        text-align: center;

        background:
            radial-gradient(
                circle at 50% 0%,
                rgba(201, 163, 90, 0.08),
                transparent 60%
            ),

            #080808;

        box-shadow:

            inset
            0 0 30px
            rgba(201, 163, 90, 0.025),

            0 0 18px
            rgba(201, 163, 90, 0.08);
    }


    .cb-result-label {

        color: #D0C5B4;

        font-family:
            "Baskerville",
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
            Georgia,
            serif;

        font-size: clamp(36px, 4vw, 57px);

        font-weight: 500;

        line-height: 1.1;

        margin: 9px 0;

        text-shadow:
            0 0 10px
            rgba(134, 184, 92, 0.18);
    }


    .cb-result-small {

        color: #AFA69A;

        font-size: 13px;
    }


    /* ========================================================
       RESULT CARDS
       ======================================================== */

    .cb-stat {

        min-height: 92px;

        display: flex;

        align-items: center;

        justify-content: space-between;

        gap: 20px;

        padding: 16px 18px;

        margin-top: 12px;

        border:
            1px solid
            rgba(167, 125, 53, 0.48);

        border-radius: 9px;

        background:
            linear-gradient(
                145deg,
                rgba(20, 20, 20, 0.98),
                rgba(8, 8, 8, 0.99)
            );

        box-shadow:
            inset
            0 0 18px
            rgba(201, 163, 90, 0.018);
    }


    .cb-stat-left {

        display: flex;

        align-items: center;

        gap: 13px;

        color: #D4C8B7;

        font-size: 14px;
    }


    .cb-stat-icon {

        width: 38px;

        min-width: 38px;

        height: 38px;

        display: flex;

        align-items: center;

        justify-content: center;

        border:
            1px solid
            rgba(201, 163, 90, 0.50);

        border-radius: 50%;

        color: var(--gold-light);

        font-size: 18px;
    }


    .cb-stat-right {

        color: var(--gold-light);

        font-family:
            "Baskerville",
            Georgia,
            serif;

        font-size: 20px;

        text-align: right;
    }


    .cb-stat-sub {

        color: #8F887F;

        font-family:
            Arial,
            Helvetica,
            sans-serif;

        font-size: 12px;

        margin-top: 2px;
    }


    /* ========================================================
       MARGIN BEREICH
       ======================================================== */

    .cb-margin {

        margin-top: 15px;

        padding: 21px;

        border:
            1px solid
            rgba(167, 125, 53, 0.50);

        border-radius: 9px;

        background:
            rgba(12, 12, 12, 0.94);
    }


    .cb-margin-title {

        color: var(--gold-light);

        font-family:
            "Baskerville",
            Georgia,
            serif;

        font-size: 19px;

        letter-spacing: 0.055em;

        margin-bottom: 16px;
    }


    .cb-margin-row {

        display: flex;

        justify-content: space-between;

        align-items: center;

        padding: 8px 0;

        border-bottom:
            1px solid
            rgba(167, 125, 53, 0.10);

        color: #AAA299;

        font-size: 13px;
    }


    .cb-margin-row:last-child {

        border-bottom: none;
    }


    .cb-margin-value {

        color: #E0D5C3;

        font-size: 15px;
    }


    /* ========================================================
       HINWEIS
       ======================================================== */

    .cb-warning {

        margin-top: 18px;

        padding: 18px 20px;

        border:
            1px solid
            rgba(167, 125, 53, 0.68);

        border-radius: 9px;

        background:
            linear-gradient(
                145deg,
                rgba(27, 23, 16, 0.96),
                rgba(9, 9, 9, 0.99)
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

        margin-bottom: 7px;

        letter-spacing: 0.04em;
    }


    /* ========================================================
       FOOTER
       ======================================================== */

    .cb-footer {

        margin-top: 26px;

        padding-top: 18px;

        border-top:
            1px solid
            rgba(167, 125, 53, 0.30);

        text-align: center;

        color: #716C64;

        font-size: 12px;

        letter-spacing: 0.12em;

        font-family:
            "Baskerville",
            Georgia,
            serif;
    }


    .cb-footer-gold {

        color: var(--gold-main);
    }


    /* ========================================================
       MOBILE
       ======================================================== */

    @media (max-width: 850px) {

        .block-container {

            padding-left: 0.7rem;

            padding-right: 0.7rem;
        }


        .cb-main-shell {

            padding: 17px;
        }


        .cb-header {

            flex-direction: column;

            align-items: flex-start;

            gap: 17px;
        }


        .cb-brand-icon {

            width: 65px;

            height: 65px;
        }


        .cb-brand-icon img {

            width: 50px;

            height: 50px;
        }


        .cb-title-main {

            font-size: 30px;
        }


        .cb-title-sub {

            font-size: 12px;

            letter-spacing: 0.10em;
        }


        .cb-stat {

            min-height: 82px;

            padding: 13px;
        }


        .cb-stat-right {

            font-size: 17px;
        }


        .cb-result-value {

            font-size: 40px;
        }
    }

    </style>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# HILFSFUNKTIONEN
# ============================================================

def money(value):
    return f"{value:,.2f} €".replace(",", "X").replace(".", ",").replace("X", ".")


def number_de(value, decimals=2):
    return (
        f"{value:,.{decimals}f}"
        .replace(",", "X")
        .replace(".", ",")
        .replace("X", ".")
    )


def safe_divide(a, b):
    if b == 0:
        return 0
    return a / b


# ============================================================
# HEADER
# ============================================================

if logo_data:

    logo_html = f"""
        <img
            src="data:image/png;base64,{logo_data}"
            style="
                width:62px;
                height:62px;
                object-fit:contain;
            "
        >
    """

else:

    logo_html = """
        <div class="cb-brand-fallback">
            ♢
        </div>
    """


if calculator_data:

    calculator_html = f"""
        <img
            src="data:image/png;base64,{calculator_data}"
            style="
                width:62px;
                height:62px;
                object-fit:contain;
            "
        >
    """

else:

    calculator_html = """
        <div class="cb-brand-fallback">
            🧮
        </div>
    """


st.html(
    f"""
    <div class="cb-header">

        <div class="cb-brand">

            <div class="cb-brand-icon">
                {calculator_html}
            </div>

            <div>

                <div class="cb-title-main">
                    COUNT OR BREAK
                </div>

                <div class="cb-title-sub">
                    Positionsgrößenrechner
                </div>

            </div>

        </div>

        <div class="cb-info-box">
            ⓘ &nbsp; Anleitung
        </div>

    </div>

    <div class="cb-line"></div>
    """
)


# ============================================================
# HAUPTBEREICH
# ============================================================

st.markdown(
    '<div class="cb-main-shell">',
    unsafe_allow_html=True,
)


left_column, right_column = st.columns(
    [1.03, 1],
    gap="large",
)


# ============================================================
# LINKE SEITE
# ============================================================

with left_column:

    # --------------------------------------------------------
    # 1. MARKT
    # --------------------------------------------------------

    st.markdown(
        '<div class="cb-section-title">1. Markt</div>',
        unsafe_allow_html=True,
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
        index=0,
    )


    instrument = st.text_input(
        "Instrument",
        value="EUR/USD" if market == "Forex CFD" else "",
        placeholder="z. B. EUR/USD, NAS100, XAU/USD, BTC/USD",
    )


    if market in [
        "Forex CFD",
        "Index CFD",
        "Krypto CFD",
        "Rohstoff CFD",
        "Aktien CFD",
        "Sonstiger CFD",
    ]:

        st.caption(
            "Broker: Pepperstone · Werte bitte anhand der "
            "aktuellen Produktspezifikation deines Instruments prüfen."
        )


    st.markdown(
        '<div class="cb-section-divider"></div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # 2. TRADE-RICHTUNG
    # --------------------------------------------------------

    st.markdown(
        '<div class="cb-section-title">2. Trade-Richtung</div>',
        unsafe_allow_html=True,
    )

    direction = st.radio(
        "Richtung",
        ["Long", "Short"],
        horizontal=True,
        label_visibility="collapsed",
    )


    if direction == "Long":

        st.markdown(
            """
            <div class="cb-direction-info">
                ↗ Long: Der Stop-Loss liegt unterhalb des Einstiegs.
            </div>
            """,
            unsafe_allow_html=True,
        )

    else:

        st.markdown(
            """
            <div class="cb-direction-info">
                ↘ Short: Der Stop-Loss liegt oberhalb des Einstiegs.
            </div>
            """,
            unsafe_allow_html=True,
        )


    st.markdown(
        '<div class="cb-section-divider"></div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # 3. KONTO & RISIKO
    # --------------------------------------------------------

    st.markdown(
        '<div class="cb-section-title">3. Konto & Risiko</div>',
        unsafe_allow_html=True,
    )

    col_a, col_b = st.columns(2)

    with col_a:

        account_size = st.number_input(
            "Kontogröße (€)",
            min_value=0.01,
            value=10000.00,
            step=100.00,
            format="%.2f",
        )

    with col_b:

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
        "Max. Risiko (€)",
        min_value=0.01,
        value=float(max_risk),
        step=10.00,
        format="%.2f",
        disabled=True,
    )


    st.markdown(
        '<div class="cb-section-divider"></div>',
        unsafe_allow_html=True,
    )


    # --------------------------------------------------------
    # 4. TRADE-DATEN
    # --------------------------------------------------------

    st.markdown(
        '<div class="cb-section-title">4. Trade-Daten</div>',
        unsafe_allow_html=True,
    )

    col_c, col_d = st.columns(2)


    with col_c:

        entry_price = st.number_input(
            "Einstiegskurs",
            min_value=0.00000001,
            value=1.17000 if market == "Forex CFD" else 100.0,
            step=0.00001 if market == "Forex CFD" else 0.1,
            format="%.5f" if market == "Forex CFD" else "%.4f",
        )


    with col_d:

        if direction == "Long":

            default_stop = (
                1.16500
                if market == "Forex CFD"
                else max(entry_price * 0.98, 0.00000001)
            )

        else:

            default_stop = (
                1.17500
                if market == "Forex CFD"
                else entry_price * 1.02
            )


        stop_loss = st.number_input(
            "Stop-Loss",
            min_value=0.00000001,
            value=float(default_stop),
            step=0.00001 if market == "Forex CFD" else 0.1,
            format="%.5f" if market == "Forex CFD" else "%.4f",
        )


    take_profit = st.number_input(
        "Take-Profit (optional)",
        min_value=0.0,
        value=0.0,
        step=0.00001 if market == "Forex CFD" else 0.1,
        format="%.5f" if market == "Forex CFD" else "%.4f",
        help="0 = kein Take-Profit angegeben.",
    )


    # --------------------------------------------------------
    # STOP DISTANZ
    # --------------------------------------------------------

    price_distance = abs(entry_price - stop_loss)

    stop_percent = safe_divide(
        price_distance,
        entry_price,
    ) * 100


    # --------------------------------------------------------
    # 5. INSTRUMENT DETAILS
    # --------------------------------------------------------

    st.markdown(
        '<div class="cb-section-divider"></div>',
        unsafe_allow_html=True,
    )

    st.markdown(
        '<div class="cb-section-title">5. Instrument Details</div>',
        unsafe_allow_html=True,
    )


    # ========================================================
    # FOREX
    # ========================================================

    if market == "Forex CFD":

        col_e, col_f = st.columns(2)

        with col_e:

            lot_size = st.number_input(
                "Lot-Größe",
                min_value=1.0,
                value=100000.0,
                step=1000.0,
                format="%.0f",
            )

        with col_f:

            pip_size = st.number_input(
                "Pip-Größe",
                min_value=0.00000001,
                value=0.00010,
                step=0.00001,
                format="%.5f",
            )


        col_g, col_h = st.columns(2)

        with col_g:

            pip_value_per_lot = st.number_input(
                "Pip-Wert pro Lot (€)",
                min_value=0.0001,
                value=10.00,
                step=0.10,
                format="%.2f",
            )

        with col_h:

            leverage = st.number_input(
                "Hebel",
                min_value=1.0,
                value=30.0,
                step=1.0,
                format="%.0f",
            )


        pips = safe_divide(
            price_distance,
            pip_size,
        )

        risk_per_lot = pips * pip_value_per_lot

        position_lots = safe_divide(
            max_risk,
            risk_per_lot,
        )

        position_units = position_lots * lot_size

        position_value = position_units * entry_price

        margin_required = safe_divide(
            position_value,
            leverage,
        )


    # ========================================================
    # FUTURES
    # ========================================================

    elif market == "Futures":

        col_e, col_f = st.columns(2)

        with col_e:

            tick_size = st.number_input(
                "Tick-Größe",
                min_value=0.00000001,
                value=0.25,
                step=0.01,
                format="%.4f",
            )

        with col_f:

            tick_value = st.number_input(
                "Tick-Wert (€)",
                min_value=0.0001,
                value=12.50,
                step=0.50,
                format="%.2f",
            )


        col_g, col_h = st.columns(2)

        with col_g:

            contract_size = st.number_input(
                "Kontraktgröße",
                min_value=0.0001,
                value=1.0,
                step=1.0,
                format="%.4f",
            )

        with col_h:

            leverage = st.number_input(
                "Hebel",
                min_value=1.0,
                value=20.0,
                step=1.0,
                format="%.0f",
            )


        ticks = safe_divide(
            price_distance,
            tick_size,
        )

        risk_per_contract = ticks * tick_value

        position_contracts = safe_divide(
            max_risk,
            risk_per_contract,
        )

        position_units = position_contracts

        position_value = (
            position_contracts
            * contract_size
            * entry_price
        )

        margin_required = safe_divide(
            position_value,
            leverage,
        )


    # ========================================================
    # CFDs
    # ========================================================

    else:

        col_e, col_f = st.columns(2)

        with col_e:

            value_per_unit = st.number_input(
                "Wert pro 1 Preis-Einheit (€)",
                min_value=0.0001,
                value=1.00,
                step=0.10,
                format="%.4f",
                help=(
                    "Wie viel € Gewinn/Verlust entsteht bei "
                    "einer Preisbewegung von 1,00 pro Einheit?"
                ),
            )


        with col_f:

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


        risk_per_unit = price_distance * value_per_unit

        position_units = safe_divide(
            max_risk,
            risk_per_unit,
        )

        position_value = (
            position_units
            * contract_size
            * entry_price
        )

        margin_required = safe_divide(
            position_value,
            leverage,
        )


    # ========================================================
    # VALIDIERUNG
    # ========================================================

    valid_trade = True

    validation_message = ""


    if entry_price <= 0:

        valid_trade = False

        validation_message = (
            "Der Einstiegskurs muss größer als 0 sein."
        )


    elif stop_loss <= 0:

        valid_trade = False

        validation_message = (
            "Der Stop-Loss muss größer als 0 sein."
        )


    elif price_distance <= 0:

        valid_trade = False

        validation_message = (
            "Einstieg und Stop-Loss dürfen nicht identisch sein."
        )


    elif direction == "Long" and stop_loss >= entry_price:

        valid_trade = False

        validation_message = (
            "Bei einem Long-Trade muss der Stop-Loss "
            "unterhalb des Einstiegs liegen."
        )


    elif direction == "Short" and stop_loss <= entry_price:

        valid_trade = False

        validation_message = (
            "Bei einem Short-Trade muss der Stop-Loss "
            "oberhalb des Einstiegs liegen."
        )


    # ========================================================
    # TAKE PROFIT
    # ========================================================

    rr_ratio = None
    potential_profit = None


    if take_profit > 0 and valid_trade:

        if direction == "Long":

            reward_distance = take_profit - entry_price

        else:

            reward_distance = entry_price - take_profit


        if reward_distance > 0:

            rr_ratio = safe_divide(
                reward_distance,
                price_distance,
            )

            potential_profit = max_risk * rr_ratio


# ============================================================
# RECHTE SEITE – ERGEBNISSE
# ============================================================

with right_column:

    st.markdown(
        """
        <div class="cb-results-title">
            🧮 &nbsp; Ergebnisse
        </div>
        """,
        unsafe_allow_html=True,
    )


    if valid_trade:

        # ----------------------------------------------------
        # HAUPTERGEBNIS
        # ----------------------------------------------------

        if market == "Forex CFD":

            position_display = (
                f"{number_de(position_lots, 2)} Lots"
            )

            position_sub = (
                f"= {number_de(position_units, 0)} Einheiten"
            )

        elif market == "Futures":

            position_display = (
                f"{number_de(position_units, 2)} Kontrakte"
            )

            position_sub = "basierend auf dem angegebenen Tick-Wert"

        else:

            position_display = (
                f"{number_de(position_units, 2)} Einheiten"
            )

            position_sub = (
                f"Positionswert: {money(position_value)}"
            )


        st.markdown(
            f"""
            <div class="cb-result-main">

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
            """,
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # MAX VERLUST
        # ----------------------------------------------------

        st.markdown(
            f"""
            <div class="cb-stat">

                <div class="cb-stat-left">

                    <div class="cb-stat-icon">
                        !
                    </div>

                    <div>
                        Max. Verlust bei Stop-Loss

                        <div class="cb-stat-sub">
                            {number_de(risk_percent, 2)} % des Kontos
                        </div>
                    </div>

                </div>

                <div class="cb-stat-right">
                    {money(max_risk)}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # STOP LOSS DISTANZ
        # ----------------------------------------------------

        if market == "Forex CFD":

            stop_display = (
                f"{number_de(pips, 1)} Pips"
            )

        elif market == "Futures":

            stop_display = (
                f"{number_de(ticks, 1)} Ticks"
            )

        else:

            stop_display = (
                f"{number_de(price_distance, 4)} Preis-Einheiten"
            )


        st.markdown(
            f"""
            <div class="cb-stat">

                <div class="cb-stat-left">

                    <div class="cb-stat-icon">
                        ◎
                    </div>

                    <div>
                        Stop-Loss-Abstand

                        <div class="cb-stat-sub">
                            {number_de(stop_percent, 2)} % vom Einstieg
                        </div>
                    </div>

                </div>

                <div class="cb-stat-right">
                    {stop_display}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # POSITIONSWERT
        # ----------------------------------------------------

        st.markdown(
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

                <div class="cb-stat-right">
                    {money(position_value)}
                </div>

            </div>
            """,
            unsafe_allow_html=True,
        )


        # ----------------------------------------------------
        # CHANCE / RISIKO
        # ----------------------------------------------------

        if rr_ratio is not None:

            st.markdown(
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

                    <div class="cb-stat-right">
                        {number_de(rr_ratio, 2)} : 1
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


            st.markdown(
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
                        class="cb-stat-right"
                        style="color:#86B85C;"
                    >
                        {money(potential_profit)}
                    </div>

                </div>
                """,
                unsafe_allow_html=True,
            )


        # ----------------------------------------------------
        # MARGIN & HEBEL
        # ----------------------------------------------------

        st.markdown(
            f"""
            <div class="cb-margin">

                <div class="cb-margin-title">
                    ▥ &nbsp; Margin & Hebel
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
                        Verwendeter Hebel
                    </span>

                    <span class="cb-margin-value">
                        1 : {number_de(leverage, 0)}
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
            """,
            unsafe_allow_html=True,
        )


    else:

        # ----------------------------------------------------
        # FEHLER
        # ----------------------------------------------------

        st.markdown(
            f"""
            <div class="cb-warning">

                <div class="cb-warning-title">
                    ⚠ Eingabe prüfen
                </div>

                {validation_message}

            </div>
            """,
            unsafe_allow_html=True,
        )


# ============================================================
# HINWEIS
# ============================================================

st.markdown(
    """
    <div class="cb-warning">

        <div class="cb-warning-title">
            ⚠ Wichtiger Hinweis
        </div>

        Dieser Rechner dient zur Orientierung bei der
        Positions- und Risikoplanung. Bei CFDs können Verluste
        schnell entstehen. Prüfe die aktuellen
        Produktspezifikationen, Kontraktgrößen, Pip-/Tick-Werte
        und Margin-Anforderungen deines konkreten Instruments
        vor dem Trade.

        <br><br>

        <strong>Risk first. Profits second.</strong>

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

        <span class="cb-footer-gold">
            COUNT OR BREAK
        </span>

        &nbsp; • &nbsp;

        TRADE PLAN. STAY DISCIPLINED. BREAK LIMITS.

    </div>
    """,
    unsafe_allow_html=True,
)


# ============================================================
# ENDE
# ============================================================

st.markdown(
    "</div>",
    unsafe_allow_html=True,
)
