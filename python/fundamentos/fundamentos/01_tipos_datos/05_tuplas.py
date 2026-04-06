# las TUPLAS son listas inmutables
tupla_letras = ("a", "e", "i", "o", "u")
tupla_sin_parentesis = "a", "e", "i", "o", "u"

# se pueden formar por cualquier tipo de dato
gato = ("Miau", 5, "persa", False)
print(gato[0]) #Imprime: Miu

# las tuplas no se pueden modificar
gato[0] = "Michi" #ERROR: TypeError: 'tuple' object does not support item assignment

# a gato se le inserta un dato
gato = gato + ("4.1",)
print(gato) #Imprime: ('Miu', 5, 'persa', False, '4.1')

# tuplas dentro de funciones
def suma_multiplicacion(x, y):
    suma = x + y
    multiplicacion = x * y
    return (suma, multiplicacion) # retorna una tupla

print(suma_multiplicacion(10, 5))