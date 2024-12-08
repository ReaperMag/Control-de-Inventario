from flask import Flask
from config import Config
from src.imports import db


def inicializar_materiales():
    materiales = ["Tubos", "Cartillas", "Tubos tapa Verde"]
    from src.Models.models import Materiales
    
    if not Materiales.query.first():
        for m in materiales:
            nuevo_material = Materiales(m,0)
            db.session.add(nuevo_material)
        db.session.commit()
        print("Materiales iniciales creados")
    else:
        print("No se insertaron materiales")

def crear_app():
    from src.routes.route import bp
    
    app = Flask(__name__)
    
    app.register_blueprint(bp)
    app.config.from_object(Config)
    
    db.init_app(app)
    
    with app.app_context():

        db.create_all()
        inicializar_materiales()
    
    return app