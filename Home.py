
import streamlit as st

# Configurazione pagina con sidebar chiusa
st.set_page_config(
    page_title="Portale Euroirte",
    layout="wide",
    initial_sidebar_state="collapsed"  # <--- sidebar chiusa di default
)

# Imposta sfondo bianco e testo nero
st.markdown(
    """
    <style>
        html, body, [data-testid="stApp"] {
            background-color: white !important;
            color: black !important;
        }
        .stTextInput input, .stPasswordInput input, .stSelectbox, .stFileUploader, .stButton {
            color: black !important;
            background-color: white !important;
        }
        .stMarkdown, .stDataFrame, .stAlert {
            color: black !important;
        }
        .css-1d391kg {  /* Titolo */
            color: black !important;
        }
    </style>
    """,
    unsafe_allow_html=True
)

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
