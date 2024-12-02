from src.imports import db


class Entrega(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True, autoincrement = True)
    material = db.Column(db.String(50), nullable = False)
    codigo = db.Column(db.Integer, nullable = False)
    cantidad = db.Column(db.Integer, nullable = False)
    fecha = db .Column(db.String(30), nullable = True)

class Materiales(db.Model):
    id = db.Column(db.Integer, primary_key = True, unique = True, autoincrement = True)
    nombre = db.Column(db.String(50))
    stock = db.Column(db.Integer)
    
    def __init__(self, nombre:str, stock:int):
        self.nombre = nombre
        self.stock = stock
    
    # def agregarMaterial(self, nombre:str, stock:int):
    #     nuevo_material = Materiales(nombre=nombre, stock=stock)
    #     db.session.add(nuevo_material)
    #     db.session.commit()
    #     return nuevo_material