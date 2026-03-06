import streamlit as st
import pandas as pd

# Configuração da App para a SAQA
st.set_page_config(page_title="Execução Financeira SAQA", layout="wide")

st.title("📊 Controlo de Execução - SAQA")
st.info("Substitui a lógica de Fundo de Maneio do IAPMEI por gestão real de tesouraria.")

# Entrada de dados
with st.sidebar:
    st.header("Registo de Movimentos")
    vendas = st.number_input("Vendas (Recebido c/ IVA)", min_value=0.0)
    reembolso_iva = st.number_input("Reembolso de IVA Recebido", min_value=0.0)
    custos = st.number_input("Total de Pagamentos (Saídas)", min_value=0.0)

# Cálculos de Fluxo de Caixa
saldo_real = (vendas + reembolso_iva) - custos

# Mostrar resultados
c1, c2 = st.columns(2)
c1.metric("Entrada Total (Cash In)", f"{vendas + reembolso_iva} €")
c2.metric("Saldo de Tesouraria", f"{saldo_real} €", delta=f"{reembolso_iva} do IVA")

st.markdown("---")
st.write("### Onde colocar o Reembolso de IVA?")
st.write("Nesta app, o reembolso entra como uma **Entrada Direta**. Ao contrário do mapa do IAPMEI, aqui vês o dinheiro a subir no momento em que cai no banco.")
