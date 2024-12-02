from flask import Flask
from config import Config

def crear_app():
    from src.routes.route import bp
    
    app = Flask(__name__)
    
    app.register_blueprint(bp)
    app.config.from_object(Config)
    
    return app