from flask import Flask

app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Paulo Godoy v1.0"