import streamlit as st
import pandas as pd

# Configuração da página com o nome da sua empresa
st.set_page_config(page_title="SAQA - Gestão Operacional", layout="wide")

# Estilização para parecer um dashboard profissional
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e0e0e0; }
    </style>
    """, unsafe_allow_html=True)

# 1. Navegação Lateral (Réplica das Abas do seu Excel)
with st.sidebar:
    st.image("https://www.iapmei.pt/getmedia/35967397-6a5e-4993-9d10-3882f0c766e4/logo_iapmei.aspx", width=150)
    st.title("Menu SAQA")
    aba = st.radio(
        "Selecione a Área de Trabalho:",
        ["Dashboard Geral", "VN (Vendas)", "CMVMC", "FSE (Custos)", "Pessoal", "Fundo de Maneio", "Cash Flow"]
    )

# --- ABA: DASHBOARD GERAL ---
if aba == "Dashboard Geral":
    st.title("📊 Painel de Controlo Operacional")
    col1, col2, col3 = st.columns(3)
    col1.metric("Volume Negócios (Real)", "8.200 €", "+5%")
    col2.metric("EBITDA Estimado", "3.400 €", "-2%")
    col3.metric("Saldo em Banco", "12.450 €", "Reembolso IVA")

# --- ABA: VN (VOLUME DE NEGÓCIOS) ---
elif aba == "VN (Vendas)":
    st.title("📈 VN - Registo de Vendas Reais")
    st.info("Utilize esta aba para registar as vendas efetuadas (quantidades x preço).")
    
    col1, col2 = st.columns(2)
    with col1:
        produto = st.text_input("Produto/Serviço", "Vacas")
        qtd = st.number_input("Quantidade", min_value=0)
    with col2:
        preco = st.number_input("Preço Unitário (€)", min_value=0.0)
        total_vn = qtd * preco
        st.subheader(f"Total VN: {total_vn:,.2f} €")
    
    if st.button("Gravar Venda"):
        st.success("Venda registada na base de dados de execução!")

# --- ABA: FUNDO DE MANEIO (Onde entra o seu Reembolso) ---
elif aba == "Fundo de Maneio":
    st.title("⚙️ Gestão de Fundo de Maneio")
    st.markdown("### Recursos: Estado")
    
    st.write("No seu Excel original, isto está na aba 'FundoManeio'. Aqui, registamos o recebimento real.")
    
    reembolso_iva = st.number_input("Valor do Reembolso de IVA Recebido (€)", min_value=0.0, help="Dinheiro que caiu na conta vindo do Estado")
    
    if reembolso_iva > 0:
        st.balloons()
        st.success(f"Entrada de {reembolso_iva}€ registada como recurso imediato.")

# --- ABA: CASH FLOW (O resultado final) ---
elif aba == "Cash Flow":
    st.title("💸 Cash Flow de Execução")
    st.write("Este mapa mostra o dinheiro real, não apenas a contabilidade.")
    
    # Simulação de dados baseada na sua estrutura do IAPMEI
    dados = {
        'Mês': ['Jan', 'Fev', 'Mar'],
        'Entradas': [8000, 8500, 13000], # Março inclui Reembolso IVA
        'Saídas': [5000, 5200, 5100]
    }
    df = pd.DataFrame(dados)
    df['Saldo'] = df['Entradas'] - df['Saídas']
    
    st.line_chart(df.set_index('Mês')[['Entradas', 'Saídas']])
    st.table(df)
