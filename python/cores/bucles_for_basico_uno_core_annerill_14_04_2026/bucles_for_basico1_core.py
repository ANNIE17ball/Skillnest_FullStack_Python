"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
def ejercicio1():
    for i in range(101):
        print(i)

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
def ejercicio2():
    for i in range(2, 501, 2):
        print(i)

# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime "🃖 - 🃁"
# - Si es divisible por 10, imprime "🂺"
# ¡Cuidado con la prioridad en tus condicionales!
def ejercicio3():
    for i in range(1, 101):
        if i % 10 == 0:
            print("🂺 and 🃖 - 🃁")
        elif i % 5 == 0:
            print("🃖 - 🃁")
        else:
            print(i)

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
def ejercicio4():
    sumaTotal = 0
    for i in range(0, 500001, 2):
        sumaTotal += i
    print(sumaTotal)


# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
def ejercicio5():
    for i in range(2024, -20, -3):
        print(i)


# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
def ejercicio6():
    inicio = 1234
    fin = 4321
    salto = 500

    for i in range(inicio, fin, salto):
        print(i)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10

# Codigo menú ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
continuar = True

while continuar:
    opcion = input("\n--- Elige una opción (1-15) (0 para salir) ---_")
    if opcion == "1":
        print("\n--- Ejecutando ejercicio uno ---")
        print(ejercicio1())
    elif opcion == "2":
        print("\n--- Ejecutando ejercicio dos ---")
        print(ejercicio2())
    elif opcion == "3":
        print("\n--- Ejecutando ejercicio tres ---")
        print(ejercicio3())
    elif opcion == "4":
        print("\n--- Ejecutando ejercicio cuatro ---")
        print(ejercicio4())
    elif opcion == "5":
        print("\n--- Ejecutando ejercicio cinco ---")
        print(ejercicio5())
    elif opcion == "6":
        print("\n--- Ejecutando ejercicio seis ---")
        print(ejercicio6())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("No válido...")