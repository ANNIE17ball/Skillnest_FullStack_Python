from flask import Flask, render_template, request, redirect #Agregamos request y redirect
app = Flask(__name__)

# La ruta raíz renderizará nuestro formulario
@app.route('/')
def index():
    return render_template("index.html")

# /crear_usuario recibe la información

@app.route('/crear_usuario', methods=['POST'])
def crear_usuario():
    print("Recibiendo información")
    print("Nombre:", request.form["nombre"])
    print("Correo:", request.form["email"])
    print("Edad:", request.form["age"])
    print("Ciudad:", request.form["ciudad"])

    #JAMAS renderizamos una plantilla ante una solicitud POST
    return render_template(

        "usuario.html",

        nombre=nombre,

        email=email

    ) #En su lugar, redirigimos a otra ruta

# volver
@app.route('/volver', methods=['POST'])
def regresar():
    print("Recibiendo información")
    print(request.form)

    #JAMAS renderizamos una plantilla ante una solicitud POST
    return redirect('/') #En su lugar, redirigimos a otra ruta

if __name__ == "__main__":
    app.run(debug=True)