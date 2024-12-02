from flask import Blueprint, render_template, jsonify, redirect, request, session


bp = Blueprint("/", __name__, template_folder="templates")


from src.Models.models import Materiales, Entrega
from src.imports import db

@bp.route("/")
def home():
    
    codes = [100,123,7475]
    materiales = ["Tubos", "Cartillas", "Tubos tapa Verde"]
    
    s = Materiales.query.all()
    
    
    stock = [{"material" : l.nombre,
              "stock" : l.stock
              } for l in s] 
    
    return render_template("index.html", codigos=codes, materiales = materiales, base = stock)

@bp.route("/listado")
def test():
    
    m = Entrega.query.all()
    s = Materiales.query.all()
    
    entregas = [{"id" : n.id,
                 "material" : n.material, 
                 "cantidad" : n.cantidad,
                 "codigo" : n.codigo,
                 "fecha" : n.fecha
                 } for n in m]
    
    stock = [{"material" : l.nombre,
              "stock" : l.stock
              } for l in s] 
    
    return render_template("listado.html", items = entregas, base = stock)

@bp.route("/add_item", methods=["POST"])
def add_item():
    import time
    
    i_codigo = request.form["codigo"]
    i_cantidad = int(request.form["cantidad"])
    i_material = request.form["material"]
    
    #Sacar hora actual y formatear mensaje
    hora = time.asctime()
    
    print("Nueva entrega: ", i_codigo," ", i_material, " ", i_cantidad*-1, " ", hora)
    
    #Reducir Stock
    stock = Materiales.query.filter_by(nombre = i_material).first()
    if stock:
        stock.stock = int(stock.stock) - int(i_cantidad)
        db.session.commit()
    
    new_join = Entrega(
        material = i_material,
        codigo = i_codigo,
        cantidad = i_cantidad * -1,
        fecha = hora
    )
    db.session.add(new_join)
    db.session.commit()
    
    return redirect("/")

@bp.route("/add_stock", methods=["POST"])
def add_stock():
    
    material = request.form["material"]
    stock = request. form["cantidad"]
    
    objeto = Materiales.query.filter_by(nombre=material).first()
    stock = int(objeto.stock) + int(stock)
    if objeto:
        objeto.stock = stock
        db.session.commit()
    
    print(objeto.nombre, " ", objeto.stock)
    
    return redirect("/")

@bp.route("/delete_item", methods=["POST"])
def delete_item():
    ide = request.form["item_id"]
    
    print("Se elimino id: ", ide)
    return redirect("/listado")

@bp.route("/sql_get")
def get_sql():
    m = Entrega.query.all()
    print(m)
    
    Entregas = [{"id" : n.id,
                 "material" : n.material, 
                 "cantidad" : n.cantidad,
                 "codigo" : n.codigo,
                 "fecha" : n.fecha
                 } for n in m]
    
    
    return jsonify(Entregas)