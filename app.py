import streamlit as st
import pandas as pd
import os
import time
import requests
from datetime import datetime
from openai import OpenAI

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(page_title="Velix AI PRO", page_icon="🚀", layout="wide")

# ==========================================
# INICIALIZAÇÃO E SEGURANÇA
# ==========================================
if "logado" not in st.session_state: st.session_state["logado"] = False
if "memoria_ia" not in st.session_state: st.session_state.memoria_ia = []
if "historico" not in st.session_state: st.session_state.historico = []

try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    ML_CLIENT_ID = st.secrets["ML_CLIENT_ID"]
    ML_CLIENT_SECRET = st.secrets["ML_CLIENT_SECRET"]
    ML_REDIRECT_URI = st.secrets["ML_REDIRECT_URI"]
except KeyError as e:
    st.error(f"Configuração ausente: {e}")
    st.stop()

# ==========================================
# FUNÇÕES CORE (IA & INTEGRAÇÕES)
# ==========================================

def gerar_ia(prompt, sistema="Você é a Velix AI, assistente de e-commerce e alta performance."):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": sistema},
                {"role": "user", "content": prompt}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na IA: {e}"

def criar_landing_page_ia(produto, oferta):
    prompt = f"Crie o código HTML/CSS de uma Landing Page de alta conversão para o produto {produto}. Oferta: {oferta}. Inclua gatilhos de escassez e design moderno azul e branco."
    return gerar_ia(prompt, "Você é um desenvolvedor Web focado em conversão.")

def reprecificador_ia(preco_atual, preco_concorrente, margem_minima):
    # Lógica de negócio: baixar 0.10 centavos se estiver acima da margem
    novo_preco = preco_concorrente - 0.10
    if novo_preco >= margem_minima:
        return round(novo_preco, 2), "✅ Preço ajustado para ganhar a Buy Box."
    return preco_atual, "⚠️ Preço não ajustado (abaixo da margem mínima)."

