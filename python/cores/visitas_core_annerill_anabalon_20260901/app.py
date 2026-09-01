from flask import Flask, render_template, request, redirect, url_for, session

app = Flask(__name__)
app.secret_key = "una-clave-secreta"

@app.route("/")
def index():
    # Inicializar variables de sesión si no existen
    if 'visitas' not in session:
        session['visitas'] = 0
    if 'reinicios' not in session:
        session['reinicios'] = 0
        
    session['visitas'] += 1
    
    return render_template("index.html",
                            visitas=session['visitas'],
                            reinicios=session['reinicios'])

@app.route("/destruir_sesion")
def destroy():
    session.clear()
    return redirect(url_for('index'))

@app.route("/incrementar-dos")
def incrementar2():
    if 'visitas' in session:
        session['visitas'] += 2 -1
    else:
        session['visitas'] = 2 -1
    return redirect(url_for('index'))

@app.route("/reiniciar")
def reiniciar():
    if 'visitas' in session:
        session['visitas'] = -1
        # Incrementar contador de reinicios
        if 'reinicios' in session:
            session['reinicios'] += 1
        else:
            session['reinicios'] = 1
    return redirect(url_for('index'))

@app.route("/aumentar/<int:num>")
def aumentar(num):
    if 'visitas' in session:
        session['visitas'] += num -1
    else:
        session['visitas'] = num -1
    return redirect(url_for('index'))

# NUEVA RUTA: procesa el formulario y redirige a /aumentar/num
@app.route("/procesar_aumento", methods=['POST'])
def procesar_aumento():
    num = request.form.get('num', type=int)
    if num is None:
        num = 0
    return redirect(url_for('aumentar', num=num))

if __name__ == "__main__":
    app.run(debug=True)