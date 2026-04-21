"""
FUNCIONES
"""

# Función de tacos
def taco(tortilla, guiso, salsa, complementos):
    # Instrucciones de preparación
    print("Calentar la tortilla")
    print("Preparar el guiso")
    print(f"Colocar {guiso} en la tortilla")
    print(f"Poner un poco de {salsa}")
    print(f"Agregar {complementos}")
    
    # Servimos nuestro taco
    return f"Taco de {guiso} con {salsa} y {complementos} en {tortilla}"

# Llamada correcta
comida = taco("tortilla de maíz", "carne asada", "salsa verde", ["cebolla", "cilantro", "guacamole"])
print(comida)

def multiplicacion(num1, num2): #definimos la función multiplación con los parámetros num1 y num2
    resultado = num1 * num2     #instrucciones dentro de la función
    return resultado            #regresamos valor de resultado

a = int(input("Por favor ingrese un numero:_"))
b = int(input("Por favor ingrese otro numero:_"))

resultado_multiplicacion = multiplicacion(a, b) #Llamado a la función con argumentos a y b
print(resultado_multiplicacion) #Se guarda en la variable el resultado que la función regresó. Imprime: 25

def buenos_dias(nombre):
    print("Buenos días "+nombre)

buenos_dias("alegría")
buenos_dias("al amor")
buenos_dias("a la vida")
buenos_dias("señor Sol")


# devoluicion de valores
def buenos_dias_dos(nombre):
    return "Buenos días "+nombre
# El valor de retorno de la función es "Buenos días Python", por lo que el valor de mi
# variable frase será ese

frase = buenos_dias_dos("Python")
print(frase) #Imprime: Buenos días Python

# ejercicio de retorno de valor...
# crear ejercicio reciva dos parametros y que devuelva el valor de una frase completa e imprimir
def creacion(clima, temperatura):
    return "Hoy hay " + clima + ", por lo tanto hace mucho " + temperatura

clim = input("Como está a fuera??:_")
temp = input("Hace frio o calor??:_")

frass = creacion(clim, temp)
print(frass)