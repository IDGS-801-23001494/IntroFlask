from flask import Flask, render_template, request
from flask import flash
from flask_wtf.csrf import CSRFProtect

import forms
import math

app = Flask(__name__)
app.secret_key = "clave secreta"

csrf = CSRFProtect()


@app.route("/")  # Llamado ruta o decorador, cada decorador tiene asociado una funcion
def index():
    titulo = "Flask IDGS801"
    lista = ["Juan", "Mario", "Pedro", "Dario"]
    return render_template("index.html", titulo=titulo, lista=lista)


@app.route("/operasBas", methods=["GET", "POST"])
def operas1():
    n1 = 0
    n2 = 0
    res = 0
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        res = float(n1) + float(n2)
    return render_template("operasBas.html", n1=n1, n2=n2, res=res)


@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    tem = float(n1) + float(n2)
    return f"La suma es: {tem}"


@app.route("/alumnos")
def alumnos():
    return render_template("alumnos.html")


@app.route("/usuarios", methods=["GET", "POST"])
def usuarios():
    mat = 0
    nom = ""
    apa = ""
    ama = ""
    email = ""
    usuarios_class = forms.UserForm(request.form)
    if request.method == "POST" and usuarios_class.validate():
        mat = usuarios_class.matricula.data
        nom = usuarios_class.nombre.data
        apa = usuarios_class.apaterno.data
        ama = usuarios_class.amaterno.data
        email = usuarios_class.correo.data
        mensaje = "Bienvenido {}".format(nom)
        flash(mensaje)

    return render_template(
        "usuarios.html",
        form=usuarios_class,
        mat=mat,
        nom=nom,
        apa=apa,
        ama=ama,
        email=email,
    )


@app.route("/numero/<int:n>")
def numero(n):
    return f"<h1>El numero es: {n}</h1>"


@app.route("/user/<int:id>/<string:username>")
def username(id, username):
    return f"<h1>Hola, {username}. Tu ID es: {id}</h1>"


@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1, n2):
    return f"<h1>La suma es: {n1 + n2}</h1>"


@app.route("/default")
@app.route(
    "/default/<string:param>"
)  # Mas de un decorador, se puede mandar a llamar de las dos maneras pero la idea es que muestre algo distinto
def func(param="Juan"):
    return f"<h1>Hola, {param}!</h1>"


@app.route("/operas")
def operas():
    return """
            <form>
                <label form="name">Name: </label>
                <input type="text" id="name" name="name" required>
                </br>
                <label for="name"> apaterno: </label>
                <input type="text" id="name" name="name" required>
            </form>

          """


# Ruta para distancia
@app.route("/distancia", methods=["GET", "POST"])
def distancia():
    x1 = 0
    x2 = 0
    y1 = 0
    y2 = 0
    r = 0

    if request.method == "POST":
        x1 = float(request.form.get("x1"))
        x2 = float(request.form.get("x2"))
        y1 = float(request.form.get("y1"))
        y2 = float(request.form.get("y2"))

        r = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template("distancia.html", r=r)


if __name__ == "__main__":
    csrf.init_app(app)
    app.run(debug=True)
