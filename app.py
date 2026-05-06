import streamlit as st
import pandas as pd
from openai import OpenAI

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="Velix AI", page_icon="🚀", layout="wide")

# ==========================================
# ESTILIZAÇÃO CSS (MENU ESCURO / TEXTO CLARO)
# ==========================================
st.markdown("""
    <style>
    .stApp { background-color: #ffffff; }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a, #1e293b) !important;
    }
    [data-testid="stSidebar"] * { color: white !important; }
    .card {
        background: #f8fafc;
        padding: 20px;
        border-radius: 12px;
        border: 1px solid #e2e8f0;
        margin-bottom: 15px;
        color: #1e293b;
    }
    h1, h2, h3 { color: #0f172a !important; }
    .stButton>button {
        border-radius: 8px;
        background-color: #2563eb;
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# CONEXÃO COM API
# ==========================================
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def gerar_ia(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except:
        return "Erro de conexão. Verifique sua chave API."

# ==========================================
# MENU LATERAL COM O SEU LOGO
# ==========================================
with st.sidebar:
    # Busca o logo da sua estrutura original
    st.image("https://gegdecore-velix-ai.streamlit.app/image_8.png", use_container_width=True)
    st.markdown("### VELIX AI PRO")
    st.divider()
    menu = st.radio("Navegação", [
        "🏠 Início", 
        "🎨 Criador PRO", 
        "🕵️ IA Espiã", 
        "📄 Landing Pages", 
        "🧠 Mentalidade Elite", 
        "📦 Mercado Livre", 
        "🤖 Avatar IA", 
        "📊 Analytics", 
        "⚙️ Configurações"
    ])

# ==========================================
# TELAS CORRIGIDAS
# ==========================================

if menu == "🏠 Início":
    st.title("🚀 Bem-vindo ao VELIX AI")
    st.subheader("Sua IA trabalhando 24hs por você")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Status", "Ativo", "Online")
    col2.metric("Processamento", "IA 4.0", "Turbo")
    col3.metric("Faturamento Monitorado", "R$ 0,00", "0%")

elif menu == "🎨 Criador PRO":
    st.title("🎨 Criador de Campanhas")
    produto = st.text_input("Nome do seu produto ou nicho")
    if st.button("Gerar Estratégia Completa"):
        resultado = gerar_ia(f"Crie uma copy de vendas irresistível para {produto}.")
        st.markdown(f"<div class='card'>{resultado}</div>", unsafe_allow_html=True)
    
    st.divider()
    st.subheader("📸 Gerador de Imagem de Produto")
    st.info("A integração com DALL-E criará imagens reais aqui assim que o comando for enviado.")

elif menu == "🕵️ IA Espiã":
    st.title("🕵️ IA Espiã")
    link = st.text_input("Cole o link do anúncio do concorrente")
    if st.button("Analisar Concorrente"):
        analise = gerar_ia(f"Analise como superar este concorrente do nicho: {link}")
        st.write(analise)

elif menu == "📄 Landing Pages":
    st.title("📄 Gerador de Landing Pages")
    niche = st.text_input("Qual o objetivo da página?")
    if st.button("Construir Estrutura Profissional"):
        codigo = gerar_ia(f"Gere o código HTML/CSS de uma landing page de alta conversão para {niche}. Entregue apenas o código.")
        st.code(codigo, language="html")

elif menu == "📦 Mercado Livre":
    st.title("📦 Integração Mercado Livre")
    st.markdown("<div class='card'>Conecte sua conta para que a Velix AI gerencie preços e responda clientes automaticamente.</div>", unsafe_allow_html=True)
    st.button("🔗 Conectar Conta Mercado Livre")

elif menu == "🤖 Avatar IA":
    st.title("🤖 Gerador de Avatar")
    st.write("Suba sua foto para criar seu avatar falante.")
    st.file_uploader("Escolha a foto do seu avatar", type=['png', 'jpg'])
    st.text_area("Roteiro que o avatar deve falar")
    if st.button("Gerar Vídeo"):
        st.info("Processando animação via IA...")

elif menu == "⚙️ Configurações":
    st.title("⚙️ Configurações do Sistema")
    st.text_input("Seu Nome Profissional", value="Daniele Xavier")
    st.text_input("WhatsApp de Suporte", placeholder="+55...")
    st.button("Salvar Preferências")
