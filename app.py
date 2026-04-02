import streamlit as st

# DADOS DA DANIELE
CLIENT_ID = "8642953419393317"
REDIRECT_URI = "https://velix-ai.streamlit.app/"

st.set_page_config(page_title="VELIX AI | Business", layout="wide")

# DESIGN NEON PROFISSIONAL
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 2px solid #00FFFF; }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p, 
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] span { color: #FFFFFF !important; font-size: 1.1rem !important; font-weight: 800 !important; }
    h1, h2, h3 { color: #00FFFF !important; text-shadow: 0 0 10px #00FFFF; }
    .stButton>button { background-image: linear-gradient(to right, #00FFFF, #FF00FF); color: white !important; border: none; font-weight: bold; border-radius: 10px; width: 100%; height: 50px; }
    .logo-velix { font-size: 2.8rem; font-weight: 900; color: #00FFFF; text-align: center; text-shadow: 0 0 20px #00FFFF; }
    </style>
    """, unsafe_allow_html=True)

# MENU LATERAL
st.sidebar.markdown('<p class="logo-velix">VELIX AI</p>', unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #00FFFF;'>SISTEMA DE ALAVANCAGEM</p>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Navegação Estratégica",
    ["📊 Dashboard Geral", "🕵️ Espião Mercado Livre", "💬 Velix Chat GPT", "⚙️ Integrações"]
)

if menu == "⚙️ Integrações":
    st.title("🔗 Conectar Mercado Livre")
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    st.markdown(f'<a href="{auth_url}" target="_blank"><button>CONECTAR CONTA AGORA</button></a>', unsafe_allow_html=True)

elif menu == "🕵️ Espião Mercado Livre":
    st.title("🕵️ Espião de Anúncios")
    st.write("Insira o link do concorrente para analisar a performance.")
    st.text_input("Link do Anúncio:")
    st.button("Analisar Concorrência")

elif menu == "💬 Velix Chat GPT":
    st.title("🧠 Inteligência Velix")
    st.write("Pronta para usar com seus créditos OpenAI.")
    st.text_area("O que vamos escalar hoje?")
    st.button("Consultar Algoritmo")

else:
    st.title("📊 Painel de Performance")
    st.metric("Faturamento Alvo", "R$ 50.000", "+20%")
