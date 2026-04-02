import streamlit as st

# --- CONFIGURAÇÕES DE IDENTIDADE VELIX AI ---
# ID real da Daniele extraído do painel de desenvolvedor
CLIENT_ID = "8642953419393317"
REDIRECT_URI = "https://velix-ai.streamlit.app/"

st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# --- O DESIGN DE ELITE (NEON & BRANCO) ---
st.markdown("""
    <style>
    /* Fundo Escuro Profissional */
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    
    /* Menu Lateral Azul Petróleo/Preto com Borda Neon */
    section[data-testid="stSidebar"] { 
        background-color: #161B22 !important; 
        border-right: 2px solid #00FFFF; 
    }
    
    /* Menu Lateral - Texto Branco Puro e Nítido */
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p, 
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] span { 
        color: #FFFFFF !important; 
        font-size: 1.1rem !important; 
        font-weight: 800 !important;
    }

    /* Títulos em Ciano Neon */
    h1, h2, h3 { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; font-family: 'Inter', sans-serif; }
    
    /* Botões Gradiente Velix (Ciano para Magenta) */
    .stButton>button {
        background-image: linear-gradient(to right, #00FFFF, #FF00FF);
        color: white !important; 
        border: none; 
        font-weight: bold; 
        border-radius: 10px;
        padding: 10px 20px;
        width: 100%;
    }
    
    /* Logo no Topo do Menu */
    .logo-text {
        font-size: 2.5rem !important;
        font-weight: 900 !important;
        color: #00FFFF !important;
        text-align: center;
        margin-bottom: 0px;
        text-shadow: 0 0 15px #00FFFF;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL (A IDENTIDADE DA FERRAMENTA) ---
st.sidebar.markdown('<p class="logo-text">VELIX AI</p>', unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #8892b0; font-size: 0.8rem;'>TERAPEUTA DE ALTA PERFORMANCE</p>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Navegação Estratégica",
    ["📊 Dashboard de Performance", "🕵️ Espião Mercado Livre", "💬 Velix Chat GPT", "⚙️ Integrações de Ativos"]
)

# --- FUNCIONALIDADES DAS TELAS ---

if menu == "⚙️ Integrações de Ativos":
    st.title("🔗 Integração de Ativos")
    st.write("Conecte a conta do seu cliente para que o algoritmo Velix comece a análise.")
    
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    
    st.markdown(f'''
        <a href="{auth_url}" target="_blank">
            <button style="width: 100%; background-image: linear-gradient(to right, #00FFFF, #FF00FF); color: white; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 16px;">
                CONECTAR CONTA MERCADO LIVRE
            </button>
        </a>
    ''', unsafe_allow_html=True)
    st.info("O sistema abrirá o portal oficial do Mercado Livre para autorização.")

elif menu == "💬 Velix Chat GPT":
    st.title("🧠 Velix Chat GPT")
    if "OPENAI_API_KEY" not in st.secrets:
        st.error("⚠️ Erro: Chave da OpenAI não configurada nos Secrets do Streamlit.")
    else:
        st.write("Sua Inteligência de Alta Performance está online.")
        pergunta = st.text_input("Qual estratégia de escala vamos traçar hoje?")
        if st.button("Consultar Algoritmo"):
            st.info("Processando análise baseada nos créditos adicionados...")

elif menu == "📊 Dashboard de Performance":
    st.title("📊 Dashboard de Performance")
    col1, col2, col3 = st.columns(3)
    col1.metric("Faturamento", "R$ 42.850", "+15%")
    col2.metric("Conversão", "5.2%", "+0.8%")
    col3.metric("ROI Médio", "4.5x", "+1.2x")

else:
    st.title(menu)
    st.write("Módulo em fase de sincronização de dados.")

st.sidebar.markdown("---")
st.sidebar.caption("Daniele Xavier | Gestão de Elite")
