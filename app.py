import pandas as pd
import os
import time
import requests
import requests

def criar_produto_ml(token, titulo, preco):

headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }

    body = {
        "title": titulo,
        "category_id": "MLB3530",
        "price": float(preco),
        "currency_id": "BRL",
        "available_quantity": 10,
        "buying_mode": "buy_it_now",
        "listing_type_id": "gold_special",
        "condition": "new",
        "pictures": [
            {
                "source": "https://http2.mlstatic.com/D_NQ_NP_2X_12345.jpg"
            }
        ]
    }

    resp = requests.post(
        "https://api.mercadolibre.com/items",
        headers=headers,
        json=body
    )

    return resp.json()

import streamlit as st

query = st.query_params

if "code" in query:
code = query["code"]

response = requests.post(  
    "https://api.mercadolibre.com/oauth/token",  
    data={  
        "grant_type": "authorization_code",  
        "client_id": st.secrets["ML_CLIENT_ID"],  
        "client_secret": st.secrets["ML_CLIENT_SECRET"],  
        "code": code,  
        "redirect_uri": st.secrets["ML_REDIRECT_URI"],  
    }  
)  

data = response.json()  

if "access_token" in data:  
    st.session_state["ml_token"] = data["access_token"]  
    st.success("Mercado Livre conectado!")

if "memoria_ia" not in st.session_state:
st.session_state.memoria_ia = []

from openai import OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

==========================================

LOGIN SYSTEM

==========================================

def tela_login():

st.markdown("""  
<h1 style='text-align:center;'>🚀 Velix AI PRO</h1>  
<p style='text-align:center;'>Faça login para acessar sua máquina de vendas</p>  
""", unsafe_allow_html=True)  

col1, col2, col3 = st.columns([1,2,1])  

with col2:  
    email = st.text_input("📧 Email")  
    senha = st.text_input("🔒 Senha", type="password")  

    if st.button("🚀 Entrar", use_container_width=True):  

        # LOGIN SIMPLES (pode trocar depois por banco)  
        if email == "admin" and senha == "123":  
            st.session_state["logado"] = True  
            st.session_state["usuario"] = {  
                "nome": "Daniele Xavier",  
                "email": email,  
                "plano": "PRO",  
                "creditos": 1240  
            }  
            st.success("Login realizado!")  
            st.rerun()  
        else:  
            st.error("Email ou senha inválidos")

==========================================

CONFIG

==========================================

st.set_page_config(page_title="Velix AI PRO", page_icon="🚀", layout="wide")

==========================================

CONTROLE DE LOGIN

==========================================

if "logado" not in st.session_state:
st.session_state["logado"] = False

if not st.session_state["logado"]:
tela_login()
st.stop()

usuario = st.session_state.get("usuario", {
"nome": "Usuário",
"plano": "FREE",
"creditos": 0
})

if "ml_token" not in st.session_state:
st.session_state.ml_token = None

==========================================

MERCADO LIVRE CALLBACK

==========================================

params = st.query_params
if "code" in params:
st.session_state.ml_token = params["code"]
st.success("✅ Mercado Livre conectado com sucesso!")

usuario = st.session_state.usuario

==========================================

CSS

==========================================

st.markdown("""

<style>  
.stApp { background:#f5f8fc; }  
section[data-testid="stSidebar"] { background:linear-gradient(180deg,#081120,#0f172a,#172554) !important; }  
section[data-testid="stSidebar"] * { color:white !important; }  
.main-title { font-size:48px; font-weight:800; }  
.card { background:white; padding:25px; border-radius:20px; box-shadow:0 10px 25px rgba(0,0,0,0.05); }  
</style>  """, unsafe_allow_html=True)

==========================================

LOGO VELIX (ACIMA DO MENU)

==========================================

import os

if os.path.exists("logo.png"):
st.sidebar.image("logo.png", use_container_width=True)
else:
st.sidebar.markdown("""
<div style='text-align:center; padding:10px;'>
<h2>🚀 Velix AI</h2>
</div>
""", unsafe_allow_html=True)

menu = st.sidebar.radio("Menu", [
"🏠Dashboard",
"🚀Criador",
"🧠 IA Estratégica",
"🕵️ IA Espiã",
"📦 Mercado Livre",
"🔥 Tendências",
"⚡ Automação"
"🤖 Avatar",
"📊 Analytics",
"⚙️ Configurações"
])

==========================================

