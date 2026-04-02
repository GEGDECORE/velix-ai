import streamlit as st

# --- CONFIGURAÇÕES TÉCNICAS (MERCADO LIVRE) ---
CLIENT_ID = "8642953419393317"
REDIRECT_URI = "https://velix-ai.streamlit.app/"

st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# --- DESIGN EXCLUSIVO VELIX (NEON & HIGH-TECH) ---
st.markdown("""
    <style>
    /* Fundo Total Dark */
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    
    /* Menu Lateral Profissional com Borda Ciano */
    section[data-testid="stSidebar"] { 
        background-color: #161B22 !important; 
        border-right: 2px solid #00FFFF; 
    }
    
    /* Texto do Menu Lateral - Branco Puro e Negrito */
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p, 
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] span { 
        color: #FFFFFF !important; 
        font-size: 1.1rem !important; 
        font-weight: 800 !important;
    }

    /* Títulos Neon */
    h1, h2, h3 { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; }
    
    /* Botões Padrão Velix (Ciano p/ Magenta) */
    .stButton>button {
        background-image: linear-gradient(to right, #00FFFF, #FF00FF);
        color: white !important; 
        border: none; 
        font-weight: bold; 
        border-radius: 10px;
        height: 50px;
        width: 100%;
    }
    
    /* Estilo do Logo VELIX AI */
    .logo-velix {
        font-size: 2.8rem !important;
        font-weight: 900 !important;
        color: #00FFFF !important;
        text-align: center;
        text-shadow: 0 0 20px #00FFFF;
        margin-bottom: -10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- ESTRUTURA DO MENU LATERAL ---
st.sidebar.markdown('<p class="logo-velix">VELIX AI</p>', unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #00FFFF; font-weight: bold;'>BUSINESS INTELLIGENCE</p>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "GESTÃO ESTRATÉGICA",
    ["📊 Dashboard de Vendas", "🕵️ Espião de Anúncios", "📈 Algoritmo de Escala", "⚙️ Conectar Mercado Livre"]
)

# --- TELAS ---

if menu == "⚙️ Conectar Mercado Livre":
    st.title("🔗 Integração de Ativos")
    st.write("Sincronize a conta do Mercado Livre para análise de dados em tempo real.")
    
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    
    st.markdown(f'''
        <a href="{auth_url}" target="_blank">
            <button style="width: 100%; background-image: linear-gradient(to right, #00FFFF, #FF00FF); color: white; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer; font-size: 16px;">
                AUTORIZAR ACESSO AO MERCADO LIVRE
            </button>
        </a>
    ''', unsafe_allow_html=True)

elif menu == "📈 Algoritmo de Escala":
    st.title("📈 Inteligência VELIX AI")
    st.write("Utilizando os créditos OpenAI para traçar estratégias de faturamento.")
    pergunta = st.text_input("Qual o objetivo de escala hoje?")
    if st.button("Executar Análise"):
        st.info("O algoritmo está processando os dados do mercado...")

elif menu == "📊 Dashboard de Vendas":
    st.title("📊 Performance da Conta")
    c1, c2, c3 = st.columns(3)
    c1.metric("Vendas Brutas", "R$ 42.850", "+15%")
    c2.metric("Taxa de Cliques", "5.2%", "+0.8%")
    c3.metric("Posicionamento Médio", "Top 10")

else:
    st.title(menu)
    st.write("Aguardando conexão com a API para exibir dados reais.")

st.sidebar.markdown("---")
st.sidebar.caption("Sessão Restrita | VELIX AI 2026")
