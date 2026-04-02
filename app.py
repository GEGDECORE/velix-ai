import streamlit as st
import pandas as pd
from openai import OpenAI

# Configuração de Interface
st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# --- SEUS DADOS DE DESENVOLVEDOR ML (Substitua quando tiver o App criado no ML) ---
CLIENT_ID = "SEU_CLIENT_ID_AQUI" 
REDIRECT_URI = "https://velix-ai.streamlit.app/" # A URL do seu app

# --- ESTILO VISUAL ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 2px solid #00FFFF; }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p, 
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] span { 
        color: #FFFFFF !important; 
        font-size: 1.1rem !important; 
        font-weight: 800 !important;
    }
    h1, h2, h3 { color: #00FFFF !important; text-shadow: 0 0 8px #00FFFF; }
    .stButton>button {
        background-image: linear-gradient(to right, #00FFFF, #FF00FF);
        color: white !important; border: none; font-weight: bold; border-radius: 10px; width: 100%;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU ---
st.sidebar.markdown("<h1 style='text-align: center;'>VELIX AI</h1>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Gestão Executiva",
    ["📊 Dashboard de Performance", "📈 Algoritmo VELIX AI", "🧠 Inteligência Estratégica", "🔗 Integração Mercado Livre"]
)

# --- TELAS ---

if menu == "🔗 Integração Mercado Livre":
    st.title("🔗 Integração de Ativos")
    st.write("Clique no botão abaixo para conectar a conta do Mercado Livre à Velix AI.")
    
    # URL oficial de autorização do Mercado Livre
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    
    # Botão que funciona como link externo
    st.markdown(f"""
        <a href="{auth_url}" target="_blank">
            <button style="
                width: 100%;
                background-image: linear-gradient(to right, #00FFFF, #FF00FF);
                color: white;
                padding: 15px;
                border: none;
                border-radius: 10px;
                font-weight: bold;
                cursor: pointer;
                font-size: 16px;">
                CONECTAR CONTA MERCADO LIVRE
            </button>
        </a>
    """, unsafe_allow_html=True)
    
    st.write("---")
    st.info("Após clicar, você será levado ao portal oficial do Mercado Livre para autorizar o acesso.")

elif menu == "📈 Algoritmo VELIX AI":
    st.title("📈 Algoritmo VELIX AI")
    url = st.text_input("Cole aqui a URL do anúncio concorrente:")
    if st.button("Executar Algoritmo de Otimização"):
        st.write("Analisando métricas de topo de funil...")

elif menu == "🧠 Inteligência Estratégica":
    st.title("🧠 Inteligência Estratégica")
    st.info("Este módulo requer saldo na OpenAI para processar as respostas.")
    st.text_area("O que deseja planejar hoje?")

elif menu == "📊 Dashboard de Performance":
    st.title("Painel de Performance")
    col1, col2, col3 = st.columns(3)
    col1.metric("Volume de Vendas", "R$ 42.850", "+15%")
    col2.metric("Conversão Média", "5.2%", "+0.8%")
    col3.metric("Anúncios no Topo", "18")

st.sidebar.markdown("---")
st.sidebar.caption("Daniele Xavier | Gestão de Elite")
