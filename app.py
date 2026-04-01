import streamlit as st
import pandas as pd

# Configuração de Interface de Alta Performance
st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide", page_icon="📈")

# Estilização DARK MODE PROFISSIONAL (Preto e Azul Royal)
st.markdown("""
    <style>
    /* Fundo Total Preto */
    .stApp {
        background-color: #0E1117;
        color: #FFFFFF;
    }
    /* Menu Lateral Dark */
    section[data-testid="stSidebar"] {
        background-color: #161B22 !important;
        border-right: 1px solid #30363D;
    }
    /* Títulos e Métricas */
    h1, h2, h3 {
        color: #58A6FF !important;
        font-family: 'Inter', sans-serif;
    }
    .stMetric {
        background-color: #1C2128;
        padding: 15px;
        border-radius: 10px;
        border: 1px solid #30363D;
    }
    /* Botões de Ação */
    .stButton>button {
        background-color: #238636;
        color: white;
        border: none;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #2EA043;
    }
    </style>
    """, unsafe_allow_html=True)

# --- NAVEGAÇÃO E LOGO ---
st.sidebar.markdown(f"<h1 style='text-align: center; color: white !important;'>VELIX AI</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; font-size: 0.8em;'>SISTEMA DE ALAVANCAGEM DE VENDAS</p>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Navegação Estratégica",
    ["📊 Dashboard de Performance", "🔍 Algoritmo de Topo", "🎥 Produção IA", "📢 Gestão de ADS", "📋 Ordens de Serviço", "⚙️ Configurações"]
)

# --- LÓGICA DAS TELAS (SEM NOMES PESSOAIS NA TELA PRINCIPAL) ---

if menu == "📊 Dashboard de Performance":
    st.markdown("<h1>Painel de Controle Estratégico</h1>", unsafe_allow_html=True)
    st.write("Monitoramento em tempo real dos seus ativos digitais.")
    
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        st.metric("Volume de Vendas", "R$ 42.850", "+15%")
    with col2:
        st.metric("CTR de Anúncios", "6.2%", "+1.4%")
    with col3:
        st.metric("ROI Médio", "4.2x", "+0.5x")
    with col4:
        st.metric("Posição Média", "1º Lugar", "Estável")

    st.write("---")
    st.subheader("📈 Gráfico de Escala de Mercado")
    chart_data = pd.DataFrame({'Market Share': [10, 15, 12, 25, 40, 55, 78]})
    st.area_chart(chart_data)

elif menu == "🔍 Algoritmo de Topo":
    st.markdown("<h1>Otimizador de Marketplace</h1>", unsafe_allow_html=True)
    st.info("O algoritmo analisa o preço do concorrente e ajusta sua oferta para o topo em milissegundos.")
    
    c1, c2 = st.columns(2)
    with c1:
        concorrente = st.number_input("Preço Atual do Concorrente (R$)", value=49.00)
    with c2:
        custo = st.number_input("Seu Custo de Operação (R$)", value=35.00)
    
    if st.button("Executar Reajuste de Topo"):
        sugestao = concorrente - 0.50
        if sugestao > custo:
            st.success(f"Estratégia Aplicada: Novo preço ajustado para *R$ {sugestao:.2f}*. Você está no topo!")
        else:
            st.error("Preço do concorrente abaixo da sua margem de segurança.")

elif menu == "📋 Ordens de Serviço":
    st.markdown("<h1>Gestão de OS</h1>", unsafe_allow_html=True)
    with st.form("os_form"):
        st.text_input("Cliente / Empresa")
        st.selectbox("Serviço", ["Consultoria SEO", "Campanha ADS", "Produção de Vídeo IA", "Otimização de Preços"])
        st.date_input("Data de Entrega")
        if st.form_submit_button("Gerar Ordem de Serviço Profissional"):
            st.info("Gerando documento...")

# --- RODAPÉ DISCRETO ---
st.sidebar.markdown("---")
st.sidebar.caption("Sessão Restrita")
# O seu nome fica apenas aqui, bem discreto, para não atrapalhar apresentações aos clientes
st.sidebar.markdown("<p style='font-size: 0.7em; color: gray;'>Operadora: Daniele Xavier</p>", unsafe_allow_html=True)