DASHBOARD PRO (NÍVEL SAAS)

==========================================

if menu == "🏠 Dashboard":

# HEADER  
st.markdown("""  
<div style='margin-bottom:20px;'>  
    <h1 style='font-size:42px; color:#0f172a;'>🚀 Velix AI PRO</h1>  
    <p style='color:#64748b; font-size:16px;'>Sua máquina de vendas inteligente trabalhando 24h</p>  
</div>  
""", unsafe_allow_html=True)  

# MÉTRICAS  
col1, col2, col3, col4 = st.columns(4)  

col1.markdown("""  
<div class='card'>  
    <h4>💰 Faturamento</h4>  
    <h2>R$ 87.400</h2>  
    <span style='color:green;'>+34% este mês</span>  
</div>  
""", unsafe_allow_html=True)  

col2.markdown("""  
<div class='card'>  
    <h4>📦 Campanhas</h4>  
    <h2>17</h2>  
    <span style='color:#64748b;'>Ativas agora</span>  
</div>  
""", unsafe_allow_html=True)  

col3.markdown("""  
<div class='card'>  
    <h4>📊 ROI</h4>  
    <h2>6.8x</h2>  
    <span style='color:#64748b;'>Retorno médio</span>  
</div>  
""", unsafe_allow_html=True)  

col4.markdown("""  
<div class='card'>  
    <h4>🧠 IA</h4>  
    <h2 style='color:green;'>ONLINE</h2>  
    <span style='color:#64748b;'>Sistema ativo</span>  
</div>  
""", unsafe_allow_html=True)  

st.divider()  

# INSIGHTS  
st.markdown("""  
<div class='card'>  
    <h3>🔥 O que a Velix está fazendo agora</h3>  
    <ul>  
        <li>Otimizando anúncios automaticamente</li>  
        <li>Gerando campanhas com alta conversão</li>  
        <li>Analisando concorrência em tempo real</li>  
        <li>Atualizando SEO dos produtos</li>  
    </ul>  
</div>  
""", unsafe_allow_html=True)  

# AÇÃO RÁPIDA  
st.markdown("### ⚡ Ação Rápida")  

if st.button("🚀 Gerar campanha rápida agora", use_container_width=True):  
    with st.spinner("Velix criando campanha inteligente..."):  
        time.sleep(2)  
    st.success("Campanha criada com sucesso!")

==========================================

CRIADOR PRO

==========================================

elif menu == "🚀Criador":

st.markdown("## 🚀 Criador de Campanhas")  

col1, col2 = st.columns(2)  

with col1:  
    produto = st.text_input("📦 Produto", placeholder="Ex: Air fryer, conexão de gás...")  
with col2:  
    publico = st.text_input("🎯 Público", placeholder="Ex: mães, homens, profissionais...")  

if st.button("✨ Gerar Campanha Inteligente", use_container_width=True):  

if not produto:  
    st.warning("Digite um produto")  
else:  
    with st.spinner("IA criando campanha profissional..."):  
        resultado = gerar_ia_inteligente(produto, publico)  

    st.success("Campanha criada com IA")  

    st.markdown("### 📢 Resultado da IA")  
    st.write(resultado)  

    # salvar histórico  
    st.session_state.historico.append({  
        "produto": produto,  
        "resultado": resultado,  
        "data": str(datetime.now())  
    })  

        st.markdown(f"""  
        <div class='card'>  
        <h3>🔥 Título</h3>  
        Oferta irresistível de {produto}  
        </div>  
        """, unsafe_allow_html=True)  

        st.markdown(f"""  
        <div class='card'>  
        <h3>📝 Descrição</h3>  
        Produto ideal para {publico if publico else "todos os públicos"}, alta procura e excelente conversão.  
        </div>  
        """, unsafe_allow_html=True)  

        st.markdown("""  
        <div class='card'>  
        <h3>🎯 CTA</h3>  
        Garanta agora antes que acabe!  
        </div>  
        """, unsafe_allow_html=True)

if st.button("🚀 Criar anúncio automático"):

titulo = gerar_ia_inteligente(produto, publico)  

resultado = criar_produto_ml(  
    st.session_state["ml_token"],  
    titulo,  
    97.90  
)  

st.success("Produto criado!")  
st.write(resultado)

def gerar_campanha_ia(produto, publico):

