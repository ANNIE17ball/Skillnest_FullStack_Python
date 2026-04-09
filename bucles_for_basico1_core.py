"""
En este archivo pondrás en práctica el uso de bucles 'for' en Python,
usando ejemplos inspirados en videojuegos y situaciones atractivas.
"""

# 1. Generador de niveles
# Imprime todos los niveles del 0 al 100 (incluyendo el 100).
for i in range(101):
    print(i)

# 2. Potenciadores de energía (Múltiplos de 2)
# Imprime los números múltiplos de 2 desde 2 hasta 500 (incluyendo el 500).
# (Tu código aquí)for i in range(101):
for i in range(2, 101, 2):
    print(i)

# 3. Trampa de emojis
# Recorre los puntos del 1 al 100.
# - Si el número es divisible por 5, imprime ""
# - Si es divisible por 10, imprime ""
# ¡Cuidado con la prioridad en tus condicionales!
for i in range(1, 101):
    if i % 10 == 0 and i % 5 == 0:
        print(".☘︎ ݁˖/˙ᵕ˙")
    elif i % 5 == 0:
        print("˙ᵕ˙")
    else:
        print(i)

# 4. Suma colosal
# Suma todos los números pares del 0 al 500,000 e imprime la suma total.
sumaTotal = 0
for i in range(5000000):
    if i % 2 == 0:
        sumaTotal += i
    else:
        continue
print(sumaTotal)


# 5. Retroceso temporal
# Desde 2024, retrocede de 3 en 3 hasta 0 o menos.
# Imprime cada valor en la cuenta regresiva.
for i in range(2024, -20, -3):
    print(i)


# 6. Contador dinámico
# Declara las variables inicio, fin, y salto (por ejemplo: inicio=3, fin=10, salto=2).
# Imprime los números en el rango que sean múltiplos de 'salto'.
inicio = 1234
fin = 4321
salto = 500

for i in range(inicio, fin, salto):
    print(i)

# Ejemplo: si inicio = 3, fin = 10, y salto = 2
# Se imprimiría: 4, 6, 8, 10