# ==========================================
# INTERFACE E CSS
# ==========================================
st.markdown("""
    <style>
    .stApp { background:#f8fafc; }
    [data-testid="stSidebar"] { background: linear-gradient(180deg, #0f172a, #1e293b) !important; }
    .card { background: white; padding: 20px; border-radius: 15px; box-shadow: 0 4px 6px -1px rgb(0 0 0 / 0.1); margin-bottom: 15px; color: #1e293b; }
    .status-ok { color: #22c55e; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# LOGIN
# ==========================================
if not st.session_state["logado"]:
    st.markdown("<h1 style='text-align:center;'>🚀 Velix AI PRO</h1>", unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        email = st.text_input("📧 Email")
        senha = st.text_input("🔒 Senha", type="password")
        if st.button("🚀 Acessar Sistema", use_container_width=True):
            if email == "admin" and senha == "123":
                st.session_state["logado"] = True
                st.session_state["usuario"] = {"nome": "Daniele Xavier", "plano": "GOLD"}
                st.rerun()
    st.stop()

# ==========================================
# MENU LATERAL
# ==========================================
st.sidebar.title("Velix AI PRO")
menu = st.sidebar.radio("Navegação", [
    "🏠 Dashboard", "🚀 Criador PRO", "🕵️ IA Espiã (Ativa)", 
    "📄 Landing Pages", "🧠 Mentalidade Elite", "📦 Mercado Livre", 
    "🤖 Avatar IA", "📊 Analytics", "⚙️ Configurações"
])

# ==========================================
# LÓGICA DOS MENUS
# ==========================================

if menu == "🏠 Dashboard":
    st.title(f"Bem-vinda, {st.session_state.usuario['nome']}! 🚀")
    m1, m2, m3 = st.columns(3)
    m1.metric("Vendas Hoje", "R$ 4.250", "+12%")
    m2.metric("Anúncios Ativos", "84", "Prontos")
    m3.metric("ROI Médio", "5.8x", "+0.4")
    
    st.markdown("""
    <div class='card'>
        <h3>🔥 Atividades do Velix Agora</h3>
        <p>• Monitorando 15 concorrentes no Mercado Livre<br>
        • Gerando 3 campanhas para Instagram<br>
        • Otimizando Landing Pages de alta conversão</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "🚀 Criador PRO":
    st.header("🚀 Criador de Campanhas & Imagens")
    prod = st.text_input("Qual o produto?")
    pub = st.text_input("Para quem vamos vender?")
    
    c1, c2 = st.columns(2)
    if c1.button("✨ Gerar Campanha Completa"):
        res = gerar_ia(f"Crie Título, Descrição e Legenda para {prod} focado em {pub}.")
        st.markdown(f"<div class='card'>{res}</div>", unsafe_allow_html=True)
    
    if c2.button("📸 Gerar Foto de Catálogo IA"):
        st.info("Gerando imagem realista via DALL-E 3... (Simulado no MVP)")
        st.image("https://via.placeholder.com/400x400.png?text=Imagem+Gerada+pela+Velix", width=300)

elif menu == "🕵️ IA Espiã (Ativa)":
    st.header("🕵️ Monitoramento e Reprecificador Automático")
    st.write("A Velix monitora seus concorrentes e ajusta seu preço em tempo real.")
    
    col_e1, col_e2 = st.columns(2)
    p_atual = col_e1.number_input("Seu Preço (R$)", value=100.0)
    p_conc = col_e2.number_input("Preço Concorrente (R$)", value=98.0)
    margem = st.number_input("Sua Margem Mínima (R$)", value=85.0)
    
    if st.button("⚡ Executar Reprecificação Inteligente"):
        novo, msg = reprecificador_ia(p_atual, p_conc, margem)
        st.subheader(f"Novo Preço Sugerido: R$ {novo}")
        st.info(msg)

elif menu == "📄 Landing Pages":
    st.header("📄 Gerador de Landing Pages (One-Click)")
    nome_p = st.text_input("Nome do Produto para a Página")
    promo = st.text_input("Qual a oferta principal? (Ex: 50% de desconto)")
    
    if st.button("🛠️ Construir Página de Vendas"):
        with st.spinner("Velix codificando sua página..."):
            codigo = criar_landing_page_ia(nome_p, promo)
            st.code(codigo, language='html')
            st.success("Copiado! Basta colar no seu domínio.")

elif menu == "🧠 Mentalidade Elite":
    st.header("🧠 Alta Performance para Vendedores (Método Daniele Xavier)")
    st.write("Dúvidas sobre o negócio ou precisa de foco? A Velix aplica seu DNA de terapeuta aqui.")
    pergunta = st.text_area("Como você está se sentindo em relação ao seu progresso hoje?")
    
    if st.button("🧘 Obter Orientação de Performance"):
        insight = gerar_ia(pergunta, "Você é uma IA mentora em Alta Performance, usando o método de Daniele Xavier. Foque em destravar o emocional do empreendedor.")
        st.markdown(f"<div class='card' style='border-left: 5px solid #172554;'>{insight}</div>", unsafe_allow_html=True)

elif menu == "🤖 Avatar IA":
    st.header("🤖 Gerador de Vídeos com Avatar")
    st.file_uploader("Suba sua foto ou de um modelo")
    st.text_area("Roteiro para o Avatar falar")
    if st.button("🎬 Renderizar Vídeo"):
        st.video("https://assets.mixkit.co/videos/preview/343/343-small.mp4")

# ==========================================
# SIDEBAR STATUS
# ==========================================
st.sidebar.divider()
st.sidebar.markdown("### 🟢 Status Velix")
st.sidebar.write("• Inteligência: *Ativa*")
st.sidebar.write("• Reprecificador: *Rodando*")
st.sidebar.write("• Plano: *Gold Member*")
