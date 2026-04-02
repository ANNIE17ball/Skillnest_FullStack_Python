"""
Este archivo demuestra varios conceptos básicos en Python.
Completa los comentarios en cada línea para relacionarlos
con los conceptos enumerados en 'reconocer.md'.
"""


import random #importacion libreria para procesos aleatorios


nombre = "Frida Kahlo" # creación de variable tipo string a la cual se le asigno un valor
print(type(nombre)) # metodo de PYTHON para mostrar tipo de dato de una variable
print(len(nombre)) # len(): devuelve el largo la variable nombre en la consola


nume = input("➤ Ingresa tu edad ")
edad = int(nume) # creación de variable tipo int a la cual se le asigno el valor de nume


#if - else
if edad < 18: # se establece condicion if
   print("Eres menor de edad.") # lo que sucederá si se cumple la condicion
elif edad == 18: # se establece condicion else if
   print("Tienes 18 años.") # lo que sucederá si se cumple la condicion
else: # se establece condicion else si no se cumple ninguna de las otras condiciones
   print("Eres mayor de edad.") # lo que sucederá si se cumple la condicion


frutas = ["manzana", "pera", "fresa"] # declara variable tipo array
print(frutas[0]) # imprime la primera pocision del array frutas (manzana)
frutas[0] = "platano" # declara que la primera posicion del array va a ser platano
frutas.append("uva") # append(): agrega un elemento al final del array
frutas.remove("pera") # remove(): elimina el elemento del array ("pera")


dimensiones = (200, 50) # declara una variable tipo tupla (variable inmutable)
print(dimensiones[0]) # imprime la posicion 0 de la variable creada


persona = { # declara variable tipo objeto (object)
   "nombre": "Carlos", # declara un item y su valor
   "edad": 30 # declara un item y su valor
}
print(persona["nombre"]) # imprime el item "nombre" de la variable persona
persona["edad"] = 31 # se modifica el valor del item "edad"
persona["ciudad"] = "Santiago" # agrega item a "persona" con un valor
del persona["ciudad"] # elimina el item "ciudad" completo de persona

#bucle for
titi = input("Por favor ingresa otro numero... ")
rango = int(titi)
for i in range(rango + 1): # bucle for: se establece un RANGo con limite del numero del usuario
   if i % 2 == 0: # se establece condicion si i == 2
      continue # contunue: ignora proceso y continua
   if i == rango + 1:# se establece condicion si i == limite del bucle
      break # si se cumple se rompe el bucle
print(i) # imprime i

contador = 0 # se declara variable int 
while contador < 3: # se crea bucle while con condicion
   print(f"while contador es: {contador}") # imprime el contador en un mensaje concatenado con f(string)
   contador += 1 # aumenta el contador en 1


def saludar_usuario(nombre): # def: se crea una funcion llamada saludar_usuario
   return f"Hola, {nombre}" # devuelve el valor de la funcion


print(saludar_usuario("Francisca")) # llama la funcion saludar_usuario y se el asigna un parametro