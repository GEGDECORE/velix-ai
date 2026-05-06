import streamlit as st
import pandas as pd
import os
from openai import OpenAI

# ==========================================
# CONFIGURAÇÃO DA PÁGINA (Sempre a primeira linha)
# ==========================================
st.set_page_config(page_title="Velix AI GOLD", page_icon="🚀", layout="wide")

# ==========================================
# ESTILIZAÇÃO CSS (CORREÇÃO DE CORES E MENU)
# ==========================================
st.markdown("""
    <style>
    /* Fundo geral */
    .stApp { background-color: #ffffff; }
    
    /* Menu Lateral Escuro com Letras Brancas */
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #0f172a, #1e293b) !important;
    }
    [data-testid="stSidebar"] * {
        color: white !important;
    }
    
    /* Cartões de Conteúdo */
    .card {
        background: #f8fafc;
        padding: 20px;
        border-radius: 15px;
        border: 1px solid #e2e8f0;
        margin-bottom: 15px;
        color: #1e293b;
    }
    
    /* Títulos */
    h1, h2, h3 { color: #0f172a !important; }
    
    /* Botões */
    .stButton>button {
        border-radius: 8px;
        background-color: #2563eb;
        color: white !important;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# CONEXÃO COM APIs (SECRETS)
# ==========================================
try:
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    ML_ID = st.secrets["ML_CLIENT_ID"]
except:
    st.error("Chaves de API não encontradas nas Secrets.")
    st.stop()

# ==========================================
# FUNÇÕES DE APOIO
# ==========================================
def gerar_conteudo(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except:
        return "Erro ao conectar com a IA. Verifique seu saldo na OpenAI."

# ==========================================
# MENU LATERAL
# ==========================================
with st.sidebar:
    st.markdown("## 🚀 Velix AI GOLD")
    st.divider()
    menu = st.radio("Navegação", [
        "🏠 Dashboard", 
        "🎨 Criador PRO", 
        "🕵️ IA Espiã", 
        "📄 Landing Pages", 
        "🧠 Mentalidade Elite", 
        "📦 Mercado Livre", 
        "🤖 Avatar IA", 
        "📊 Analytics", 
        "⚙️ Configurações"
    ])
    st.divider()
    st.markdown("● Status: *Ativo*")
    st.markdown("● Plano: *Business Gold*")

# ==========================================
# TELAS DO SISTEMA
# ==========================================

if menu == "🏠 Dashboard":
    st.title("Bem-vinda ao seu Império, Daniele! 🚀")
    col1, col2, col3 = st.columns(3)
    col1.metric("Vendas Estimadas", "R$ 12.450", "+15%")
    col2.metric("Anúncios Monitorados", "42", "Ativos")
    col3.metric("Análise de Nicho", "98%", "Excelente")
    
    st.markdown("<div class='card'><h3>Resumo da Semana</h3><p>Sua IA reprecificou 12 itens e gerou 5 novas landing pages com alto ROI.</p></div>", unsafe_allow_html=True)

elif menu == "🎨 Criador PRO":
    st.title("🎨 Criador de Campanhas & Imagens")
    produto = st.text_input("Qual o produto?")
    publico = st.text_input("Para quem vamos vender?")
    
    c1, c2 = st.columns(2)
    if c1.button("✨ Gerar Texto de Venda"):
        texto = gerar_conteudo(f"Crie um anúncio persuasivo para {produto} focado em {publico}.")
        st.markdown(f"<div class='card'>{texto}</div>", unsafe_allow_html=True)
    
    if c2.button("📸 Gerar Foto de Catálogo (DALL-E)"):
        st.info("Conectando com DALL-E para gerar imagem real...")
        # Simulação de placeholder para visualização imediata
        st.image("https://img.freepik.com/fotos-gratis/renderizacao-3d-de-um-produto-de-podio_23-2150411132.jpg", caption="Sugestão de Estilo de Imagem")

elif menu == "📄 Landing Pages":
    st.title("📄 Gerador de Landing Pages")
    nome_p = st.text_input("Nome do Produto")
    if st.button("🛠️ Criar Código da Página"):
        html_code = gerar_conteudo(f"Crie apenas o código HTML e CSS de uma landing page moderna para {nome_p}.")
        st.code(html_code, language="html")
        st.success("Código gerado! Copie e cole no seu publicador.")

elif menu == "🧠 Mentalidade Elite":
    st.title("🧠 Mentalidade de Alta Performance")
    pergunta = st.text_area("O que está travando seu crescimento hoje?")
    if st.button("🧘 Obter Orientação TRLI"):
        resposta = gerar_conteudo(f"Aja como uma mentora de alta performance. Responda com foco em destravar o empreendedor: {pergunta}")
        st.markdown(f"<div class='card' style='border-left: 5px solid #2563eb;'>{resposta}</div>", unsafe_allow_html=True)

elif menu == "📦 Mercado Livre":
    st.title("📦 Integração Mercado Livre")
    st.markdown("""
    <div class='card'>
        <h3>Conectar sua Conta</h3>
        <p>Clique no botão abaixo para autorizar o Velix AI a gerenciar seus anúncios e perguntas.</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("🔗 Conectar ao Mercado Livre"):
        st.write(f"Redirecionando para autenticação... (App ID: {ML_ID})")
        st.info("Link de autorização gerado com sucesso.")

elif menu == "🤖 Avatar IA":
    st.title("🤖 Gerador de Vídeos com Avatar")
    upload = st.file_uploader("Suba sua foto", type=['jpg', 'png'])
    roteiro = st.text_area("O que o avatar deve dizer?")
    if st.button("🎬 Renderizar Vídeo"):
        if upload and roteiro:
            st.success("Processando vídeo com IA...")
            st.video("https://www.w3schools.com/html/mov_bbb.mp4") # Exemplo de player
        else:
            st.warning("Por favor, suba uma foto e digite o roteiro.")

elif menu == "📊 Analytics":
    st.title("📊 Relatórios de Performance")
    data = {"Data": ["01/05", "02/05", "03/05", "04/05"], "Vendas": [1200, 1500, 1100, 1900]}
    df = pd.DataFrame(data)
    st.line_chart(df.set_index("Data"))
    st.markdown("<div class='card'>Seu faturamento cresceu 22% desde que a Velix IA começou a monitorar os preços.</div>", unsafe_allow_html=True)

elif menu == "⚙️ Configurações":
    st.title("⚙️ Configurações do Sistema")
    st.text_input("Seu Nome Profissional", value="Daniele Xavier")
    st.text_input("Link de Redirecionamento (ML)", value="https://velix-ai.streamlit.app")
    st.checkbox("Reprecificação Automática Ativa")
    st.checkbox("Notificações no WhatsApp")
    st.button("Salvar Preferências")
