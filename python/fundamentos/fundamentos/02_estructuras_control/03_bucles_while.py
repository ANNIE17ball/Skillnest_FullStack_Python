# while condicion:
    #Código que se ejecuta mientras la condición se cumpla

# ejemplo:
num = 0
while num < 4:
    print("bucle while -", num)
    num += 1
#Imprime: bucle while - 0, bucle while - 1, bucle while - 2, bucle while - 3

num = 0
while num < 4:
    print("bucle while -", num)
    num += 1
else:
    print("Acabamos de salir del bucle")

"""
Controles de bucles -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
for letra in "detente":
    if letra == "n":
        break
    print(letra)
#Imprime: d, e, t, e

for letra in "detente":
    if letra == "n":
        continue
    print(letra)
#Imprime: d, e, t, e, t, e

x = 6
while x > 2:
    print(x)
    x -= 1
    if x == 3:
        break
else: #Recuerda: Solo se ejecuta en una salida normal, NO en un break
    print("Sentencia final")