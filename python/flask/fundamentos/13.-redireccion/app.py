from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


# ==========================================
# RUTA PRINCIPAL
# ==========================================

@app.route("/")
def index():
    return render_template("index.html")


# ==========================================
# PROCESAR FORMULARIO
# ==========================================

@app.route("/registrar", methods=["POST"])
def registrar():

    # Obtener datos del formulario
    nombre = request.form["nombre"]
    precio = request.form["precio"]
    categoria = request.form["categoria"]

    # Mostrar información en la terminal
    print("===================================")
    print("Producto recibido")
    print(f"Nombre: {nombre}")
    print(f"Precio: {precio}")
    print(f"Categoría: {categoria}")
    print("===================================")

    # Redireccionar después del POST
    return redirect(url_for("resultado"))


# ==========================================
# MOSTRAR RESULTADO
# ==========================================

@app.route("/resultado")
def resultado():

    print("Usuario redirigido mediante GET")

    # request.form estará vacío
    print("request.form:", request.form)

    return render_template("resultado.html")


# ==========================================
# RUTA DE AYUDA
# ==========================================

@app.route("/ayuda")
def ayuda():
    return render_template("ayuda.html")


# ==========================================
# EJECUTAR SERVIDOR
# ==========================================

if __name__ == "__main__":
    app.run(debug=True)