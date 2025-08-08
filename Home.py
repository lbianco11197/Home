
import streamlit as st

# Configurazione pagina con sidebar chiusa
st.set_page_config(
    page_title="Portale Euroirte",
    layout="wide",
    initial_sidebar_state="collapsed"  # <--- sidebar chiusa di default
)

#imposta sfondo sempre bianco e testi neri
st.markdown("""
    <style>
    /* Sfondo e testo di base */
    html, body, [data-testid="stApp"] {
        background-color: white !important;
        color: black !important;
    }

    /* RADIO BUTTON - Forza etichette nere */
    .stRadio div[role="radiogroup"] label span {
        color: black !important;
        font-weight: 500 !important;
    }

    /* RADIO BUTTON - Mobile layout più leggibile */
    @media only screen and (max-width: 768px) {
        .stRadio > div {
            flex-direction: row !important;
            justify-content: space-evenly;
            gap: 10px;
        }
        .stRadio div[role="radiogroup"] label span {
            font-size: 15px !important;
        }
    }

    /* Pulsanti */
    .stButton > button {
        background-color: white !important;
        color: black !important;
        border: 1px solid #ccc !important;
        border-radius: 6px !important;
    }
    </style>
""", unsafe_allow_html=True)

# Lista di utenti autorizzati
utenti_autorizzati = ["lbianco", "acapizzi", "gcassarino"]
password_corretta = "Euroirte111927"

# Sidebar riservata
with st.sidebar:
    st.markdown("## Area Riservata")
    admin_login = st.checkbox("Accedi come amministratore")

    if admin_login:
        username = st.text_input("Nome utente")
        password = st.text_input("Password", type="password")

        if username in utenti_autorizzati and password == password_corretta:
            st.success(f"Accesso autorizzato, benvenuto {username} 👋")
            st.markdown("[Vai all'area di gestione file 📁](https://amministratore.streamlit.app/)")
        elif username and password:
            st.error("Credenziali errate")

st.set_page_config(page_title="Portale Euroirte", layout="centered")

# Logo e benvenuto
st.image("LogoEuroirte.jpg", width=200)
st.markdown("""
# Benvenuto nel portale di **Avanzamento Produzione Euroirte**

Gestisci e monitora i dati di produzione per committente e tipologia di report.
""", unsafe_allow_html=True)

# Scelta Committente
st.markdown("## Seleziona la committente")
committente = st.radio("", ["TIM", "OPEN FIBER"], horizontal=True)

if committente == "TIM":
    st.markdown("### Seleziona il tipo di report")
    col1, col2 = st.columns(2)
    with col1:
        if st.button("📈 Report Assurance"):
            st.markdown("[Vai al Report Assurance TIM](https://avanzamento-impulsiva-v2-ds8ntkmcuqu3mtlak3ntog.streamlit.app/)")
    with col2:
        if st.button("📊 Report Delivery"):
            st.markdown("[Vai al Report Delivery TIM](https://avanzamento-delivery-8ffqqvktcoli9kqk48dgki.streamlit.app/)")
else:
    st.markdown("🚧 I report per Open Fiber sono attualmente in fase di sviluppo.")
