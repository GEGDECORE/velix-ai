import streamlit as st

# ID REAL DA DANIELE
CLIENT_ID = "8642953419393317" 
REDIRECT_URI = "https://velix-ai.streamlit.app/" 

st.set_page_config(page_title="VELIX AI | Business Intelligence", layout="wide")

# DESIGN NEON PROFISSIONAL
st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: #FFFFFF !important; }
    section[data-testid="stSidebar"] { background-color: #161B22 !important; border-right: 2px solid #00FFFF; }
    [data-testid="stSidebar"] [data-testid="stWidgetLabel"] p, 
    [data-testid="stSidebar"] label p,
    [data-testid="stSidebar"] span { color: #FFFFFF !important; font-size: 1.1rem !important; font-weight: 800 !important; }
    h1, h2, h3 { color: #00FFFF !important; text-shadow: 0 0 8px #00FFFF; }
    .stButton>button { background-image: linear-gradient(to right, #00FFFF, #FF00FF); color: white !important; border: none; font-weight: bold; border-radius: 10px; width: 100%; }
    </style>
    """, unsafe_allow_html=True)

st.sidebar.markdown("<h1 style='text-align: center;'>VELIX AI</h1>", unsafe_allow_html=True)
st.sidebar.write("---")

menu = st.sidebar.radio("Navegação", ["📊 Dashboard", "💬 Velix Chat GPT", "⚙️ Integrações"])

if menu == "⚙️ Integrações":
    st.title("🔗 Integração Mercado Livre")
    auth_url = f"https://auth.mercadolivre.com.br/authorization?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    st.markdown(f'<a href="{auth_url}" target="_blank"><button style="width: 100%; background-image: linear-gradient(to right, #00FFFF, #FF00FF); color: white; padding: 15px; border: none; border-radius: 10px; font-weight: bold; cursor: pointer;">CONECTAR CONTA</button></a>', unsafe_allow_html=True)

elif menu == "💬 Velix Chat GPT":
    st.title("🧠 Inteligência Velix")
    st.info("Pronta para uso com seus créditos OpenAI.")

else:
    st.title("📊 Dashboard")
    st.metric("Performance", "R$ 42.850", "+15%")
