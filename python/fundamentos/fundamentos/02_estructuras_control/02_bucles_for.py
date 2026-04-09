for i in range(4): # for que repetira i hasta llegar al rango 4 (3)
    print(i)

for i in range(2, 8): # for que repetira i desde el 2 hasta llegar al rango 8 (7)
    print(i)

for i in range(2, 10, 3): # for que repetira i desde el 2 hasta llegar al rango 10 (9) de 3 en 3
    print(i)

# ejemplos
for i in range(0, 15, 3):
    print(i)  #Imprime: 0, 3, 6, 9, 12
for i in range(10, 1, -3):
    print(i)  #Imprime: 10, 7, 4

# bucle el cual recorre las letras(caracteres) de un string
for letra in 'Python':
    print(letra) #Imprime: 'P', 'y', 't', 'h', 'o', 'n'

"""
Estructuras de listas
"""

lista = ['brócoli', 'pepino', 'pimiento']

for i in range( len(lista) ):
    print(i, lista[i]) #Imprime n(i) verdura(i) por cada elemnto en la lista

for verdura in lista:
    print(verdura)  #Imprime una verdura(i) por cada elemento en la lista


tupla = ('fresa', 'manzana', 'cereza')

for i in range( len(tupla) ):
    print(i, tupla[i]) #Imprime: 0 fresa, 1 manzana, 2 cereza

for fruta in tupla:
    print(fruta) #Imprime: fresa, manzana, cereza


estudiante = {"nombre": "Gonzalo", "curso": "Python"}
for clave in estudiante:
    print(clave)
#Imprime: nombre, curso
for clave in estudiante:
    print(estudiante[clave])
#Imprime: Gonzalo, Python

platillos_tipicos = {"México": "Tacos", "Colombia": "Ajiaco", "Costa Rica": "Casado"}
#Otra forma de iterar a través de las claves (las llaves)
for clave in platillos_tipicos.keys():
    print(clave)
#Imprime: México, Colombia, Costa Rica

#Iteramos a través de los valores
for valor in platillos_tipicos.values():
    print(valor)
#Imprime: Tacos, Ajiaco, Casado

#Iteramos a través de los elementos (clave-valor)
for clave, valor in platillos_tipicos.items():
    print(clave, "=", valor)
#Imprime: México = Tacos, Colombia = Ajiaco, Costa Rica = Casado