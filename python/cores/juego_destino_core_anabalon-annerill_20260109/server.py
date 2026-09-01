from flask import Flask, render_template, request, session, redirect, url_for
import random
app = Flask(__name__)

# Clave para manejar sesiones en Flask
app.secret_key = "clave_secreta"

# Ruta principal que muestra el formulario para ingresar datos
@app.route("/")
def index():
    return render_template("index.html")

# Ruta para procesar los datos del formulario y almacenarlos en sesión
@app.route("/enviar", methods=["POST"])
def enviar_usuario():
    # Obtener datos del formulario
    nombre = request.form["nombre"]
    edad = request.form["fechaNacimiento"]
    color = request.form["colorFavorito"]
    animal = request.form["animal"]
    
    # Guardar información en la sesión
    session["nombre_usuario"] = nombre
    session["fecha_usuario"] = edad
    session["color_usuario"] = color
    session["animal_usuario"] = animal
    
    # --------------------------------------
    # Redireccionar
    # --------------------------------------
    return redirect(url_for("futuro"))

# Ruta para mostrar la predicción del futuro basada en los datos ingresados
@app.route("/futuroUsuario")
def futuro():
    # Verificar que existan los datos en sesión
    if "nombre" not in session:
        return redirect(url_for("index"))
    
    # Mensajes positivos y negativos
    mensajes_positivos = [
        "Tendrás un futuro brillante lleno de éxitos.",
        "La suerte estará de tu lado en todos tus proyectos.",
        "Grandes oportunidades te esperan en el amor y el trabajo.",
        "Tu creatividad te llevará a lugares increíbles.",
        "Superarás todos los obstáculos con valentía."
    ]
    
    mensajes_negativos = [
        "Cuidado con las decisiones impulsivas, podrían traerte problemas.",
        "Se avecinan días difíciles, pero todo pasará.",
        "Alguien cercano podría traicionarte, mantén los ojos abiertos.",
        "No todo lo que brilla es oro, analiza bien las ofertas.",
        "Evita los viajes largos en los próximos meses."
    ]

    # Elegir aleatoriamente entre positivo o negativo
    # random.choice elige de forma equitativa entre todas las posibilidades
    if random.choice([True, False]):
        destino = random.choice(mensajes_positivos)
    else:
        destino = random.choice(mensajes_negativos)

    # Renderizar la plantilla con los datos
    return render_template("futuro.html",
                            nombre = session["nombre"],
                            edad = session["edad"],
                            color = session["color"],
                            animal = session["animal"],
                            destino = destino)

if __name__ == "__main__":
    app.run(debug=True)