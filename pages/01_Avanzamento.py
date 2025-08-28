# pages/01_Avanzamento.py
import streamlit as st
st.set_page_config(page_title="Avanzamento Economico", layout="wide")

st.title("📊 Avanzamento Economico")
st.caption("Questa è una pagina interna (multipagina).")

# Esempio: link per tornare alla Home senza aprire nuove schede
st.page_link("Home.py", label="🏠 Torna alla Home")
