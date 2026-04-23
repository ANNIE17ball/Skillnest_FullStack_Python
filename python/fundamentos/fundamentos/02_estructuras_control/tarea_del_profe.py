
# MINI DESAFÍO (nivel core)
# 1. Cambiar el puntaje de Pedro a 75
# 2. Crear función que imprima:
#    "Carlos obtuvo 80 puntos"
# 3. Crear función que reciba "nombre" o "puntaje" e imprima solo esos valores

datos = [
    {"nombre": "Carlos", "puntaje": 80},
    {"nombre": "María", "puntaje": 95},
    {"nombre": "Pedro", "puntaje": 70}
]
# 1)
datos[2]["puntaje"] = 75

# 2)
def imprimir(dicci):
    where = int(input(f"Ingresa un indice(0/{len(dicci) - 1}):_"))
    print(f"{dicci[where]["nombre"]} obtuvo {dicci[where]["puntaje"]} puntos")

# 3)
def valor_de_datos(val):
    if val in datos[0]:
        for i in range(len(datos)):
            print(datos[i][val])