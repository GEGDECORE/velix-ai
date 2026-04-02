import streamlit as st
import requests

# --- CONFIGURAÇÃO DE IDENTIDADE DA VELIX AI ---
# ID extraído da sua foto oficial do painel de desenvolvedor
CLIENT_ID = "8642953419393317" 
REDIRECT_URI = "https://velix-ai.streamlit.app/" 

st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# --- RESTAURAÇÃO DO DESIGN NEON E ALTA VISIBILIDADE ---
st.markdown("""
    <style>
    /* Fundo Escuro Profissional */
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    
    /* Menu Lateral com Borda Neon */
    section[data-testid="stSidebar"] { 
        background-color: #161B22 !important; 
        border-right: 2px solid #00FFFF; 
    }
    
    /* Texto do Menu Lateral - Branco Puro e Nítido */
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p, 
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] span { 
        color: #FFFFFF !important; 
        font-size: 1.1rem !important; 
        font-weight: 800 !important;
    }

    /* Títulos em Ciano Neon */
    h1, h2, h3 { color: #00FFFF !important; text-shadow: 0 0 8px #00FFFF; }
    
    /* Botões em Gradiente Velix */
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

# --- MENU LATERAL (NAVEGAÇÃO ESTRATÉGICA) ---
st.sidebar.markdown("<h1 style='text-align: center;'>VELIX AI</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #8892b0;'>SISTEMA DE ALAVANCAGEM</p>", unsafe_allow_html=True)
st.sidebar.write("---")

# Opções de menu conforme solicitado
menu = st.sidebar.radio(
    "Navegação Estratégica",
    ["📊 Dashboard Geral", "🕵️ Espião Mercado Livre", "💬 Velix Chat GPT", "⚙️ Integrações"]
)

# --- TELAS DO SISTEMA ---

if menu == "⚙️ Integrações":
    st.title("🔗 Integração de Ativos")
    st.write("Conecte a conta do cliente para sincronizar produtos e vendas.")
    
    # Link de autenticação real com seu ID
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    
    st.markdown(f'''
        <a href="{auth_url}" target="_blank">
            <button style="width: 100%; background-image: linear-gradient(to right, #00FFFF, #FF00FF); color: white; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 16px;">
                CONECTAR CONTA MERCADO LIVRE
            </button>
        </a>
    ''', unsafe_allow_html=True)
    st.info("Clique no botão acima para autorizar a Velix AI no Mercado Livre.")

elif menu == "💬 Velix Chat GPT":
    st.title("🧠 Inteligência Velix")
    # Verificação de chave nos Secrets
    if "OPENAI_API_KEY" not in st.secrets:
        st.warning("⚠️ Configure sua chave da OpenAI nos 'Secrets' para ativar o chat.")
    else:
        st.write("Inteligência pronta. Como posso ajudar na sua estratégia hoje?")
        st.text_input("Sua pergunta:")
        st.button("Consultar Algoritmo")

elif menu == "📊 Dashboard Geral":
    st.title("Painel de Performance")
    col1, col2 = st.columns(2)
    col1.metric("Vendas Mensais", "R$ 42.850", "+15%")
    col2.metric("Conversão", "5.2%", "+0.8%")

else:
    st.title(menu)
    st.info("Módulo em fase de estruturação de dados.")

st.sidebar.markdown("---")
st.sidebar.caption("Daniele Xavier | Gestão de Elite")
