
import streamlit as st

st.set_page_config(page_title="Portale Euroirte", layout="centered")

# Logo e benvenuto
st.image("LogoEuroirte.jpg", width=200)
st.markdown("""
# Benvenuto nel portale di **Avanzamento Produzione Euroirte**

menu = st.selectbox("Scegli una sezione", ["Benvenuto", "TIM - Report Assurance", "TIM - Report Delivery", "Area Amministratore"])

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