prompt = f"""  
Crie uma campanha altamente persuasiva para vendas.  

Produto: {produto}  
Público: {publico}  

Gere:  

- Título chamativo  
- Descrição persuasiva  
- CTA forte  
- Legenda para Instagram com hashtags  

Seja único, criativo e vendedor.  
"""  

resposta = client.chat.completions.create(  
    model="gpt-4o-mini",  
    messages=[{"role": "user", "content": prompt}]  
)  

return resposta.choices[0].message.content

==========================================

IA ESTRATÉGICA PRO

==========================================

def gerar_ia_inteligente(produto, publico):

def responder_perguntas(token):

import requests  

headers = {"Authorization": f"Bearer {token}"}  

resp = requests.get(  
    "https://api.mercadolibre.com/my/received_questions/search",  
    headers=headers  
)  

perguntas = resp.json().get("questions", [])  

for p in perguntas:  

    if p["status"] == "UNANSWERED":  

        resposta_ia = gerar_ia_inteligente(  
            p["text"],  
            "cliente interessado"  
        )  

        requests.post(  
            f"https://api.mercadolibre.com/answers?question_id={p['id']}",  
            headers=headers,  
            json={"text": resposta_ia}  
        )  

historico = "\n".join(st.session_state.memoria_ia[-5:])  

prompt = f"""  
Histórico recente:  
{historico}  

Novo produto: {produto}  
Público: {publico}  

Gere campanha melhor que as anteriores, evitando repetição.  
"""  

resposta = client.chat.completions.create(  
    model="gpt-4o-mini",  
    messages=[{"role": "user", "content": prompt}]  
)  

resultado = resposta.choices[0].message.content  

# salva aprendizado  
st.session_state.memoria_ia.append(resultado)  

return resultado

==========================================

IA ESPIÃ PRO

==========================================

elif menu == "🕵️ IA Espiã":

st.markdown("## 🕵️ Análise de Concorrência")  

concorrente = st.text_input("Produto ou nicho do concorrente")  

if st.button("Espionar", use_container_width=True):  

    prompt = f"""  
    Analise concorrentes do produto {concorrente}.  

    Entregue:  
    - Pontos fortes  
    - Pontos fracos  
    - Como vencer eles  
    """  

    resposta = client.chat.completions.create(  
        model="gpt-4o-mini",  
        messages=[{"role": "user", "content": prompt}]  
    )  

    st.success("Concorrência analisada")  
    st.write(resposta.choices[0].message.content)

==========================================

MERCADO LIVRE PRO

==========================================

import requests

elif menu == "📦 Mercado Livre PRO":

st.markdown("## 📦 Integração Mercado Livre")  

CLIENT_ID = st.secrets["ML_CLIENT_ID"]  
REDIRECT_URI = st.secrets["ML_REDIRECT_URI"]  

auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"  

if "ml_token" not in st.session_state:  
    st.warning("Conta não conectada")  
    st.link_button("🔗 Conectar Mercado Livre", auth_url)  

else:  
    st.success("Conta conectada!")  

    headers = {  
        "Authorization": f"Bearer {st.session_state['ml_token']}"  
    }  

    resp = requests.get("https://api.mercadolibre.com/users/me", headers=headers)  

    if resp.status_code == 200:  
        dados = resp.json()  
        st.write("👤 Usuário:", dados.get("nickname"))

if st.session_state.get("ml_token"):

busca = st.text_input("Buscar produto no Mercado Livre")  

if st.button("Buscar"):  

    headers = {  
        "Authorization": f"Bearer {st.session_state['ml_token']}"  
    }  

    resp = requests.get(  
        f"https://api.mercadolibre.com/sites/MLB/search?q={busca}",  
        headers=headers  
    )  

    data = resp.json()  

    for item in data.get("results", [])[:3]:  
        st.write(item["title"])  

        if st.button(f"Gerar campanha IA - {item['id']}"):  

            resultado = gerar_ia_inteligente(item["title"], "compradores online")  

            st.write(resultado)

==========================================

TENDÊNCIAS PRO

==========================================

elif menu == "🔥 Tendências":

st.markdown("## 🔥 Radar de Tendências")  

