import streamlit as st
import base64
from pathlib import Path

# ===============================================================
#  CONFIGURAZIONE PAGINA (una sola volta)
# ===============================================================
st.set_page_config(
    page_title="Portale Euroirte",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ===============================================================
#  SFONDO (immagine locale)
# ===============================================================
def add_bg_from_local(image_path: str = "sfondo.png"):
    p = Path(image_path)
    if not p.exists():
        st.warning(f"Immagine di sfondo '{image_path}' non trovata.")
        return
    encoded = base64.b64encode(p.read_bytes()).decode()
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/png;base64,{encoded}");
            background-size: cover;
            background-attachment: fixed;
            background-repeat: no-repeat;
        }}
        /* Contenitore principale con sfondo semi-trasparente per leggibilità */
        [data-testid="stApp"] > div > div:nth-child(2) > div {{
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 10px;
        }}
        /* Testi e pulsanti */
        h1, h2, h3, p, span, div, label {{ color: #0b1320 !important; }}
        .stButton > button {{ background-color: #fff !important; color:#0b1320 !important; border:1px solid #999 !important; }}
        .stButton > button:hover {{ background-color:#f0f0f0 !important; }}
        .stLinkButton > a {{ background-color:#fff !important; border:1px solid #999 !important; }}
        .stLinkButton > a:hover {{ background-color:#f0f0f0 !important; }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local("sfondo.png")

# ===============================================================
#  SIDEBAR: Area riservata (Admin)
#  Ora usa la NAVIGAZIONE INTERNA con st.page_link/st.switch_page
# ===============================================================
UTENTI_AUTORIZZATI = {"lbianco", "acapizzi", "gcassarino"}
PASSWORD_CORRETTA = "Euroirte111927"

with st.sidebar:
    st.markdown("## Area Riservata")
    admin_login = st.checkbox("Accedi come amministratore")

    if admin_login:
        username = st.text_input("Nome utente")
        password = st.text_input("Password", type="password")

        if username in UTENTI_AUTORIZZATI and password == PASSWORD_CORRETTA:
            st.success(f"Accesso autorizzato, benvenuto {username} 👋")
            # Apri la pagina Admin NELLA STESSA APP
            if st.button("Vai all'area di gestione 📁"):
                st.switch_page("pages/99_Admin.py")
        elif username and password:
            st.error("Credenziali errate")

# ===============================================================
#  HEADER
# ===============================================================
logo_path = Path("LogoEuroirte.png")
if logo_path.exists():
    st.image(str(logo_path), width=200)

st.markdown("""
# Benvenuto nel portale di **Avanzamento Produzione Euroirte**
Gestisci e monitora i dati di produzione per committente e tipologia di report.
""")

# ===============================================================
#  SCELTA COMMITTENTE + LINK INTERNI ALLE PAGINE
# ===============================================================
st.markdown("## Seleziona la committente")
committente = st.radio("", ["TIM", "OPEN FIBER"], horizontal=True)

if committente == "TIM":
    st.markdown("### Seleziona il tipo di report")
    col1, col2 = st.columns(2)
    with col1:
        # Apre "pages/01_Assurance_TIM.py" nella stessa scheda
        st.page_link("pages/01_Assurance_TIM.py", label="📝 Vai al Report Assurance TIM")
    with col2:
        st.page_link("pages/02_Delivery_TIM.py", label="📊 Vai al Report Delivery TIM")

if committente == "OPEN FIBER":
    st.page_link("pages/03_Delivery_OF.py", label="📊 Vai al Report Delivery OF")
