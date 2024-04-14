from flask import Flask, render_template, request
import mysql.connector

database = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="pos"
)

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    return render_template("menu.html")

@app.route("/productos")
def productos():
    # Abrir un cursor para ejecutar consultas
    cursor = database.cursor()

    # Obtener datos de la tabla productos
    cursor.execute('SELECT * FROM productos')
    productos = cursor.fetchall()

    # Cerrar el cursor
    cursor.close()

    return render_template('catalogoProductos.html', productos=productos)

@app.route("/clientes")
def clientes():
    # Abrir un cursor para ejecutar consultas
    cursor = database.cursor()

    # Obtener datos de la tabla clientes
    cursor.execute('SELECT * FROM clientes')
    clientes = cursor.fetchall()

    # Cerrar el cursor
    cursor.close()

    return render_template('catalogoClientes.html', Clientes=clientes)

@app.route("/usuarios")
def usuarios():
    # Abrir un cursor para ejecutar consultas
    cursor = database.cursor()

    # Obtener datos de la tabla usuarios
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()

    # Cerrar el cursor
    cursor.close()

    return render_template('catalogoUsuarios.html', usuarios=usuarios)

if __name__ == '__main__':
    app.run()
