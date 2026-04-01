import streamlit as st
from pymongo import MongoClient
from datetime import datetime

# Configuração de Conexão com o MongoDB
# Já configurado com seu usuário e senha fornecidos
uri = "mongodb+srv://danixavier27_db_user:fDPiWGsXFr2DTUbd@cluster0.ukv584f.mongodb.net/?appName=Cluster0"
client = MongoClient(uri)
db = client['venda_flow_db']
collection = db['vendas']

# Configuração da Página do Streamlit
st.set_page_config(page_title="VendaFlow AI", page_icon="🚀", layout="wide")

st.title("🚀 VendaFlow AI - Gestão de Alta Performance")
st.subheader("Bem-vinda de volta, Daniele Xavier")

# Menu Lateral
menu = ["Registrar Venda", "Histórico de Vendas", "Dashboard"]
choice = st.sidebar.selectbox("Navegação", menu)

if choice == "Registrar Venda":
    st.header("📝 Nova Venda")
    
    with st.form("form_venda"):
        cliente = st.text_input("Nome do Cliente")
        servico = st.selectbox("Serviço", ["Terapia de Reintegração", "Mentoria de Alta Performance", "Combo Destrave", "Outros"])
        valor = st.number_input("Valor (R$)", min_value=0.0, format="%.2f")
        data = st.date_input("Data da Venda", datetime.now())
        
        submit = st.form_submit_button("Salvar Venda")
        
        if submit:
            if cliente and valor > 0:
                venda_data = {
                    "cliente": cliente,
                    "servico": servico,
                    "valor": valor,
                    "data": str(data),
                    "timestamp": datetime.now()
                }
                collection.insert_one(venda_data)
                st.success(f"Venda para {cliente} registrada com sucesso!")
            else:
                st.error("Por favor, preencha o nome do cliente e o valor.")

elif choice == "Histórico de Vendas":
    st.header("📊 Histórico de Vendas")
    vendas = list(collection.find().sort("timestamp", -1))
    
    if vendas:
        for v in vendas:
            with st.expander(f"{v['cliente']} - R$ {v['valor']}"):
                st.write(f"*Serviço:* {v['servico']}")
                st.write(f"*Data:* {v['data']}")
    else:
        st.info("Nenhuma venda registrada ainda.")

elif choice == "Dashboard":
    st.header("📈 Desempenho Geral")
    vendas = list(collection.find())
    total_faturado = sum(v['valor'] for v in vendas)
    total_vendas = len(vendas)
    
    col1, col2 = st.columns(2)
    col1.metric("Total Faturado", f"R$ {total_faturado:.2f}")
    col2.metric("Quantidade de Vendas", total_vendas)
