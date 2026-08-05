from flask import Flask, render_template, request
app = Flask(__name__)

# Base de datos ficticia de plataformas digitales
datos = [
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "Suecia"},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU."},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU."},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU."},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU."},
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU."},
]

@app.route('/enviar', methods=['POST'])
def procesar_formulario():
    # Leemos los 3 selectores usando su atributo name=""
    pais_sel = request.form.get('paises')
    criterio_orden = request.form.get('tabla')
    direccion_orden = request.form.get('orden')
    
    # for + append" en una línea
    if pais_sel == "all":
        items_filtrados = datos["items"]
    else:
        items_filtrados = [i for i in datos["items"] if i.get("pais") == pais_sel]
        
    # 'reverse=True' si el usuario eligió "desc" (Descendente)
    es_descendente = (direccion_orden == "desc")
    
    # Ordenamos usando el criterio que viene del segundo select
    items_procesados = sorted(
        items_filtrados, 
        key=lambda x: x.get(criterio_orden), 
        reverse=es_descendente
    )
    
    # 4. RESPUESTA: Contamos los elementos automáticamente con len()
    total = len(items_procesados)
    texto_resultado = f"Mostrando {total} plataformas de {pais_sel.upper()} ordenadas por {criterio_orden} ({direccion_orden})"
    
    return render_template(
        'index.html', 
        items=items_procesados, 
        texto=texto_resultado
    )

# Ruta para mostrar la tabla con datos
@app.route('/')
def lista():
    return render_template('index.html', datos=sorted(datos), texto="Mostrando 7 plataformas")

# Ruta para mostrar la tabla con datos en orden descendente?
@app.route('/')
def lista():
    return render_template('index.html', datos=sorted(datos, reverse=True), texto="Mostrando 7 plataformas")

# Ruta para mostrar la tabla con datos limitados
@app.route('/cantidad/<int:cantidad>')
def lista(cantidad):
    return render_template('index.html', datos=sorted(datos[:cantidad]), texto=f"Mostrando solo {cantidad} plataformas")

# Ruta para mostrar la tabla con datos limitados
@app.route('/cantidad/<int:cantidad>')
def lista(cantidad):
    return render_template('index.html', datos=datos[:cantidad], texto=f"Mostrando solo {cantidad} plataformas")

if __name__ == "__main__":
    app.run(debug=True)