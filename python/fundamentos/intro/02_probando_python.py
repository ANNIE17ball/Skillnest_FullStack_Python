import random 
# libreria para utilizar el metodo ramdom(aleatorio)

"""
Este archivo sirve para practicar la ejecución de archivos en Python.
Incluimos un ejemplo con un bucle y selección aleatoria de días,
para que te familiarices con la terminal y el flujo básico de un programa.
"""

# Imprimimos un mensaje de bienvenida
print("¡Bienvenido a Python!")

# Explicamos lo que haremos a continuación
print("Ahora veremos un bucle que muestra los números del 1 al 10:")

# pedirle un numero al usuario
nume = input("Ingrese un numero limite: ")
limite = int(nume) # transformar el input a numero

# Bucle for que recorre los números del 1 al limite
for num in range(1, limite + 1):
    print(f"El valor actual de num es: {num}")

# Definimos una lista de días laborables
semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sabado", "Domingo"]

# Seleccionamos al azar un día de la semana
dia = random.choice(semana)
print(f"Hoy es: {dia}")

# Dependiendo del día, mostramos un mensaje motivacional distinto
if dia == "Lunes":
    print("¡Comenzamos la semana con buena energía!")
elif dia == "Viernes":
    print("¡Cerramos la semana listos para un buen descanso!")
elif dia == "Sabado" or dia == "Domingo": # if con or
    print("¡Aprovecha de descansar todo lo que puedas!")
else:
    print("¡Cada día es una nueva oportunidad de aprender!")