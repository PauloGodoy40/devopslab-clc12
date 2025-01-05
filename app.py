from flask import Flask
from flask_wtf.csrf imnport CSRFProtect 
app = Flask(__name__)

@app.route("/")
def pagina_inicial():
    return "Paulo Godoy"
