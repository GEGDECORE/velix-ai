import streamlit as st
import pandas as pd
from openai import OpenAI

# Configuração de Interface
st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# --- ESTILO DE ALTA VISIBILIDADE (LETRAS BRANCAS E NÍTIDAS) ---
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 1px solid #00FFFF; }
    
    /* FORÇAR LETRAS DO MENU PARA BRANCO PURO */
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p, 
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] span { 
        color: #FFFFFF !important; 
        font-size: 1.1rem !important; 
        font-weight: 700 !important;
    }

    /* Métrica e Números Neon */
    [data-testid="stMetricValue"] { color: #00FFFF !important; font-weight: bold !important; }
    h1, h2, h3 { color: #00FFFF !important; }

    /* Botão Gradiente */
    .stButton>button {
        background-image: linear-gradient(to right, #00FFFF, #FF00FF);
        color: white !important; border: none; font-weight: bold; border-radius: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- MENU LATERAL ---
st.sidebar.markdown("<h1 style='text-align: center; color: white !important;'>VELIX AI</h1>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio(
    "Navegação Estratégica",
    ["📊 Dashboard Geral", "🕵️‍♂️ Espião Mercado Livre", "🧠 Velix Chat GPT"]
)

# --- LÓGICA DA INTELIGÊNCIA (VERSÃO V1 ATUALIZADA) ---
if menu == "🧠 Velix Chat GPT":
    st.title("🧠 Inteligência Velix")
    
    if "OPENAI_API_KEY" in st.secrets:
        client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
        
        pergunta = st.text_input("O que deseja perguntar para a estratégia do seu cliente?")
        
        if st.button("Consultar IA"):
            if pergunta:
                with st.spinner("Analisando..."):
                    try:
                        # NOVO FORMATO DE COMANDO DA OPENAI
                        completion = client.chat.completions.create(
                            model="gpt-3.5-turbo",
                            messages=[{"role": "user", "content": pergunta}]
                        )
                        st.markdown(f"### Resposta da Velix:\n{completion.choices[0].message.content}")
                    except Exception as e:
                        st.error(f"Erro na conexão: {e}")
            else:
                st.warning("Digite uma pergunta primeiro.")
    else:
        st.error("⚠️ Chave OpenAI não encontrada nos Secrets.")

elif menu == "📊 Dashboard Geral":
    st.title("Painel de Controle Estratégico")
    col1, col2, col3 = st.columns(3)
    col1.metric("Vendas Mensais", "R$ 42.850", "+15%")
    col2.metric("ROI Campanhas", "4.2x", "+0.5x")
    col3.metric("Anúncios Ativos", "24")

elif menu == "🕵️‍♂️ Espião Mercado Livre":
    st.title("🕵️‍♂️ Espião Mercado Livre")
    st.info("Ferramenta de monitoramento de preços ativado.")
    url = st.text_input("Cole o link do concorrente:")
    if st.button("Analisar Topo"):
        st.write("Analisando dados do anúncio...")

st.sidebar.markdown("---")
st.sidebar.caption("Daniele Xavier | Gestão de Elite")
