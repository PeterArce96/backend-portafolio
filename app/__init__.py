# todo paquete de python dentro de una carpeta siempre va reconocer como su archivo principal al archivo __init__.py
from flask import Flask
from flask_bootstrap import Bootstrap4
from app.FirebaseAdmin import FirebaseAdmin

fb = FirebaseAdmin()

# Blueprints
from .portafolio import portafolio
from .admin import admin

# archivo de configuración
from .config import Config

def create_app():
    app = Flask(__name__)

    bootstrap = Bootstrap4(app)

    app.config.from_object(Config)

    app.register_blueprint(portafolio)
    app.register_blueprint(admin)

    return app