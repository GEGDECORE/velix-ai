import streamlit as st
import pandas as pd
import openai

# Configuração de Interface
st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# --- ESTILO DE ALTA VISIBILIDADE (FORÇANDO BRANCO E NEON) ---
st.markdown("""
    <style>
    /* Fundo Preto Profundo */
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    
    /* MENU LATERAL - FORÇANDO TEXTO BRANCO */
    section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 1px solid #00FFFF; }
    
    /* Títulos do Menu Lateral */
    section[data-testid="stSidebar"] h1, section[data-testid="stSidebar"] p { color: #FFFFFF !important; }
    
    /* Opções do Menu (As letras que estavam escuras) */
    [data-testid="stSidebar"] .st-at, [data-testid="stSidebar"] label p {
        color: #FFFFFF !important; 
        font-size: 1.1rem !important;
        font-weight: 600 !important;
    }
    
    /* Números das Métricas (Dashboard) - Ciano Neon para destacar */
    [data-testid="stMetricValue"] { color: #00FFFF !important; font-size: 2rem !important; font-weight: bold !important; }
    [data-testid="stMetricLabel"] p { color: #FFFFFF !important; font-size: 1rem !important; }
    [data-testid="stMetricDelta"] { color: #FF00FF !important; } /* Magenta para as porcentagens */

    /* Títulos Principais */
    h1, h2, h3 { color: #00FFFF !important; text-shadow: 0 0 5px #00FFFF; }

    /* Botão Gradiente */
    .stButton>button {
        background-image: linear-gradient(to right, #00FFFF, #FF00FF);
        color: white !important; border: none; font-weight: bold; border-radius: 10px; padding: 0.5rem 1rem;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTEÚDO ---
st.sidebar.markdown("<h1 style='text-align: center;'>VELIX AI</h1>", unsafe_allow_html=True)
st.sidebar.markdown("<p style='text-align: center;'>SISTEMA DE ALAVANCAGEM</p>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Navegação Estratégica",
    ["📊 Dashboard Geral", "🕵️‍♂️ Espião Mercado Livre", "🧠 Velix Chat GPT"]
)

if menu == "📊 Dashboard Geral":
    st.title("Painel de Controle Estratégico")
    col1, col2, col3 = st.columns(3)
    # Aqui os números ficarão em Ciano Neon bem brilhante
    col1.metric("Vendas Mensais", "R$ 42.850", "+15%")
    col2.metric("ROI Campanhas", "4.2x", "+0.5x")
    col3.metric("Anúncios Ativos", "24", "Estável")
    
    st.write("---")
    st.subheader("Crescimento de Mercado")
    chart_data = pd.DataFrame({'Escala': [10, 25, 45, 60, 90]})
    st.line_chart(chart_data)

elif menu == "🕵️‍♂️ Espião Mercado Livre":
    st.title("🕵️‍♂️ Espião Mercado Livre")
    st.write("Insira o link para análise de topo.")
    url = st.text_input("URL do Concorrente:")
    if st.button("Rastrear e Superar"):
        st.info("Conectando ao Mercado Livre...")

elif menu == "🧠 Velix Chat GPT":
    st.title("🧠 Inteligência Velix")
    pergunta = st.text_input("O que deseja perguntar para a estratégia do seu cliente?")
    if st.button("Consultar IA"):
        if "OPENAI_API_KEY" in st.secrets:
            openai.api_key = st.secrets["OPENAI_API_KEY"]
            response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": pergunta}])
            st.write(response.choices[0].message.content)
        else:
            st.error("Por favor, configure a chave no menu Secrets.")

st.sidebar.markdown("---")
st.sidebar.caption("Operadora: Daniele Xavier")
