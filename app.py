import streamlit as st
import pandas as pd
from openai import OpenAI
import time
import requests

# ==========================================
# CONFIGURAÇÃO DA PÁGINA
# ==========================================
st.set_page_config(
    page_title="Velix AI PRO",
    page_icon="🚀",
    layout="wide"
)

# ==========================================
# CSS PREMIUM (SAAS PROFISSIONAL)
# ==========================================
st.markdown("""
<style>

.stApp{
    background:#f4f7fb;
}

[data-testid="stSidebar"]{
    background:linear-gradient(180deg,#020617,#0f172a,#1e293b)!important;
    border-right:1px solid rgba(255,255,255,0.08);
}

[data-testid="stSidebar"] *{
    color:white!important;
}

.block-container{
    padding-top:2rem;
}

.main-title{
    font-size:48px;
    font-weight:800;
    color:#0f172a;
    margin-bottom:0;
}

.subtitle{
    color:#64748b;
    font-size:18px;
    margin-top:0;
}

.card{
    background:white;
    padding:24px;
    border-radius:18px;
    border:1px solid #e2e8f0;
    box-shadow:0 8px 30px rgba(15,23,42,0.05);
    margin-bottom:18px;
}

.metric-card{
    background:white;
    padding:20px;
    border-radius:18px;
    border:1px solid #e2e8f0;
    box-shadow:0 8px 25px rgba(15,23,42,0.05);
}

.metric-title{
    color:#64748b;
    font-size:14px;
    font-weight:600;
}

.metric-value{
    font-size:34px;
    font-weight:800;
    color:#0f172a;
}

.metric-green{
    color:#16a34a;
    font-size:13px;
}

h1,h2,h3{
    color:#0f172a!important;
}

.stButton>button{
    width:100%;
    border-radius:12px;
    border:none;
    background:linear-gradient(90deg,#2563eb,#4f46e5);
    color:white!important;
    font-weight:700;
    padding:14px;
    font-size:15px;
}

.stTextInput input,
.stTextArea textarea{
    border-radius:12px!important;
}

.chat-box{
    background:white;
    padding:18px;
    border-radius:16px;
    border:1px solid #e2e8f0;
}

</style>
""", unsafe_allow_html=True)

# ==========================================
# OPENAI
# ==========================================
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

# ==========================================
# FUNÇÃO IA
# ==========================================
def gerar_ia(prompt):

    try:

        resposta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role":"system",
                    "content":"Você é a Velix AI, especialista em vendas, copywriting, automação, Mercado Livre e redes sociais."
                },
                {
                    "role":"user",
                    "content":prompt
                }
            ]
        )

        return resposta.choices[0].message.content

    except Exception as e:
        return f"Erro na IA: {e}"

# ==========================================
# LOGIN
# ==========================================
if "logado" not in st.session_state:
    st.session_state.logado = False

def tela_login():

    st.markdown("""
    <div style='text-align:center;padding-top:40px;'>
        <h1 class='main-title'>🚀 Velix AI PRO</h1>
        <p class='subtitle'>Sua máquina de vendas inteligente</p>
    </div>
    """, unsafe_allow_html=True)

    col1,col2,col3 = st.columns([1,1.2,1])

    with col2:

        st.markdown("<div class='card'>", unsafe_allow_html=True)

        email = st.text_input("📧 E-mail")
        senha = st.text_input("🔒 Senha", type="password")

        if st.button("Entrar na Plataforma"):

            if email and senha:

                st.session_state.logado = True

                st.session_state.usuario = {
                    "nome":"Daniele Xavier",
                    "email":email,
                    "plano":"PRO",
                    "creditos":1240
                }

                st.success("Login realizado com sucesso!")
                time.sleep(1)
                st.rerun()

            else:
                st.error("Preencha email e senha")

        st.markdown("</div>", unsafe_allow_html=True)

if not st.session_state.logado:
    tela_login()
    st.stop()

