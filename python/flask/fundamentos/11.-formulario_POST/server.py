from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    # Obtener datos del formulario
    nombre = request.form.get("nombre")
    email = request.form.get("email")
    age = request.form.get("age")
    ciudad = request.form.get("ciudad")

    # Redirigir a una ruta GET que muestre el resultado
    # Pasamos los datos como parámetros en la URL (o podrías usar sesión)
    return redirect(url_for('mostrar_usuario', nombre=nombre, email=email, age=age, ciudad=ciudad))

@app.route('/usuario')
def mostrar_usuario():
    # Recibir los datos desde la URL
    nombre = request.args.get("nombre")
    email = request.args.get("email")
    age = request.args.get("age")
    ciudad = request.args.get("ciudad")
    return render_template("user.html", nombre=nombre, email=email, age=age, ciudad=ciudad)

if __name__ == "__main__":
    app.run(debug=True)