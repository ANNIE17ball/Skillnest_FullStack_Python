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
            print(f"Lo lograsteee!! ദ്ദി◝ ⩊ ◜.ᐟ al {intento} intento")
            break
        else:
            print("Fallaste")
            intento += 1
    if intento == 3:
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
    for i in range(can):
        inpu = int(input(f"Por favor ingresar numero {i + 1}:_"))
        if inpu != "":
            usuario.append(inpu)
        else:
            print("No puedes reponer ese numero...")
    
    nuevoArreglo = []
    for i in range(len(usuario)):
        if usuario[i] >= 50:
            nuevoArreglo.append(usuario[i])
    print(usuario)
    print(nuevoArreglo)

# Buscador de Elementos
"""
Crea una lista de 10 ciudades. Pide al usuario que ingrese el nombre de una ciudad y el programa debe
decir si la ciudad se encuentra en la lista y en qué índice (posición) está
"""
def elementos():
    ciudades = ["Nairobi", "Tokio", "Denver", "Berlin", "Denver", 
                "Rio", "Helsinki", "Marsella", "Helsinki", "Moscu",]
    ciudad = input("Por favor ingresar una ciudad con mayuscula al principio:_")
    
    esta = ciudades.index(ciudad)
    if esta < len(ciudades):
        print(f"Tu ciudad si está y se encuentra en la posición {esta}")
    else:
        print("Nop, tu ciudad no está...")

# Simulación de Inventario
"""
Crea dos arreglos: uno para nombres_productos y otro para precios. Permite al usuario ingresar
3 productos con sus precios. Luego, muestra una lista formateada: Producto: [Nombre] - Precio: $[Valor].
"""
def dosArreglos():
    productos = []
    precios = []
    
    maxi = 0
    while maxi < 3:
        producto = input("Por favor ingresar producto:_")
        if producto != "":
            precio = int(input("Por favor ingresar precio:_$"))
            if precio != "" and precio != 0:
                productos.append(producto)
                precios.append(precio)
                maxi += 1
            else:
                print("Por favor ingresar elemento valido")
        else:
            print("Por favor ingresar elemento valido")
    
    for i in range(3):
        print(f"Producto: [{productos[i]}] - Precio: ${[precios[i]]}")

# Generador de Lista de Compras
"""
Usa un bucle while para que el usuario agregue artículos a una lista de compras. El proceso
termina cuando el usuario escribe "terminar".Al final, muestra la lista ordenada alfabéticamente.
"""
def articulos():
    print("Que deseas ingresar??")
    compras = []
    ok = True

    while ok:
        cosas = input("> ")
        
        if cosas.lower() == "terminar":
            print("Terminando la lista")
            ok = False
        elif cosas != "":
            compras.append(cosas)
        else:
            print("Por favor ingresar elemento valido")
    print(sorted(compras))

# Análisis de Temperaturas
"""
Solicita las temperaturas de los 7 días de la semana y guárdalas en un arreglo. Muestra:
El promedio semanal.
Cuántos días la temperatura fue superior a 25 grados.
El día con la temperatura más baja (asumiendo que el índice 0 es Lunes).

"""
def semana():
    dias = ["Luenes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
    diasSuperior = []
    total = 0
    baja = 100
    cant = 0
    
    while cant < 7:
        temps = float(input(f"Ingresa temperatura del dia {dias[cant]}:_"))
        total += temps
        if temps == "":
            print("Por favor ingresar valor valido...")
            break
        elif temps < baja:
            baja = temps
        elif temps > 25:
            diasSuperior.append(dias[cant])
        else:
            pass
        cant += 1
        
    print(f"El primedio de las temperaturas de la semana son de {total / 7}° la temperatura mas baja fue {baja}° y los dias mas calurosos fueron {diasSuperior}")


# Codigo menú ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
continuar = True

while continuar:
    print("\n--- ejercicios python ---")
    print("--- 1-. ejercicios uno ---")
    print("--- 2-. ejercicios dos ---")
    print("--- 3-. ejercicios tres ---")
    print("--- 4-. ejercicios cuatro ---")
    print("--- 5-. ejercicios cinco ---")
    print("--- 6-. ejercicios seis ---")
    print("--- 7-. ejercicios siete ---")
    print("--- 8-. ejercicios ocho ---")
    print("--- 9-. ejercicios nueve ---")
    print("--- 10-. ejercicios diez ---")
    print("--- 11-. ejercicios once ---")
    print("--- 12-. ejercicios doce ---")
    print("--- 13-. ejercicios trece ---")
    print("--- 14-. ejercicios catorce ---")
    print("--- 15-. ejercicios quince ---")
    opcion = input("\n--- Elige una opción (1-15) (0 para salir) ---_")
    if opcion == "1":
        print("\n--- Ejecutando ejercicio uno ---")
        print(numerosDinamicos())
    elif opcion == "2":
        print("\n--- Ejecutando ejercicio dos ---")
        print(anios())
    elif opcion == "3":
        print("\n--- Ejecutando ejercicio tres ---")
        print(calculador())
    elif opcion == "4":
        print("\n--- Ejecutando ejercicio cuatro ---")
        print(clasificador())
    elif opcion == "5":
        print("\n--- Ejecutando ejercicio cinco ---")
        print(entero())
    elif opcion == "6":
        print("\n--- Ejecutando ejercicio dos ---")
        print(sumar())
    elif opcion == "7":
        print("\n--- Ejecutando ejercicio siete ---")
        print(frase())
    elif opcion == "8":
        print("\n--- Ejecutando ejercicio ocho ---")
        print(contraseña())
    elif opcion == "9":
        print("\n--- Ejecutando ejercicio nueve ---")
        print(nombres())
    elif opcion == "10":
        print("\n--- Ejecutando ejercicio diez ---")
        print(promedios())
    elif opcion == "11":
        print("\n--- Ejecutando ejercicio once ---")
        print(filto())
    elif opcion == "12":
        print("\n--- Ejecutando ejercicio doce ---")
        print(elementos())
    elif opcion == "13":
        print("\n--- Ejecutando ejercicio trece ---")
        print(dosArreglos())
    elif opcion == "14":
        print("\n--- Ejecutando ejercicio catorce ---")
        print(articulos())
    elif opcion == "15":
        print("\n--- Ejecutando ejercicio quince ---")
        print(semana())
    elif opcion == "0":
        print("Saliendo...")
        continuar = False
    else:
        print("No válido...")