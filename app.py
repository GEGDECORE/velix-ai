import sys
import os

sys.path.append(os.path.dirname(_file_))

import streamlit as st
import sqlite3
from openai import OpenAI
import requests
# --- FUNÇÃO PARA CRIAR O BANCO SE ELE NÃO EXISTIR ---
def inicializar_banco():
    with sqlite3.connect('usuarios.db') as conn:
        cursor = conn.cursor()
        # Cria a tabela consumidor com os campos necessários
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS consumidor (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf TEXT UNIQUE NOT NULL,
                status_financeiro TEXT
            )
        """)
        # Adiciona um dado de teste se o banco estiver vazio
        cursor.execute("SELECT COUNT(*) FROM consumidor")
        if cursor.fetchone()[0] == 0:
            cursor.execute("INSERT INTO consumidor (nome, cpf, status_financeiro) VALUES (?, ?, ?)", 
                           ("Cliente Exemplo Enterprise", "35399224828", "Ativo / Premium"))
        conn.commit()

# Chame a função para preparar o terreno
inicializar_banco()

# --- CONFIGURAÇÕES DO APP (Seus dados reais das fotos) ---
CLIENT_ID = "8642952419393317"
CLIENT_SECRET = "puiFotSx7q7I20kcXe3Bg5T6fMKARCQQ"
REDIRECT_URI = "https://localhost:8501."

# --- DESIGN CORPORATIVO VELIX-AI ---
st.set_page_config(page_title="Velix-AI | Enterprise Intelligence", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #000000; color: #ffffff; }
    .main-card { 
        padding: 20px; border-radius: 15px; 
        background: #0a0a0a; border: 1px solid #333;
        box-shadow: 0px 4px 15px rgba(0, 242, 255, 0.1);
    }
    .stButton>button { 
        background: linear-gradient(90deg, #00f2ff, #7000ff); 
        color: white; border: none; font-weight: bold; width: 100%;
        border-radius: 10px; height: 45px;
    }
    input { background-color: #1a1a1a !important; color: white !important; border: 1px solid #333 !important; }
    .ai-box { padding: 15px; border-left: 4px solid #7000ff; background: #0d0d0d; margin-top: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRA LATERAL ---
with st.sidebar:
    st.image("logo.png", width=180)
    st.title("🛡️ Central de Chaves")
    openai_key = st.text_input("OpenAI API Key", type="password")
    st.markdown("---")
    st.caption("ID do App: " + CLIENT_ID)

# --- CABEÇALHO ---
st.title("💼 Velix-AI | Enterprise Dashboard")

# --- 1. MÓDULO DE CONEXÃO MERCADO LIVRE ---
with st.expander("🔗 Integração de Marketplace", expanded=True):
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    
    col_a, col_b = st.columns([2, 1])
    with col_a:
        st.info("Conecte a Velix-AI à conta corporativa para análise de grandes fluxos.")
    with col_b:
        st.markdown(f'<a href="{auth_url}" target="_blank"><button style="width:100%; cursor:pointer; background-color:#00f2ff; border-radius:10px; padding:10px;">Conectar Mercado Livre</button></a>', unsafe_allow_html=True)
    
    codigo_retorno = st.text_input("Cole aqui o código (code) retornado na URL:")

# --- 2. MÓDULO DE BUSCA E INTELIGÊNCIA VENDAFLOW ---
st.markdown("---")
st.subheader("📊 Análise de Performance")

col1, col2 = st.columns([1, 2])

with col1:
    identificador = st.text_input("CPF ou CNPJ do Cliente")
    executar = st.button("EXECUTAR CONSULTA INTELIGENTE")

if executar:
    if identificador:
        try:
            with sqlite3.connect('usuarios.db') as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT nome, status_financeiro FROM consumidor WHERE cpf = ?", (identificador,))
                res = cursor.fetchone()
                
                if res:
                    nome, status = res
                    with col2:
                        st.markdown(f"""
                        <div class="main-card">
                            <h4 style="color:#00f2ff;">Registro Localizado</h4>
                            <p><b>Titular:</b> {nome}</p>
                            <p><b>Status:</b> {status}</p>
                        </div>
                        """, unsafe_allow_html=True)
                        
                        if openai_key:
                            client = OpenAI(api_key=openai_key)
                            with st.spinner("VendaFlow AI gerando estratégia..."):
                                response = client.chat.completions.create(
                                    model="gpt-3.5-turbo",
                                    messages=[{"role": "user", "content": f"Crie uma estratégia B2B para o cliente {nome} com status {status}."}]
                                )
                                st.markdown("##### 🚀 Estratégia VendaFlow AI")
                                st.markdown(f'<div class="ai-box">{response.choices[0].message.content}</div>', unsafe_allow_html=True)
                        else:
                            st.warning("Adicione a chave OpenAI para liberar o Insight de IA.")
                else:
                    st.error("❌ Cliente não localizado no banco Velix-AI.")
        except Exception as e:
            st.error(f"Erro no banco de dados: {e}")

st.markdown("<br><hr>", unsafe_allow_html=True)
st.caption("© 2026 Velix-AI | Enterprise Solutions")
import streamlit as st
from openai import OpenAI

# 🔑 SUA CHAVE OPENAI
client = OpenAI(api_key="SUA_CHAVE_AQUI")

st.markdown("---")
st.title("🤖 Velix AI - Criador de Anúncios Inteligentes")

produto = st.text_input("Nome do produto")
detalhes = st.text_area("Detalhes do produto")

if st.button("🚀 Gerar Anúncio com IA"):
    if produto:
        with st.spinner("Gerando anúncio profissional..."):
            prompt = f"""
            Crie um anúncio profissional para Mercado Livre.

            Produto: {produto}
            Detalhes: {detalhes}

            Gere:
            - Título chamativo
            - Descrição persuasiva
            - Lista de benefícios
            - Palavras-chave SEO
            """

            resposta = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}]
            )

            resultado = resposta.choices[0].message.content
            from modules.ai_engine import gerar_roteiro

            st.success("✅ Anúncio pronto!")
            st.write(resultado)
    else:
        st.warning("Digite o nome do produto")