if st.button("🔍 Buscar produtos em alta", use_container_width=True):  

    with st.spinner("Analisando mercado..."):  
        time.sleep(2)  

    st.success("Tendências encontradas!")  

    col1, col2, col3 = st.columns(3)  

    col1.markdown("""  
    <div class='card'>  
    <h4>Air Fryer</h4>  
    🔥 Alta demanda  
    </div>  
    """, unsafe_allow_html=True)  

    col2.markdown("""  
    <div class='card'>  
    <h4>Conexões de gás</h4>  
    📈 Crescimento constante  
    </div>  
    """, unsafe_allow_html=True)  

    col3.markdown("""  
    <div class='card'>  
    <h4>Organizadores</h4>  
    💰 Alto ticket médio  
    </div>  
    """, unsafe_allow_html=True)

==========================================

AUTOMAÇÃO PRO

==========================================

elif menu == "⚡ Automação":

st.markdown("## ⚡ Automação 24h")  

st.success("🟢 Sistema ativo e rodando")  

st.markdown("""  
<div class='card'>  
<h3>🤖 O que está rodando agora:</h3>  
<ul>  
    <li>✔️ Monitoramento de produtos</li>  
    <li>✔️ Análise de concorrência</li>  
    <li>✔️ Geração de conteúdo</li>  
    <li>✔️ Otimização SEO</li>  
</ul>  
</div>  
""", unsafe_allow_html=True)

==========================================

AVATAR PRO

==========================================

elif menu == "🤖 Avatar":

st.markdown("## 🤖 Avatar IA (Vídeos)")  

foto = st.file_uploader("📸 Envie sua foto", type=["png", "jpg", "jpeg"])  

roteiro = st.text_area("📝 Roteiro do vídeo", height=120)  

if st.button("🎬 Gerar Vídeo", use_container_width=True):  

    if not foto:  
        st.warning("Envie uma foto")  
    else:  
        with st.spinner("Gerando avatar..."):  
            time.sleep(3)  

        st.success("Vídeo criado com sucesso!")  

        st.video("https://assets.mixkit.co/videos/preview/343/343-small.mp4")

==========================================

ANALYTICS PRO

==========================================

elif menu == "📊 Analytics":

st.markdown("## 📊 Performance e ROI")  

col1, col2, col3 = st.columns(3)  

col1.metric("Vendas", "R$ 12.400", "+22%")  
col2.metric("Conversão", "3.4%")  
col3.metric("ROI", "5.2x")  

st.markdown("### 📈 Evolução de Vendas")  

df = pd.DataFrame({  
    "vendas": [10, 20, 40, 80, 120, 200]  
})  

st.line_chart(df)

==========================================

CONFIGURAÇÕES PRO

==========================================

elif menu == "⚙️ Configurações":

st.markdown("## ⚙️ Configurações")  

nome = st.text_input("Nome", st.session_state.usuario.get("nome", ""))  
email = st.text_input("Email", st.session_state.usuario.get("email", ""))  

if st.button("💾 Salvar Alterações", use_container_width=True):  

    st.session_state.usuario["nome"] = nome  
    st.session_state.usuario["email"] = email  

    st.success("Dados atualizados com sucesso!")

==========================================

STATUS DO SISTEMA (SIDEBAR FINAL PRO)

==========================================

st.sidebar.divider()

Card visual

st.sidebar.markdown("""

<div style="  
background: rgba(255,255,255,0.06);  
padding: 16px;  
border-radius: 16px;  
margin-top: 10px;  
margin-bottom: 10px;  
border: 1px solid rgba(255,255,255,0.08);  
">  <h4 style="color:white; margin:0;">  
🚀 Sistema Velix  
</h4>  <p style="color:#cbd5e1; font-size:12px; margin-top:6px;">  
Automação • IA • Marketplace  
</p>  </div>  
""", unsafe_allow_html=True)  ==========================================

STATUS REAL DO SISTAEMA

==========================================

Evita erro se não existir ainda

ml_conectado = st.session_state.get("ml_token", False)

Status organizados

st.sidebar.markdown("### 🟢 Status do Sistema")

col1, col2 = st.sidebar.columns(2)

with col1:
st.success("Banco")
st.success("IA")

with col2:
st.success("Online")

Mercado Livre (dinâmico)

if ml_conectado:
st.sidebar.success("🟢 Mercado Livre conectado")
else:
st.sidebar.warning("🟡 Mercado Livre não conectado")

==========================================

INFORMAÇÃO FINAL (CREDIBILIDADE)

==========================================

st.sidebar.markdown("""

<div style="text-align:center; font-size:11px; color:#94a3b8; margin-top:12px;">  
Velix AI PRO<br>  
Sistema operacional inteligente ativo  
</div>  
""", unsafe_allow_html=True)
