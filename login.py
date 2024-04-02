import functools
import sqlalchemy.exc
from flask_sqlalchemy import SQLAlchemy
from flask import Blueprint, flash, g, redirect, render_template, request, session, url_for
from alchemyClasses.cliente import Cliente
loginClienteBlueprint = Blueprint('loginCliente', __name__, url_prefix='/loginCliente')

@loginClienteBlueprint.route('/', methods=['GET','POST'])
def loginCliente():

        # Recibe los datos
        if request.method == 'POST':

            nombre = request.form['nombre']
            correo = request.form['correo']
            contrasena = request.form['contraseña']

            #verifica que este en la base de datos de cliente
            cliente = Cliente.query.filter_by(nombre=nombre, correo=correo, contraseña=contrasena).first()


            if cliente != None:

                session.clear()
                session['cliente_id'] = cliente.id_cliente
                session['cliente_nombre'] = cliente.nombre
                return redirect(url_for("loginCliente.success"))
            else:
                return  render_template('loginCliente.html')
        else:  # Estamos haciendo un wget localhost:5000/login/
            return render_template('loginCliente.html')

@loginClienteBlueprint.route('/success', methods=['GET'])
def success():
    if session.get('cliente_id') != None:
        return render_template("success.html")
    flash("ERROR: Cookie de sesion vacia")
    return redirect(url_for('loginCliente.loginCliente'))

@loginClienteBlueprint.route("/failure", methods=["GET"])
def failure():
    return render_template("failure.html")

#-----------------------------  Este es la funcion de cliente

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cliente(db.Model):
    __tablename__ = 'cliente'

    #id_cliente = db.Column('id_cliente', db.String(200), primary_key=True, server_default=text('UUID()'))
    #id_cliente = db.Column('id_cliente', db.String(200), primary_key=True)
    id_cliente = db.Column('id_cliente', db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column('nombre', db.String(45))
    correo = db.Column('correo', db.String(45))
    telefono = db.Column('telefono', db.Integer)
    fna = db.Column('fna', db.Date)
    contraseña = db.Column('contraseña', db.String(45))



    def __init__(self, nombre, correo, telefono, fna, contraseña):
        #self.id_cliente = id_cliente
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.fna = fna
        self.contraseña = contraseña
