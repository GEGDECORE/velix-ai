import streamlit as st
import pandas as pd
import os
import time
import requests
from datetime import datetime
from openai import OpenAI

# ==========================================
# 1. CONFIGURAÇÃO VISUAL DE ALTO NÍVEL
# ==========================================
st.set_page_config(page_title="Velix AI PRO - Vendas 24h", page_icon="🚀", layout="wide")

st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;700;900&display=swap');
    * { font-family: 'Inter', sans-serif; }
    .main { background-color: #f8fafc; }
    .stButton>button { 
        background: linear-gradient(90deg, #0f172a 0%, #334155 100%); 
        color: white; border: none; border-radius: 12px; font-weight: 800;
        height: 3.5em; transition: 0.4s; width: 100%;
    }
    .stButton>button:hover { transform: scale(1.02); box-shadow: 0 10px 20px rgba(0,0,0,0.1); }
    .card {
        background: white; padding: 25px; border-radius: 16px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.05); border: 1px solid #e2e8f0;
        margin-bottom: 20px;
    }
    .status-badge { background: #dcfce7; color: #166534; padding: 6px 15px; border-radius: 30px; font-size: 13px; font-weight: bold; }
</style>
""", unsafe_allow_html=True)

# ==========================================
# 2. INICIALIZAÇÃO E CÉREBRO DA IA
# ==========================================
if "logado" not in st.session_state: st.session_state.logado = False
if "ml_token" not in st.session_state: st.session_state.ml_token = None
if "usuario" not in st.session_state: st.session_state.usuario = {}

client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def sniper_vendas_ia(produto, publico):
    """Gera conteúdo de altíssima conversão para o Mercado Livre"""
    prompt = f"""
    Você é o VELIX AI PRO. Crie uma estratégia de vendas imbatível.
    PRODUTO: {produto} | PÚBLICO: {publico}
    ENTREGA:
    - Título SEO Premium (Max 60 caracteres)
    - Descrição com Gatilhos Mentais (AIDA)
    - 5 Tags de busca de alta intenção de compra
    - 1 Dica estratégica de precificação ou kit
    """
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "system", "content": "Estrategista de E-commerce e Growth Hacking."},
                      {"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"Erro na Inteligência Velix: {e}"

# ==========================================
# 3. PORTAL DE ACESSO (SaaS)
# ==========================================
if not st.session_state.logado:
    st.markdown("<h1 style='text-align:center; padding-top: 40px;'>🚀 VELIX AI PRO</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align:center; color:#64748b;'>Faça login na sua central de automação e lucro</p>", unsafe_allow_html=True)
    
    col1, col2, col3 = st.columns([1,1.3,1])
    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        email_login = st.text_input("📧 Email Registrado")
        senha_login = st.text_input("🔒 Senha de Acesso", type="password")
        
        if st.button("ATIVAR MINHA MÁQUINA DE VENDAS"):
            if email_login == "admin" and senha_login == "123":
                st.session_state.logado = True
                st.session_state.usuario = {
                    "nome": "Daniele Xavier", 
                    "email": email_login, 
                    "plano": "PRO ELITE", 
                    "creditos": 2500
                }
                st.rerun()
            else:
                st.error("Usuário ou senha inválidos.")
        st.markdown("</div>", unsafe_allow_html=True)
    st.stop()

# ==========================================
# 4. DASHBOARD E NAVEGAÇÃO
# ==========================================
with st.sidebar:
    # Correção do Logo: Tenta carregar logo.png da raiz
    if os.path.exists("logo.png"):
        st.image("logo.png", use_container_width=True)
    else:
        st.markdown("<h1 style='text-align:center; color:#0f172a;'>VELIX AI</h1>", unsafe_allow_html=True)
    
    st.divider()
    menu = st.radio("Painel Estratégico", [
        "🏠 Home Dashboard", "🚀 Criador Sniper", "🧠 IA Estratégica", 
        "🕵️ IA Espiã", "📦 Mercado Livre PRO", "🔥 Radar de Tendências", 
        "⚡ Automação 24h", "🤖 Avatar Vendedor", "📊 Analytics ROI"
    ])
    
    st.divider()
    st.markdown(f"👤 *{st.session_state.usuario['nome']}*")
    st.markdown(f"🏆 Plano: <span class='status-badge'>{st.session_state.usuario['plano']}</span>", unsafe_allow_html=True)
    st.progress(0.9, text=f"Créditos: {st.session_state.usuario['creditos']}")

# ==========================================
# 5. CONTEÚDO DINÂMICO
# ==========================================

if menu == "🏠 Home Dashboard":
    st.title("Performance Operacional")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Vendas Mensais", "R$ 87.400", "+34%")
    c2.metric("Conversão", "5.2%", "Acima da média")
    c3.metric("ROI Geral", "7.1x", "Excelente")
    c4.metric("Status IA", "ONLINE", "24h")

    st.markdown("""
    <div class='card'>
        <h3>🔥 Atividade da Velix Agora</h3>
        <p>• Monitorando 145 produtos no Mercado Livre.</p>
        <p>• Otimizando descrições de anúncios com baixa conversão.</p>
        <p>• 🟢 <b>Oportunidade:</b> Tendência de alta detectada no nicho de <b>Cozinha Luxo</b>.</p>
    </div>
    """, unsafe_allow_html=True)

elif menu == "🚀 Criador Sniper":
    st.header("🚀 Criador Sniper: Anúncios que Vendem")
    with st.container():
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        col_p, col_a = st.columns(2)
        p_nome = col_p.text_input("📦 Nome do Produto", placeholder="Ex: Mangueira de Gás Blindada")
        p_alvo = col_a.text_input("🎯 Público Alvo", placeholder="Ex: Donas de casa, Instaladores")
        
        if st.button("GERAR ESTRATÉGIA DE ELITE"):
            if p_nome:
                with st.spinner("Velix AI processando milhões de dados de conversão..."):
                    resultado = sniper_vendas_ia(p_nome, p_alvo)
                    st.markdown(f"### 📋 Estratégia Gerada\n{resultado}")
            else:
                st.warning("Por favor, informe o produto.")
        st.markdown("</div>", unsafe_allow_html=True)

elif menu == "📦 Mercado Livre PRO":
    st.header("📦 Mercado Livre: Automação Total")
    if not st.session_state.ml_token:
        st.warning("Sua conta ainda não está sincronizada para vendas automáticas.")
        # Link de conexão que usa seu e-mail e secrets
        auth_url = f"https://auth.mercadolibre.com.br/authorization?response_type=code&client_id={st.secrets['ML_CLIENT_ID']}&redirect_uri={st.secrets['ML_REDIRECT_URI']}"
        st.link_button("🔗 CONECTAR COM MERCADO LIVRE", auth_url)
    else:
        st.success("✅ Conectado como: " + st.session_state.usuario['email'])

elif menu == "🤖 Avatar Vendedor":
    st.header("🤖 Avatar Humano Digital")
    st.write("Crie um vendedor que fala e apresenta seu produto 24h.")
    st.file_uploader("Suba a imagem do seu avatar", type=['jpg', 'png'])
    st.text_area("Roteiro do Vídeo (copywriting)")
    if st.button("GERAR VÍDEO PUBLICITÁRIO"):
        st.info("Renderizando humano digital via Velix Engine...")
        time.sleep(3)
        st.video("https://assets.mixkit.co/videos/preview/343/343-small.mp4")

# Mantém as outras abas com visual profissional
else:
    st.header(f"Módulo: {menu}")
    st.markdown(f"<div class='card'>O módulo <b>{menu}</b> está otimizando seus dados para máxima performance.</div>", unsafe_allow_html=True)
