from flask import Flask, render_template, request

app = Flask(__name__)

plataformas = [
    {"nombre": "Spotify", "usuarios": "515M", "fundado": "2006", "pais": "EE.UU."},
    {"nombre": "Netflix", "usuarios": "247M", "fundado": "1997", "pais": "EE.UU."},
    {"nombre": "YouTube", "usuarios": "2.5B", "fundado": "2005", "pais": "EE.UU."},
    {"nombre": "Twitch", "usuarios": "140M", "fundado": "2011", "pais": "EE.UU."},
    {"nombre": "TikTok", "usuarios": "1.7B", "fundado": "2016", "pais": "China"},
    {"nombre": "Instagram", "usuarios": "2.35B", "fundado": "2010", "pais": "EE.UU."},
    {"nombre": "Discord", "usuarios": "250M", "fundado": "2015", "pais": "EE.UU."},
]

@app.route('/')
def inicio():
    # Valores por defecto
    return render_template('index.html', 
                           datos=plataformas, 
                           columna='nombre', 
                           direccion='asc',
                           pais_sel='todos',
                           texto="Mostrando todas las plataformas (7)")

@app.route('/enviar', methods=['POST'])
def procesar():
    # 1. Obtener valores del formulario
    pais = request.form.get('paises', 'todos')
    columna = request.form.get('tabla', 'nombre')
    direccion = request.form.get('orden', 'asc')

    # 2. Normalizar país
    if pais in ('todos', 'todos2'):
        pais_filtro = 'todos'   # para mostrarlo en el select
        filtrados = plataformas
    else:
        pais_filtro = pais
        filtrados = [p for p in plataformas if p['pais'] == pais]

    # 3. Ordenar
    invertir = (direccion == 'desc')
    # key=lambda x: x[columna]: sirve para ordenar o buscar en una lista según el contenido de una columna o clave específica.
    datos_ordenados = sorted(filtrados, key=lambda x: x[columna], reverse=invertir)

    # 4. Mensaje
    total = len(datos_ordenados)
    
    if pais_filtro == 'todos':
        nombre_pais = 'Todos'
    else:
        nombre_pais = pais

    if columna == 'fundado':
        columna_nombre = 'Año Fundación'
    else:
        columna_nombre = columna.capitalize()  #m étodo que convierte el primer carácter de un texto en mayúscula y todos los demás en minúsculas

    if direccion == 'asc':
        direccion_texto = 'Ascendente'
    else:
        direccion_texto = 'Descendente'

    # Mensaje final
    texto = f"Mostrando {total} plataformas de {nombre_pais} ordenadas por {columna_nombre} ({direccion_texto})"

    # 5. Renderizar pasando todos los valores para mantener la selección
    return render_template('index.html', 
                           datos=datos_ordenados, 
                           columna=columna,     
                           direccion=direccion,   
                           pais_sel=pais_filtro,
                           texto=texto)

if __name__ == '__main__':
    app.run(debug=True)