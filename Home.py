
import streamlit as st

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

#sidebar Amministratore
with st.sidebar:
    st.markdown("## Area Riservata")
    admin_access = st.checkbox("Accedi come amministratore")

    if admin_access:
        admin_pwd = st.text_input("Password", type="password")

        if admin_pwd == "euroirte2025":
            st.success("Accesso autorizzato")
            st.markdown("[Vai all'area di gestione file 📁](https://upload-euroirte-admin.streamlit.app/)")
        elif admin_pwd != "":
            st.error("Password errata")