# ==========================================
# SIDEBAR
# ==========================================
with st.sidebar:

    # LOGO
    st.image(
        "https://gegdecore-velix-ai.streamlit.app/image_8.png",
        use_container_width=True
    )

    st.markdown("## 🚀 VELIX AI PRO")
    st.caption("Automação • IA • Marketplace")

    st.divider()

    usuario = st.session_state.usuario

    st.markdown(f"""
    <div class='card' style='background:rgba(255,255,255,0.05);border:none;'>
        <h4 style='color:white;margin:0;'>{usuario["nome"]}</h4>
        <p style='color:#cbd5e1;margin:0;font-size:13px;'>{usuario["email"]}</p>
        <br>
        <p style='color:white;margin:0;'>Plano: <b>{usuario["plano"]}</b></p>
        <p style='color:white;margin:0;'>Créditos: <b>{usuario["creditos"]}</b></p>
    </div>
    """, unsafe_allow_html=True)

    menu = st.radio(
        "Menu",
        [
            "🏠 Dashboard",
            "🎨 Criador PRO",
            "📱 Conteúdo Redes Sociais",
            "🕵️ IA Espiã",
            "📄 Landing Pages",
            "📦 Mercado Livre",
            "⚡ Automação 24h",
            "🤖 Avatar IA",
            "💬 Chat Velix GPT",
            "📊 Analytics",
            "⚙️ Configurações"
        ]
    )

