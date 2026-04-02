import streamlit as st
import requests
from openai import OpenAI

# --- CONFIGURAÇÃO DE INTEGRAÇÃO ---
CLIENT_ID = "8642953419393317" 
REDIRECT_URI = "https://velix-ai.streamlited.app/" 

# Configuração de Interface
st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# --- ESTILO VISUAL CORRIGIDO ---
st.markdown("""
    <style>
    .stApp { 
        background-color: #0E1117; 
        color: #FFFFFF !important; 
    }
    section[data-testid="stSidebar"] { 
        background-color: #161B22 !important; 
        border-right: 2px solid #00FFFF; 
    }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p, 
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] span { 
        color: #FFFFFF !important; 
        font-size: 1.1rem !important; 
        font-weight: 800 !important;
    }
    h1, h2, h3 { 
        color: #00FFFF !important; 
        text-shadow: 0 0 8px #00FFFF; 
    }
    .stButton>button {
        background-image: linear-gradient(to right, #00FFFF, #FF00FF);
        color: white !important; 
        border: none; 
        font-weight: bold; 
        border-radius: 10px; 
        width: 100%;
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
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    
    st.markdown(f'<a href="{auth_url}" target="_blank"><button style="width: 100%; background-image: linear-gradient(to right, #00FFFF, #FF00FF); color: white; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 16px;">CONECTAR CONTA MERCADO LIVRE</button></a>', unsafe_allow_html=True)
    st.info("Clique acima para autorizar a Velix AI no Mercado Livre.")

elif menu == "📈 Algoritmo VELIX AI":
    st.title("📈 Algoritmo VELIX AI")
    st.text_input("URL do anúncio concorrente:")
    st.button("Executar Otimização")

elif menu == "🧠 Inteligência Estratégica":
    st.title("🧠 Inteligência Estratégica")
    st.text_area("Sua pergunta estratégica:")
    st.button("Consultar IA")

elif menu == "📊 Dashboard de Performance":
    st.title("Painel de Performance")
    st.metric("Vendas Mensais", "R$ 42.850", "+15%")

st.sidebar.markdown("---")
st.sidebar.caption("Daniele Xavier | Gestão de Elite")
