import streamlit as st
import pandas as pd

# Configuração inicial
st.set_page_config(page_title="SAQA - Execução Financeira", layout="wide")

# Menu de Navegação (imita as abas do seu Excel)
aba = st.sidebar.radio(
    "Seleccione a Área (Abas)",
    ["Regras de Utilização", "VN (Vendas)", "FSE", "Fundo de Maneio", "DR (Resultados)", "Cash Flow"]
)

# --- ABA: REGRAS DE UTILIZAÇÃO ---
if aba == "Regras de Utilização":
    st.title("📖 Regras de Utilização")
    st.write("Estimar o volume de negócios da empresa através das quantidades vendidas e preços.")

# --- ABA: VN (VENDAS) ---
elif aba == "VN (Vendas)":
    st.title("📈 VN - Volume de Negócios")
    st.info("Registe aqui a execução real das vendas.")
    mes = st.selectbox("Mês", ["Janeiro", "Fevereiro", "Março"])
    valor_vn = st.number_input("Valor de Vendas Realizado (€)", min_value=0.0)
    st.success(f"Registado: {valor_vn}€ em {mes}")

# --- ABA: FUNDO DE MANEIO (Onde entra o IVA) ---
elif aba == "Fundo de Maneio":
    st.title("⚙️ Fundo de Maneio")
    st.subheader("Recursos Fundo Maneio - Estado")
    
    # Campo específico para o seu reembolso
    reembolso_iva = st.number_input("Valor do Reembolso de IVA recebido (€)", min_value=0.0)
    
    if reembolso_iva > 0:
        st.warning(f"O montante de {reembolso_iva}€ será reflectido como entrada no Cash Flow.")

# --- ABA: CASH FLOW ---
elif aba == "Cash Flow":
    st.title("💸 Mapa de Cash Flow")
    st.write("Aqui vê o saldo acumulado e os meios libertos.")
    
    # Exemplo de visualização simples
    st.metric("CASH FLOW Acumulado", "31.523 €", delta="Melhoria via IVA")
    st.bar_chart({"Resultados": [30211, 33504, 33504], "Cash Flow": [31523, 33504, 33504]})
