import streamlit as st
import pandas as pd
from pymongo import MongoClient

# Configuração da Página - Estilo Profissional
st.set_page_config(page_title="VELIX AI - Central de Vendas", layout="wide", page_icon="🚀")

# Estilização Customizada (CSS)
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 5px; background-color: #004aad; color: white; }
    .sidebar .sidebar-content { background-image: linear-gradient(#2e3192, #1bffff); color: white; }
    h1 { color: #004aad; }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL (Idêntico à sua foto) ---
st.sidebar.image("https://via.placeholder.com/150?text=VELIX+AI", width=120) # Coloque seu logo aqui depois
st.sidebar.title("Menu VELIX AI")
menu = st.sidebar.radio(
    "Navegação",
    ["🏠 Painel de Controle", "💰 Vendas IA", "🎥 Vídeo IA", "👤 Avatar IA", "📢 Anúncios (ADS)", "📞 Atendimento", "📊 Resultados"]
)

st.sidebar.info(f"Logada como: *Daniele Xavier*")

# --- CONEXÃO MONGODB (Seu motor de dados) ---
# Substitua pela sua string de conexão real quando tiver
# client = MongoClient("SUA_URL_DO_MONGODB")
# db = client.velix_db

# --- LÓGICA DAS TELAS ---

if menu == "🏠 Painel de Controle":
    st.title("🚀 Central de Vendas Inteligente")
    st.subheader("Bem-vinda de volta, Daniele Xavier")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Vendas Hoje", "R$ 1.250,00", "+12%")
    col2.metric("Alcance de Anúncios", "45.200", "+5%")
    col3.metric("Conversão", "4.8%", "+0.2%")
    
    st.write("---")
    st.write("### 📈 Monitoramento em Tempo Real")
    st.info("O algoritmo está monitorando 15 produtos da sua carteira neste momento.")

elif menu == "💰 Vendas IA":
    st.title("💰 Estratégia de Vendas e Precificação")
    st.write("### Otimizador de Topo de Busca")
    
    with st.expander("Calcular Preço para Vencer Concorrente", expanded=True):
        preco_concorrente = st.number_input("Qual o preço do concorrente no Marketplace?", value=49.00)
        trava_lucro = st.number_input("Qual seu preço mínimo de lucro (Trava)?", value=40.00)
        
        if preco_concorrente > trava_lucro:
            sugestao = preco_concorrente - 0.50
            st.success(f"✅ Sugestão VELIX: Altere seu preço para *R$ {sugestao:.2f}* para ficar no topo.")
        else:
            st.warning("⚠️ Atenção: O preço do concorrente está abaixo da sua trava de lucro. Não baixe mais!")

    st.write("### 🧠 SEO e Palavras-Chave de Ouro")
    st.text_area("Descreva o produto para gerar palavras-chave que o algoritmo ama:")
    if st.button("Gerar Palavras-Chave de Alta Performance"):
        st.write("🔍 Sugestão: Melhor custo-benefício, Oferta Relâmpago, Entrega Rápida, Garantia Total")

elif menu == "🎥 Vídeo IA":
    st.title("🎥 Vídeo IA para Anúncios")
    st.write("Crie vídeos rápidos para Reels e TikTok que convertem.")
    st.file_uploader("Suba o vídeo do seu produto aqui")
    st.button("Adicionar Legendas Magnéticas e Voz de IA")

elif menu == "👤 Avatar IA":
    st.title("👤 Avatar Humano Apresentador")
    st.write("Transforme seu roteiro em um vídeo com apresentador realista.")
    roteiro = st.text_area("Escreva o que o avatar deve falar:")
    st.select_slider("Escolha o tom de voz:", options=["Vendedor", "Autoridade", "Amigável"])
    st.button("Gerar Vídeo de Apresentação")

elif menu == "📢 Anúncios (ADS)":
    st.title("📢 Gerador de Campanhas")
    st.write("Crie criativos para Meta e Google Ads em segundos.")
    publico = st.multiselect("Público Alvo:", ["Empresários", "Estética", "Vendas Online", "Autônomos"])
    if st.button("Criar Copy para Anúncio"):
        st.code("⚠️ ÚLTIMAS VAGAS: Pare de perder clientes para o preço do vizinho. Com a VELIX AI...")

elif menu == "📊 Resultados":
    st.title("📊 Relatórios de Performance")
    # Exemplo de gráfico
    chart_data = pd.DataFrame({'Vendas': [10, 20, 15, 30, 45, 50, 80]})
    st.line_chart(chart_data)
    st.write("Seu crescimento nos últimos 7 dias foi de *40%* acima da média do setor.")

# Rodapé profissional
st.write("---")
st.caption("VELIX AI - Alta Performance em Vendas | Desenvolvido para Daniele Xavier")
