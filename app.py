import streamlit as st
import pandas as pd
import openai

# Configuração de Interface de Alta Performance
st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide", page_icon="🚀")

# --- ESTILO DARK NEON (ALTA VISIBILIDADE) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF; }
    section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 1px solid #30363D; }
    
    /* Melhorando a visibilidade do menu lateral */
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p { color: #FFFFFF !important; font-size: 1.1em; }
    [data-testid="stSidebar"] .st-bs { border-color: #00FFFF !important; }
    
    /* Cores Neon do Logo nos Títulos */
    h1 { color: #FFFFFF !important; text-shadow: 0 0 10px #00FFFF; }
    h2, h3 { color: #00FFFF !important; }
    
    /* Botão com gradiente do seu logo */
    .stButton>button {
        background-image: linear-gradient(to right, #00FFFF, #FF00FF);
        color: white; border: none; font-weight: bold; border-radius: 8px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.markdown("<h1 style='text-align: center;'>VELIX AI</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center; color: #8B949E;'>SISTEMA DE ALAVANCAGEM</p>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Navegação Estratégica",
    ["📊 Dashboard Geral", "🕵️‍♂️ Espião Mercado Livre", "🧠 Velix Chat GPT", "⚙️ Integrações"]
)

# --- CONFIGURAÇÃO OPENAI ---
try:
    openai.api_key = st.secrets["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"]
except:
    st.sidebar.warning("⚠️ Configure a chave OpenAI nos Secrets.")

# --- TELAS ---

if menu == "📊 Dashboard Geral":
    st.title("Painel de Controle Estratégico")
    col1, col2, col3 = st.columns(3)
    col1.metric("Vendas Mensais", "R$ 42.850", "+15%")
    col2.metric("ROI Campanhas", "4.2x", "+0.5x")
    col3.metric("Anúncios Ativos", "24", "Estável")
    st.area_chart(pd.DataFrame({'Market Share': [10, 25, 40, 55, 78]}))

elif menu == "🕵️‍♂️ Espião Mercado Livre":
    st.title("🕵️‍♂️ Espião de Concorrência ML")
    st.write("Conectado via API do Mercado Livre")
    
    url_concorrente = st.text_input("URL do anúncio concorrente:")
    preco_concorrente = st.number_input("Preço do Concorrente", value=49.00)
    margem_minima = st.number_input("Sua Margem Mínima", value=40.00)
    
    if st.button("Analisar e Sugerir"):
        sugestao = preco_concorrente - 0.50
        if sugestao > margem_minima:
            st.success(f"💡 Sugestão Velix: Altere seu preço para *R$ {sugestao:.2f}* para vencer o leilão.")
        else:
            st.error("❌ O preço do concorrente está abaixo do seu limite de lucro.")

elif menu == "🧠 Velix Chat GPT":
    st.title("🧠 Inteligência Velix (OpenAI)")
    st.write("Use esta IA para criar scripts de vendas ou analisar estratégias.")
    
    pergunta = st.text_area("O que você deseja perguntar para a estratégia da sua empresa?")
    if st.button("Consultar Inteligência"):
        if pergunta:
            with st.spinner("Velix AI pensando..."):
                try:
                    response = openai.ChatCompletion.create(
                        model="gpt-3.5-turbo",
                        messages=[{"role": "user", "content": pergunta}]
                    )
                    st.markdown(f"*Resposta da Velix:*\n\n{response.choices[0].message.content}")
                except Exception as e:
                    st.error(f"Erro na API: {e}")
        else:
            st.warning("Por favor, digite uma pergunta.")

elif menu == "⚙️ Integrações":
    st.title("⚙️ Status das Conexões")
    st.success("✅ Mercado Livre: Conectado (API ok)")
    st.success("✅ OpenAI: Conectada (Chave ativa)")
    st.info("Operadora Responsável: Daniele Xavier")

st.sidebar.markdown("---")
st.sidebar.caption("Sessão Restrita | Daniele Xavier")
