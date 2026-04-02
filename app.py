import streamlit as st
import requests

# --- CONFIGURAÇÃO DA DANIELE ---
# Copie o número que aparece abaixo do nome 'Daniele' na sua tela do ML e cole abaixo:
CLIENT_ID = "8642953419393317" 
REDIRECT_URI = "https://velix-ai.streamlit.app/" 

# Configuração de Interface
st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# --- ESTILO VISUAL PROFISSIONAL ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 2px solid #00FFFF; }
    
    /* Menu Lateral Nitidez Total */
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

# --- MENU LATERAL ---
st.sidebar.markdown("<h1 style='text-align: center;'>VELIX AI</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>SISTEMA DE ALAVANCAGEM</p>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Navegação Estratégica",
    ["📊 Dashboard Geral", "📈 Espião Mercado Livre", "🧠 Velix Chat GPT", "🔗 Integrações"]
)

# --- TELAS ---

if menu == "🔗 Integrações":
    st.title("🔗 Integração de Ativos")
    st.write("Conecte a conta do cliente para sincronizar produtos e vendas.")
    
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    
    st.markdown(f'''
        <a href="{auth_url}" target="_blank">
            <button style="width: 100%; background-image: linear-gradient(to right, #00FFFF, #FF00FF); color: white; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 16px;">
                CONECTAR CONTA MERCADO LIVRE
            </button>
        </a>
    ''', unsafe_allow_html=True)
    st.info("Após clicar, autorize o acesso na página oficial do Mercado Livre.")

elif menu == "🧠 Velix Chat GPT":
    st.title("🧠 Inteligência Velix")
    st.warning("⚠️ Erro detectado: Saldo insuficiente na OpenAI (Quota Exceeded). Adicione créditos para ativar.")

else:
    st.title(menu)
    st.info("Módulo em fase de sincronização de dados.")

st.sidebar.markdown("---")
st.sidebar.caption("Sessão Restrita | Daniele Xavier")
