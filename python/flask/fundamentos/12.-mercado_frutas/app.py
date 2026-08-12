from flask import Flask, render_template, request

app = Flask(__name__)

frutas = [
    {
        "nombre": "Manzana",
        "precio": 2.5,
        "imagen": "manzana.jfif",
        "descripcion": "Fruta dulce y crujiente, rica en fibra y vitamina C."
    },
    {
        "nombre": "Plátano",
        "precio": 1.8,
        "imagen": "platano.jpeg",
        "descripcion": "Fruta energética rica en potasio, perfecta para deportistas."
    },
    {
        "nombre": "Naranja",
        "precio": 3.0,
        "imagen": "naranja.jpg",
        "descripcion": "Cítrico jugoso con alto contenido de vitamina C y antioxidantes."
    },
    {
        "nombre": "Fresa",
        "precio": 4.5,
        "imagen": "frutilla.webp",
        "descripcion": "Baya dulce y aromática, rica en antioxidantes y vitamina C."
    },
    {
        "nombre": "Uva",
        "precio": 3.8,
        "imagen": "uva.webp",
        "descripcion": "Fruta pequeña y dulce, ideal para snacks y postres."
    },
    {
        "nombre": "Piña",
        "precio": 5.0,
        "imagen": "pina.jpg",
        "descripcion": "Fruta tropical dulce y ácida, con propiedades antiinflamatorias."
    },
    {
        "nombre": "Sandía",
        "precio": 4.2,
        "imagen": "sandia.jpg",
        "descripcion": "Fruta refrescante, compuesta en un 90% de agua, ideal para el verano."
    },
    {
        "nombre": "Mango",
        "precio": 3.5,
        "imagen": "mango.webp",
        "descripcion": "Fruta tropical dulce y aromática, rica en vitaminas A y C."
    }
]

@app.route("/")
def index():
    return render_template("index.html", frutas=frutas)

@app.route("/frutas")
def catalogo():
    return render_template("frutas.html", frutas=frutas)

@app.route("/checkout", methods=["POST"])
def checkout():
    nombre = request.form.get("nombre", "Cliente")
    email = request.form.get("email", "sin@email.com")
    direccion = request.form.get("direccion", "Sin dirección")

    pedido = []
    total = 0
    total_frutas = 0

    for fruta in frutas:
        # Usamos el nombre de la fruta como clave (coincide con el atributo name del input)
        cantidad_str = request.form.get(fruta["nombre"], "0")
        try:
            cantidad = int(cantidad_str)
        except ValueError:
            cantidad = 0

        if cantidad > 0:
            subtotal = cantidad * fruta["precio"]
            pedido.append({
                "nombre": fruta["nombre"],
                "precio": fruta["precio"],
                "cantidad": cantidad,
                "subtotal": subtotal,
                "imagen": fruta["imagen"]
            })
            total += subtotal
            total_frutas += cantidad

    return render_template(
        "checkout.html",
        nombre=nombre,
        email=email,
        direccion=direccion,
        pedido=pedido,
        total=total,
        total_frutas=total_frutas
    )

if __name__ == "__main__":
    app.run(debug=True)