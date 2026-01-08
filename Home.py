import streamlit as st
import pandas as pd
import base64
import requests

# ===============================================================
#  BLOCCO DI CODICE DA COPIARE E INCOLLARE
# ===============================================================

# 1. Funzione per lo sfondo
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

# 2. Configurazione della pagina (una sola volta)
st.set_page_config(
    page_title="Portale Euroirte",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# 3. Chiamata alla funzione per impostare lo sfondo
#    Assicurati di avere 'sfondo.png' nella stessa cartella
try:
    add_bg_from_local('sfondo.png')
except FileNotFoundError:
    st.warning("Immagine di sfondo 'sfondo.png' non trovata.")


# 4. Nuovo Stile CSS per leggibilità
st.markdown("""
<style>
/* Contenitore principale con sfondo semi-trasparente */
[data-testid="stApp"] > div > div:nth-child(2) > div {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 2rem;
    border-radius: 10px;
}

/* Testo nero per tutti gli elementi */
h1, h2, h3, p, span, div, label {
    color: black !important;
}

/* --- INPUT (anche nella SIDEBAR) con bordo grigio chiaro --- */
.stTextInput > div > div > input,
.stPasswordInput > div > div > input,
.stSelectbox div[data-baseweb="select"],
.stMultiSelect div[data-baseweb="select"],
.stNumberInput input,
.stDateInput input,
.stTextArea textarea {
    background-color: rgba(255,255,255,0.9) !important;
    border: 1px solid #ddd !important;   /* 👈 bordo grigio chiaro */
    border-radius: 8px;
    color: #000 !important;
}

/* Pulsanti */
.stButton > button {
    background-color: white !important;
    color: black !important;
    border: 1px solid #ddd !important;   /* 👈 bordo chiaro */
    border-radius: 8px;
}
.stButton > button:hover {
    background-color: #f0f0f0 !important;
}

/* Link Button */
.stLinkButton > a {
    background-color: white !important;
    border: 1px solid #ddd !important;
    border-radius: 8px;
}
.stLinkButton > a:hover {
    background-color: #f0f0f0 !important;
}
</style>
""", unsafe_allow_html=True)

st.markdown("""
<style>
/* Linea di separazione sulla sidebar */
[data-testid="stSidebar"] {
    border-right: 2px solid #ddd !important;  /* 👈 linea grigio chiaro */
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
# Header: logo + bottone News
col_logo, col_spazio, col_news = st.columns([2, 6, 2])

with col_logo:
    st.image("LogoEuroirte.png", width=180)

with col_news:
    st.markdown("<br>", unsafe_allow_html=True)
    st.link_button(
        "📰 News A.C. IMPIANTI s.r.l.",
        "https://news-acimpianti.streamlit.app/"
    )

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



