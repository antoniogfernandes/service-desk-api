from flask import Flask
from database import inicializar_banco
from routes.chamados_routes import chamados_bp
from routes.usuarios_routes import usuarios_bp
from routes.atendimentos_routes import atendimentos_bp

app = Flask(__name__)

app.register_blueprint(chamados_bp)
app.register_blueprint(usuarios_bp)
app.register_blueprint(atendimentos_bp)

inicializar_banco()

@app.route("/")
def home():
    return {"status": "Service Desk API rodando 🚀"}

if __name__ == "__main__":
    app.run(debug=True)