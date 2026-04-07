""" 
Diccionarios:
estructura de datos que nos permite almacenar contenido a través de una llave (o clave) y un valor
"""

estudiante = {"nombre": "Gonzalo", "curso": "Python"} #Notación Literal
print(estudiante["nombre"]) #Imprime el nombre del estudiante

estudiante["nombre"] = "Vicente"
print(estudiante["nombre"]) #Imprime: Vicente

estudiante["nombre"] = input("Ingresa un nombre ").lower()
print(estudiante["nombre"]) #Imprime input

paises = {} #Diccionario vacío
paises["MEX"] = "México" #Agregando valores
paises["COL"] = "Colombia"
paises["CHL"] = "Chile"
paises["PER"] = "Perú"
paises["CAM"] = "Camboya"

# Condición pra buscar elemento e insertar si no existe
if "CRI" in paises: #Preguntamos si existe la clave en el diccionario
    print("¿Deseas reemplazar el valor?")
else: #No existe esa clave
    paises["CRI"] = "Costa Rica"
print(paises)

valor_removido = paises.pop("MEX") #Elimina el elemento y devuelve su valor
print("El elemento eliminado fue:",valor_removido)
del paises["COL"] #Elimina el elemento
print(paises) #Imprime: {'CHL': 'Chile'}

# Diccionario multi-línea
pintor = { 
    "nombre": "Frida Kahlo",
    "pais": "México",
    "fecha_nacimiento": "6 de julio de 1907"
    }

# Diccionarios anidados
escuela = {
    "nombre": "Coding Dojo LATAM",
    # Otro diccionario
    "profesores": [
        {"nombre": "Alfredo", "apellido": "Salazar", "cursos": ["Python", "Java"]},
        {"nombre": "Valeria", "apellido": "Romero", "cursos": ["Fundamentos", "Java"]},
        {"nombre": "Marcelo", "apellido": "Argotti", "cursos":["MERN", "Python"]}
    ]
}