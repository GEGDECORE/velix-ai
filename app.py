from flask import Flask, request, jsonify
import os

app = Flask(__name__)

@app.route("/")
def home():
    return "VELIX AI rodando 🚀"

@app.route("/gerar", methods=["POST"])
def gerar():
    data = request.json

    produto = data.get("produto", "")
    descricao = data.get("descricao", "")

    anuncio = f"""
🔥 SUPER OFERTA 🔥

📦 Produto: {produto}

📝 Descrição otimizada:
{descricao}

🚀 Compre agora e aproveite!
Entrega rápida + qualidade garantida!

💥 Estoque limitado!
"""

    return jsonify({"anuncio": anuncio})

if _name_ == "_main_":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
