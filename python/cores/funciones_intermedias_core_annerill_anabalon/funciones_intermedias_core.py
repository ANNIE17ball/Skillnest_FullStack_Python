import os
# extra -------------------------------------------------------------------------------------------------------------------------------------------
def limpiar_consola():
    os.system('cls')

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

"""
Evaluacion core
"""
# 1) 
# En puntajes, cambia el valor 300 por 600 (ajuste en los puntajes de la primera ronda).
# En streamers, cambia el nombre de ”GameNinjaPro” a ”EliteGamerX”.
# En eventos, cambia la ciudad “Las Vegas” por “San Francisco”.
# En ubicacion, cambia el valo de ”latitud” a 40.712776 (cambiando la sede del torneo a Nueva York).

# Ranking de puntajes de un torneo de eSports -----------------------------------------------------------------------------------------------------------------------------------
puntajes = [ [1000, 1500, 2000], [300, 700, 1400] ]
puntajes[1][0] = 600

# Lista de creadores de contenido en una plataforma de streaming ----------------------------------------------------------------------------------------------------------------------
streamers = [
    {"nombre": "GameNinjaPro", "seguidores": 250000},
    {"nombre": "PixelWarrior", "seguidores": 180000}
]
streamers[0]["nombre"] = "EliteGamerX"

# Eventos en distintas ciudades del mundo --------------------------------------------------------------------------------------------------------------------------------------------
eventos = {
    "Estados Unidos": ["Los Ángeles", "Nueva York", "Las Vegas"],
    "España": ["Madrid", "Barcelona", "Valencia"]
}
eventos["Estados Unidos"][2] = "San Francisco"

# Coordenadas de la sede de un torneo internacional ---------------------------------------------------------------------------------------------------------------------------------------------
ubicacion = [
    {"latitud": 34.052235, "longitud": -118.243683}
]
ubicacion[0]["latitud"] = 40.712776

# 2) Creacion de funciones ⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘⫘

""" Funcion uno """
def iterar_diccionario(lista):
    inte = input("Ingresa un numero (0/1):_")
    
    if inte == "0":
        print(f"nombre - {lista[0]["nombre"]}, seguidores - {lista[0]["seguidores"]}")
    elif inte == "1":
        print(f"nombre - {lista[1]["nombre"]}, seguidores - {lista[1]["seguidores"]}")
    else:
        print("Por favor ingresar valor valido")

""" Funcion dos """
def obtener_valores(clave, lista):
    for i in range(len(lista)):
        actual = lista[i]
        if actual in lista:
            print(lista[i][clave])
        else:
            pass

""" Funcion tres """
# diccionario especial
categorias = {
    "juegos_populares": [
        "Fortnite", 
        "Minecraft", 
        "Valorant", 
        "GTA V",
    ],
    "ciudades_eventos": [
        "Nueva York",
        "Madrid",
        "Tokio",
    ]
}

def mostrar_informacion(diccionario):
    for categoria, lista in diccionario.items():
        print(f"{len(lista)} {categoria.upper()}")
        for item in lista:
            print(item)

# ⫶☰ MENU
print("Bienvenido a python!")
print("Este es un menu, por favor seleccionar del uno al cinco para revisar las funciones, ")
print("seis para ver los diccionarios y 0 para salir")

seguir = True
while seguir:
    seleccion = input("Seleccionar nivel >> ")
    if seleccion == "1":
        limpiar_consola()
        print("Navegando al nivel uno...⏅")
        print(iterar_diccionario(streamers))
    elif seleccion == "2":
        limpiar_consola()
        print("Navegando al nivel dos...⛴")
        obtener_valores("nombre", streamers)
        obtener_valores("seguidores", streamers)
    elif seleccion == "3":
        limpiar_consola()
        print("Navegando al nivel tres...☸")
        mostrar_informacion(categorias)
    elif seleccion == "4":
        limpiar_consola()
        print("Navegando al nivel cuatro...°‧ 𓆝 𓆟 𓆞 ·｡")
        print(imprimir(datos))
    elif seleccion == "5":
        limpiar_consola()
        print("Navegando al nivel cinco...𓆝𓆟༝˚｡⋆𓆉︎⋆｡˚༝𓆞𓆝")
        print(valor_de_datos("puntaje"))
        print(valor_de_datos("nombre"))
    elif seleccion == "6":
        limpiar_consola()
        print("Mostrando diccionarios...𓂃 ོ☼𓂃")
        print("Diccionario de puntajes")
        print(puntajes)
        print("Diccionario de streamers")
        print(streamers)
        print("Diccionario de eventos")
        print(eventos)
        print("Diccionario de ubicaciones")
        print(ubicacion)
        print("Diccionario de categorias")
        print(categorias)
        print("Diccionario de datos")
        print(datos)
    elif seleccion == "0":
        limpiar_consola()
        print("Saliendo...")
        seguir = False
    else:
        print("No válido...")