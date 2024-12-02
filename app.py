from flask_sqlalchemy import SQLAlchemy
import os

from src import crear_app
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

app = crear_app()
# app.config.from_object(Config)
# print(app.config)

db.init_app(app)

with app.app_context():

    db.create_all()
    inicializar_materiales()

if __name__ == "__main__":
    
    port = int(os.environ.get("PORT",5000))
    
    app.run(debug=True, port=port)