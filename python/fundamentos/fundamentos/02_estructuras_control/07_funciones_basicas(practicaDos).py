import os
"""
Practica funciones basicas practica dos
"""

# 1-. Calcula experiencia -------------------------------------------------------------------------------------
lista = []
def multiplica_por_2(num):
    for i in range(num + 1):
        lista.append( 2 * i )
    return lista

def ejercicio1():
    resultado = multiplica_por_2(5)
    print(resultado)

# 2-. Analiza publicaciones ------------------------------------------------------------------------------------------------------
def suma_y_resta(a):
    print(a[0] + a[1])
    return a[0] - a[1]

def ejercicio2():
    resultado = suma_y_resta([120, 115])
    print(resultado)
# Imprime: 235 y retorna: 5

# 3-. Puntaje ajustado -------------------------------------------------------------------------------------------------------------
def sumatoria_menos_longitud(b):
    suma_total = 0
    for i in range(len(b)):
        suma_total += b[i]
    print(f"Suma total = {suma_total}, longitud = {len(b)}")
    return suma_total - len(b)

def ejercicio3():
    resultado = sumatoria_menos_longitud([10, 5, 3, 7])
    print(resultado)

# 4-. Ajusta visualizaciones -----------------------------------------------------------------------------------------------

def valores_multiplicados_segundo(c):
    resultado = []
    print(len(c))
    for i in range(len(c)):
        if c[i] * (len(c)-1) != 0:
            resultado.append(c[i] * (len(c)-1))
    return resultado

def ejercicio4():
    resultado_uno = valores_multiplicados_segundo([100, 3, 50, 20])
    print(resultado_uno)
    resultado_dos = valores_multiplicados_segundo([100])
    print(resultado_dos)

# 5-. Genera precio fijo --------------------------------------------------------------------------------------------------------------
def valor_multiplicado_longitud(a, b):
    resultado = []
    for i in range(b):
        resultado.append(a * b)
    return resultado

def ejercicio5():
    resultado_uno = valor_multiplicado_longitud(5, 2)
    print(resultado_uno)
    resultado_dos = valor_multiplicado_longitud(7, 5)
    print(resultado_dos)

# extra -------------------------------------------------------------------------------------------------------------------------------------------
def limpiar_consola():
    os.system('cls')

continuar = True

while continuar:
    opcion = input("\n--- Elige una opción (1-15) (0 para salir) ---_")
    if opcion == "1":
        limpiar_consola()
        print("\n--- Ejecutando ejercicio uno ---")
        print(ejercicio1())
    elif opcion == "2":
        limpiar_consola()
        print("\n--- Ejecutando ejercicio dos ---")
        print(ejercicio2())
    elif opcion == "3":
        limpiar_consola()
        print("\n--- Ejecutando ejercicio tres ---")
        print(ejercicio3())
    elif opcion == "4":
        limpiar_consola()
        print("\n--- Ejecutando ejercicio cuatro ---")
        print(ejercicio4())
    elif opcion == "5":
        limpiar_consola()
        print("\n--- Ejecutando ejercicio cinco ---")
        print(ejercicio5())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("No válido...")