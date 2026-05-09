import streamlit as st
import pandas as pd
import os
import time
import requests
from datetime import datetime
from openai import OpenAI

# ==========================================
# 1. CONFIGURAÇÃO E ESTILIZAÇÃO (UI/UX)
# ==========================================
st.set_page_config(page_title="Velix AI PRO", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f8fafc; }
    .stButton>button { border-radius: 8px; font-weight: 600; transition: 0.3s; height: 3em; }
    .card {
        background: white; padding: 20px; border-radius: 12px;
        box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); border: 1px solid #e2e8f0;
        margin-bottom: 15px; color: #1e293b;
    }
    .metric-card { text-align: center; padding: 15px; background: #ffffff; border-radius: 10px; border: 1px solid #e2e8f0; }
    h1, h2, h3 { color: #0f172a; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INICIALIZAÇÃO E FUNÇÕES DE IA
# ==========================================
if "logado" not in st.session_state: st.session_state.logado = False
if "memoria_ia" not in st.session_state: st.session_state.memoria_ia = []
if "ml_token" not in st.session_state: st.session_state.ml_token = None
if "usuario" not in st.session_state: st.session_state.usuario = {}

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def gerar_ia_inteligente(produto, publico, contexto_extra=""):
    historico = "\n".join(st.session_state.memoria_ia[-3:])
    prompt = f"""
    Atue como o motor de vendas Velix AI.
    Histórico Recente: {historico}
    Produto: {produto} | Público: {publico}
    {contexto_extra}
    Gere: Título Magnético, Descrição Persuasiva e CTA Inabalável.
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Você é uma IA de automação de vendas 24h."},
                      {"role": "user", "content": prompt}]
        )
        resultado = response.choices[0].message.content
        st.session_state.memoria_ia.append(f"Venda: {produto}")
        return resultado
    except Exception as e:
        return f"Erro na IA: {e}"

# ==========================================
# 3. INTEGRAÇÃO MERCADO LIVRE
# ==========================================
def criar_produto_ml(token, titulo, preco):
    headers = {"Authorization": f"Bearer {token}", "Content-Type": "application/json"}
    body = {
        "title": titulo, "category_id": "MLB3530", "price": float(preco),
        "currency_id": "BRL", "available_quantity": 10, "buying_mode": "buy_it_now",
        "listing_type_id": "gold_special", "condition": "new",
        "pictures": [{"source": "https://http2.mlstatic.com/D_NQ_NP_2X_12345.jpg"}]
    }
    resp = requests.post("https://api.mercadolibre.com/items", headers=headers, json=body)
    return resp.json()

# ==========================================
# 4. SISTEMA DE LOGIN
# ==========================================
if not st.session_state.logado:
    st.markdown("<h1 style='text-align:center;'>🚀 Velix AI PRO</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,1.5,1])
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        email = st.text_input("📧 Email")
        senha = st.text_input("🔒 Senha", type="password")
        if st.button("🚀 Entrar na Máquina de Vendas", use_container_width=True):
            if email == "admin" and senha == "123":
                st.session_state.logado = True
                st.session_state.usuario = {"nome": "Daniele Xavier", "plano": "PRO", "creditos": 1240}
                st.rerun()
            else: st.error("Credenciais inválidas.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ==========================================
# 5. BARRA LATERAL (SIDEBAR)
# ==========================================
with st.sidebar:
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.markdown("<h2 style='text-align:center;'>VELIX AI</h2>", unsafe_allow_html=True)
    
    st.divider()
    menu = st.radio("Menu Principal", [
        "🏠 Dashboard", "🚀 Criador", "🧠 IA Estratégica", 
        "🕵️ IA Espiã", "📦 Mercado Livre", "🔥 Tendências", 
        "⚡ Automação", "🤖 Avatar", "📊 Analytics", "⚙️ Configurações"
    ])
    
    st.divider()
    st.success(f"Online: {st.session_state.usuario['nome']}")
    st.info(f"Plano: {st.session_state.usuario['plano']}")
    st.progress(0.7, text=f"Créditos: {st.session_state.usuario['creditos']}")

# ==========================================
# 6. CONTEÚDO DAS PÁGINAS
# ==========================================

# --- DASHBOARD ---
if menu == "🏠 Dashboard":
    st.markdown("<h1>Dashboard Operacional</h1>", unsafe_allow_html=True)
    m1, m2, m3, m4 = st.columns(4)
    with m1: st.markdown("<div class='metric-card'><h4>Faturamento</h4><h2>R$ 87.400</h2></div>", unsafe_allow_html=True)
    with m2: st.markdown("<div class='metric-card'><h4>Campanhas</h4><h2>17 Ativas</h2></div>", unsafe_allow_html=True)
    with m3: st.markdown("<div class='metric-card'><h4>ROI</h4><h2>6.8x</h2></div>", unsafe_allow_html=True)
    with m4: st.markdown("<div class='metric-card'><h4>Status IA</h4><h2 style='color:green;'>ON</h2></div>", unsafe_allow_html=True)
    
    st.divider()
    st.markdown("""
    <div class='card'>
        <h3>🔥 Atividade em Tempo Real</h3>
        <ul>
            <li>IA otimizando anúncios automáticos...</li>
            <li>Radar de tendências detectou alta em: <b>Smart Home</b></li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- CRIADOR ---
elif menu == "🚀 Criador":
    st.header("🚀 Criador de Campanhas")
    c1, c2 = st.columns(2)
    prod = c1.text_input("Produto", placeholder="O que vamos vender?")
    pub = c2.text_input("Público", placeholder="Para quem?")
    
    if st.button("✨ Gerar Campanha Pro", use_container_width=True):
        if prod:
            with st.spinner("Velix AI criando estratégia..."):
                res = gerar_ia_inteligente(prod, pub)
                st.markdown(f"<div class='card'><h3>Estratégia Gerada</h3>{res}</div>", unsafe_allow_html=True)
        else: st.warning("Informe o produto.")

# --- IA ESPIÃ ---
elif menu == "🕵️ IA Espiã":
    st.header("🕵️ Inteligência de Mercado")
    alvo = st.text_input("Nicho ou Concorrente para analisar")
    if st.button("Iniciar Espionagem", use_container_width=True):
        with st.spinner("Analisando pontos fracos da concorrência..."):
            analise = gerar_ia_inteligente(alvo, "Análise de Mercado", "Compare com o líder de mercado e dê 3 dicas para superar.")
            st.info(analise)

# --- MERCADO LIVRE ---
elif menu == "📦 Mercado Livre":
    st.header("📦 Integração Mercado Livre PRO")
    if not st.session_state.ml_token:
        st.warning("Mercado Livre não conectado.")
        st.link_button("🔗 Autorizar Integração", f"https://auth.mercadolibre.com.br/authorization?response_type=code&client_id={st.secrets['ML_CLIENT_ID']}&redirect_uri={st.secrets['ML_REDIRECT_URI']}")
    else:
        st.success("✅ Sistema conectado ao Mercado Livre")
        # Aqui entra a lógica de listagem de produtos

# --- AVATAR ---
elif menu == "🤖 Avatar":
    st.header("🤖 Avatar IA de Vendas")
    st.file_uploader("Upload da sua foto/avatar", type=["png", "jpg"])
    st.text_area("Roteiro do Vídeo")
    if st.button("🎬 Gerar Vídeo", use_container_width=True):
        st.info("Processando animação... (Simulação)")
        time.sleep(2)
        st.video("https://assets.mixkit.co/videos/preview/343/343-small.mp4")

# --- OUTROS MENUS (PLACEHOLDERS PROFISSIONAIS) ---
else:
    st.header(f"{menu}")
    st.markdown(f"<div class='card'>Módulo <b>{menu}</b> em operação ativa 24h.</div>", unsafe_allow_html=True)
