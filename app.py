from flask import Flask, jsonify
import os

app = Flask(__name__)

usuarios = [
    {"id": 1, "nome": "Pedro Lacerda"},
    {"id": 2, "nome": "Ana Lucia"},
    {"id": 3, "nome": "Maria Fernanda"},
]

@app.route("/usuarios", methods=["GET"])
def home():
    return jsonify({"mensagem": "API de usuarios - acesse /usuarios"})

@app.route("/", methods=["GET"])
def listar_usuarios():
    return jsonify(usuarios)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5001))
    app.run(host="0.0.0.0", port=port)