# ==========================================
# DASHBOARD
# ==========================================
if menu == "🏠 Dashboard":

    st.markdown("""
    <h1 class='main-title'>🚀 Velix AI PRO</h1>
    <p class='subtitle'>Sistema inteligente de vendas automáticas</p>
    """, unsafe_allow_html=True)

    c1,c2,c3,c4 = st.columns(4)

    with c1:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-title'>Faturamento</div>
            <div class='metric-value'>R$ 87k</div>
            <div class='metric-green'>+34% este mês</div>
        </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-title'>Campanhas</div>
            <div class='metric-value'>17</div>
            <div class='metric-green'>Ativas agora</div>
        </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-title'>Conversão</div>
            <div class='metric-value'>6.8x</div>
            <div class='metric-green'>ROI médio</div>
        </div>
        """, unsafe_allow_html=True)

    with c4:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-title'>Status IA</div>
            <div class='metric-value' style='color:#16a34a;'>ONLINE</div>
            <div class='metric-green'>Sistema ativo</div>
        </div>
        """, unsafe_allow_html=True)

    st.divider()

    st.markdown("""
    <div class='card'>
        <h3>🔥 O que a Velix faz automaticamente</h3>

        ✅ Cria campanhas de vendas<br><br>

        ✅ Gera conteúdo para Instagram e TikTok<br><br>

        ✅ Analisa concorrentes automaticamente<br><br>

        ✅ Sugere preços inteligentes<br><br>

        ✅ Responde clientes no Mercado Livre<br><br>

        ✅ Cria páginas de alta conversão<br><br>

        ✅ Automatiza vendas 24 horas
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# CRIADOR
# ==========================================
elif menu == "🎨 Criador PRO":

    st.title("🎨 Criador de Campanhas")

    produto = st.text_input("Produto")
    publico = st.text_input("Público-alvo")

    if st.button("🚀 Gerar Campanha Completa"):

        prompt = f"""
        Crie uma campanha profissional de vendas para:

        Produto: {produto}
        Público: {publico}

        Gere:
        - Título
        - Descrição
        - CTA
        - Copy emocional
        - Estratégia de venda
        """

        resultado = gerar_ia(prompt)

        st.markdown(
            f"<div class='card'>{resultado}</div>",
            unsafe_allow_html=True
        )

# ==========================================
# CONTEÚDO REDES SOCIAIS
# ==========================================
elif menu == "📱 Conteúdo Redes Sociais":

    st.title("📱 Conteúdo para Redes Sociais")

    nicho = st.text_input("Seu nicho")
    objetivo = st.selectbox(
        "Objetivo",
        [
            "Vender",
            "Engajar",
            "Atrair clientes",
            "Autoridade",
            "Viralizar"
        ]
    )

    if st.button("🔥 Criar Conteúdo Inteligente"):

        prompt = f"""
        Crie conteúdo viral para Instagram/TikTok.

        Nicho: {nicho}
        Objetivo: {objetivo}

        Gere:
        - Legenda
        - CTA
        - Hashtags
        - Ideia de vídeo
        - Gancho forte
        """

        resultado = gerar_ia(prompt)

        st.markdown(
            f"<div class='card'>{resultado}</div>",
            unsafe_allow_html=True
        )

# ==========================================
# IA ESPIÃ
# ==========================================
elif menu == "🕵️ IA Espiã":

    st.title("🕵️ IA Espiã")

    concorrente = st.text_input("Link ou produto do concorrente")

    if st.button("Analisar Concorrência"):

        prompt = f"""
        Analise concorrentes do produto:

        {concorrente}

        Gere:
        - Pontos fortes
        - Pontos fracos
        - Estratégia para vencer
        - Melhor preço
        - Melhor copy
        """

        resultado = gerar_ia(prompt)

        st.markdown(
            f"<div class='card'>{resultado}</div>",
            unsafe_allow_html=True
        )

# ==========================================
# LANDING PAGE
# ==========================================
elif menu == "📄 Landing Pages":

    st.title("📄 Landing Pages")

    objetivo = st.text_input("Objetivo da página")

    if st.button("Construir Landing Page"):

        prompt = f"""
        Gere uma landing page profissional para:

        {objetivo}

        Gere:
        - Headline
        - Sessões
        - CTA
        - Estrutura persuasiva
        """

        resultado = gerar_ia(prompt)

        st.code(resultado)

# ==========================================
# MERCADO LIVRE
# ==========================================
elif menu == "📦 Mercado Livre":

    st.title("📦 Mercado Livre PRO")

    st.markdown("""
    <div class='card'>
    Conecte sua conta para:

    ✅ Responder clientes automaticamente<br><br>
    ✅ Criar anúncios com IA<br><br>
    ✅ Ajustar preços automaticamente<br><br>
    ✅ Monitorar concorrentes<br><br>
    ✅ Automatizar vendas 24h
    </div>
    """, unsafe_allow_html=True)

    st.button("🔗 Conectar Mercado Livre")

# ==========================================
# AUTOMAÇÃO
# ==========================================
elif menu == "⚡ Automação 24h":

    st.title("⚡ Automação Inteligente")

    st.success("Sistema ativo e rodando")

    st.markdown("""
    <div class='card'>

    🤖 Respondendo clientes automaticamente<br><br>

    📦 Monitorando produtos em alta<br><br>

    💰 Ajustando preços inteligentes<br><br>

    🧠 Gerando conteúdo automaticamente<br><br>

    🚀 Otimizando anúncios
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# AVATAR
# ==========================================
elif menu == "🤖 Avatar IA":

    st.title("🤖 Avatar IA")

    foto = st.file_uploader(
        "Envie sua foto",
        type=["png","jpg","jpeg"]
    )

    roteiro = st.text_area("Roteiro do vídeo")

    if st.button("🎬 Gerar Vídeo"):

        if foto:

            with st.spinner("Criando avatar..."):
                time.sleep(3)

            st.success("Vídeo gerado!")

        else:
            st.warning("Envie uma foto")

# ==========================================
# CHAT GPT INTERNO
# ==========================================
elif menu == "💬 Chat Velix GPT":

    st.title("💬 Chat Velix GPT")

    if "chat_velix" not in st.session_state:
        st.session_state.chat_velix = []

    for m in st.session_state.chat_velix:
        st.chat_message(m["role"]).write(m["content"])

    pergunta = st.chat_input("Digite sua pergunta")

    if pergunta:

        st.session_state.chat_velix.append({
            "role":"user",
            "content":pergunta
        })

        resposta = gerar_ia(pergunta)

        st.session_state.chat_velix.append({
            "role":"assistant",
            "content":resposta
        })

        st.rerun()

# ==========================================
# ANALYTICS
# ==========================================
elif menu == "📊 Analytics":

    st.title("📊 Analytics")

    c1,c2,c3 = st.columns(3)

    c1.metric("Vendas", "R$ 12.400", "+22%")
    c2.metric("Conversão", "3.2%")
    c3.metric("ROI", "5.8x")

    df = pd.DataFrame({
        "Vendas":[10,20,40,80,150,230]
    })

    st.line_chart(df)

# ==========================================
# CONFIGURAÇÕES
# ==========================================
elif menu == "⚙️ Configurações":

    st.title("⚙️ Configurações")

    nome = st.text_input(
        "Nome",
        value=usuario["nome"]
    )

    whatsapp = st.text_input("WhatsApp")

    if st.button("Salvar Configurações"):

        st.success("Configurações salvas!")

# ==========================================
# STATUS FINAL
# ==========================================
st.sidebar.divider()

st.sidebar.success("🟢 Sistema online")
st.sidebar.success("🧠 IA ativa")
st.sidebar.success("🚀 Velix operacional")

st.sidebar.markdown("""
<div style='text-align:center;
font-size:12px;
color:#94a3b8;
margin-top:15px;'>

VELIX AI PRO<br>
Sistema inteligente de automação

</div>
""", unsafe_allow_html=True)
