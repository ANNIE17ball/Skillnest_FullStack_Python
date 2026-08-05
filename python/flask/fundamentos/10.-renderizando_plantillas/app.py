from flask import Flask, render_template
import  random
app = Flask(__name__)

@app.route('/listas')
def renderizar_listas():
    #Próximamente estas listas serán extraidas de la base de datos
    listado_estudiantes = [
        {'nombre': 'Florencia', 'edad': 25},
        {'nombre': 'Valentina', 'edad': 30},
        {'nombre': 'José', 'edad': 27},
        {'nombre': 'Patricio', 'edad': 21}
    ]
    
    num1 = random.randint(-10, 10) #Genera un número aleatorio entre -10 y 10
    num2 = random.randint(-10, 10)
    num3 = random.randint(-10, 10)
    return render_template('index.html', numeros=[num1, num2, num3], estudiantes=listado_estudiantes)

if __name__ == "__main__":
    app.run(debug=True)