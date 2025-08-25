import streamlit as st
import pandas as pd
import base64
import requests

# Funzione per caricare e codificare l'immagine di sfondo
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded_string}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Configurazione pagina con sidebar chiusa
st.set_page_config(
    page_title="Portale Euroirte",
    layout="wide",
    # --- IMPOSTA L'IMMAGINE DI SFONDO ---
# Assicurati di avere un file 'sfondo.jpg' nella stessa cartella dello script
try:
    add_bg_from_local('sfondo.png')
except FileNotFoundError:
    st.warning("Immagine di sfondo 'sfondo.png' non trovata. Verrà usato uno sfondo bianco.")

# --- MODIFICA LO STILE CSS ESISTENTE ---
st.markdown(
    """
    <style>
    /* Rimuovi lo sfondo bianco per far vedere l'immagine */
    /* html, body, [data-testid="stApp"] { background-color: white !important; } */

    /* Rendi i widget leggermente trasparenti per leggibilità */
    .stSelectbox div[data-baseweb="select"],
    .stDataFrame, .stDataFrame table, .stDataFrame th, .stDataFrame td,
    .stButton > button,
    div[data-baseweb="radio"] {
        background-color: rgba(255, 255, 255, 0.8) !important;
    }

    /* Il resto del tuo stile rimane invariato */
    .stSelectbox span, .stSelectbox label { color: black !important; font-weight: 500; }
    .stButton > button { color: black !important; border: 1px solid #999 !important; border-radius: 6px; }
    div[data-baseweb="radio"] label span { color: black !important; font-weight: 600 !important; }
    header [data-testid="theme-toggle"] { display: none; }
    </style>
    """,
    unsafe_allow_html=True,
)
    initial_sidebar_state="collapsed"  # <--- sidebar chiusa di default
)

#imposta sfondo sempre bianco e testi neri
#st.markdown("""
#<style>
#/* Sfondo generale bianco e testo nero */
#html, body, [data-testid="stApp"] {
#    background-color: white !important;
#    color: black !important;
#}

/* Titoli, markdown e testi */
h1, h2, h3, h4, h5, h6, p, span, div, label {
    color: black !important;
}

/* Radio button etichette */
div[data-baseweb="radio"] label {
    color: black !important;
    font-weight: 600 !important;
}

/* Input e selezioni */
input, textarea, select {
    background-color: white !important;
    color: black !important;
}

/* Pulsanti */
button[kind="primary"], button[kind="secondary"], .stButton > button {
    background-color: white !important;
    color: black !important;
    border: 1px solid #999 !important;
    border-radius: 6px;
}

/* Pulsanti al passaggio del mouse */
button[kind="primary"]:hover, button[kind="secondary"]:hover, .stButton > button:hover {
    background-color: #f0f0f0 !important;
    color: black !important;
}

/* Dataframe */
.css-1d391kg, .stDataFrame, .css-1m3z7sd {
    color: black !important;
    background-color: white !important;
}

/* Riduzione padding su mobile */
@media only screen and (max-width: 768px) {
    .stRadio > div {
        flex-direction: row !important;
        gap: 1rem;
        justify-content: space-around;
    }
    .stRadio label {
        font-size: 14px !important;
    }
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
            st.markdown("[Vai all'area di gestione 📁](https://amministratore.streamlit.app/)")
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
        st.link_button("📝 Vai al Report Assurance TIM", "https://avanzamento-impulsiva-v2-ds8ntkmcuqu3mtlak3ntog.streamlit.app/")
    with col2:
        st.link_button("📊 Vai al Report Delivery TIM", "https://avanzamento-delivery-8ffqqvktcoli9kqk48dgki.streamlit.app/")

if committente == "OPEN FIBER": 
        st.link_button("📊 Vai al Report Delivery OF", "https://avanzamentodeliveryof.streamlit.app/")



