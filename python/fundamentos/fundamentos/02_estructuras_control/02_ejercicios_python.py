"""
Iteracion y condicionales
"""

# Números Pares Dinámicos
"""Desarrolla un programa que solicite al usuario cuántos números pares desea ver ($n$)
. El programa debe imprimir los primeros $n$ números pares positivos."""

def numerosDinamicos():
    nume = int(input("Por favor ingresar un valor_"))

    if nume == "":
        print("Por favor ingresar un valor valido...")
    elif nume == 0:
        print("😡")
    else:
        for i in range(nume*2):
            if i % 2 == 0:
                print(i)
            else:
                continue

# Verificador de Edad y Acceso
"""
Pide al usuario su año de nacimiento. Calcula su edad y muestra si es mayor de edad (18+). 
Si tiene menos de 18, indica cuántos años le faltan para la mayoría de edad.
"""
def anios():
    año = int(input("Podrias ingresar tu año de nacimiento por favor?_"))
    edad = 2026 - año

    if edad >= 18:
        print("Ya estás grandecitooo")
    else:
        print(f"Estas pequeño, te falta/n {18 - edad} para ser mayor")

# Calculadora de Descuentos
"""
Solicita el precio de un producto y la cantidad comprada. Si el total supera los $100, 
aplica un 15% de descuento. Muestra el subtotal, el descuento aplicado y el total final
"""
def calculador():
    precio = int(input("Por favor ingresar precio del producto_"))
    cantidad = int(input("Por favor ingresar cantidad del producto_"))

    total = precio * cantidad
    if total > 100:
        descuento = total * 0.15
        print(f"Tu descuento da un total de {descuento}") 
    else:
        print("Casi tienes descuento... ￣\_(ツ)_/￣")

# Clasificador de Números
"""
Pide un número al usuario e indica si es: Positivo-Par,
Positivo-Impar, Negativo-Par, Negativo-Impar o Cero.
"""
def clasificador():
    num = int(input("Por favor ingresar un numero_"))
    if num == "":
        print("(  •̀ - •́  )")
    else:
        # negativo
        if num < 0:
            if num % 2 == 0:
                print(f"El {num} es negativo-par")
            else:
                print(f"El {num} es negativo-impar")
        # positivo
        elif num > 0:
            if num % 2 == 0:
                print(f"El {num} es positivo-par")
            else:
                print(f"El {num} es positivo-impar")
        else:
            print("Ese es el cero...")

# Tabla de Multiplicar Personalizada
"""
Solicita un número entero y muestra su tabla de multiplicar del 1 al 12, pero solo muestra
los resultados que sean múltiplos de 3.
"""
def entero():
    enteroo = int(input("Podrias ingresar un numero plis_"))
    for i in range(13):
        multi = i * enteroo
        if multi % 3 == 0:
            print(multi)
        else:
            continue

# Sumatoria con Centinela
"""
Crea un programa que pida números continuamente y los sume. El ciclo debe terminar cuando el usuario
ingrese un número negativo. Al final, muestra la suma total (sin incluir el negativo).
"""
def sumar():
    bucle = True
    ttal = 0
    while bucle:
        inp = int(input("Sumar:_"))
        if inp >= 0:
            ttal += inp
        else:
            bucle = False
            break
    print(ttal)

# Contador de Vocales
"""
Pide al usuario una frase o palabra. Utiliza un bucle para recorrer la cadena y contar cuántas
vocales tiene en total
"""
def frase():
    frase = input("Por favor ingresa una palabra:_")
    letras = 0
    for i in frase:
        letras += 1
    print(f"Tu palabra tiene un total de {letras} letras")

# Validación de Contraseña
"""
Define una contraseña en una variable. Pide al usuario que la intente adivinar.
Tienes un máximo de 3 intentos; si falla los 3, bloquea el acceso.
"""
def contraseña():
    contra = "RegnaD"
    intento = 0

    while intento < 3:
        show = input("Intenta adivinar mi contaseña...")
        if contra == show:
            print("Lo lograsteee!! ദ്ദി◝ ⩊ ◜.ᐟ")
            break
        else:
            print("Fallaste")
            intento += 1
    if intento >= 2:
        print("(─ ‿ ─)")

# Registro de Nombres
"""
Crea un arreglo vacío. Pide al usuario que ingrese 5 nombres. Guárdalos en el arreglo y, al final,
imprímelos en orden inverso al que fueron ingresados.
"""
def nombres():
    nombres = []
    maxi = 0
    while maxi < 5:
        nombre = input(f"Por favor ingresar nombre {maxi + 1}:_")
        if nombre != "":
            nombres.append(nombre)
            maxi += 1
        else:
            print("Tienes que ingresar un nombre")

    for i in range(4, -1, -1):
        print(nombres[i])

# Promedio de Notas
"""
Solicita al usuario cuántas notas desea ingresar. Almacena cada nota en un arreglo. Al finalizar,
calcula y muestra el promedio, la nota más alta y la más baja.
"""
def promedios():
    cant = int(input("Cuantas notas deseas ingresar:_"))
    total = 0
    vuelta = 0
    alta = 0
    baja = 90

    while vuelta < cant:
        nota = float(input(f"Ingresa tu nota {vuelta + 1}:_"))
        if nota < baja and nota >= 1.0:
            baja = nota
            total += nota
            
            vuelta += 1
        elif nota > alta and nota <= 7.0:
            alta = nota
            total += nota
        
            vuelta += 1
        else:
            print("Tienes que ingresar un valor valido...")
    print(f"Tu promedio es de {total/cant}, tu nota mas alta es {alta} y la mas baja es la {baja}")

# Filtro de Arreglos
"""
Dado un arreglo de números generado por el usuario, crea un nuevo arreglo que contenga solo los números 
que sean mayores a 50. Muestra ambos arreglos
"""
def filto():
    can = int(input("Cuantos numeros vas a ingresar?:_"))
    usuario = []
    for i in range(can + 1):
        inpu = int(input(f"Por favor ingresar numero {i + 1}"))
        if inpu == "":
            usuario.append(inpu)
    
    nuevoArreglo = []
    for i in range(len(usuario)):
        if usuario[i] >= 50:
            nuevoArreglo.append(usuario[i])