# actividad: gestor de inventario

'''1) crear una lista llamada inventario que contenga los siguientes articulos
    'laptop', 'ratón', 'monitor', 'HDMI' '''
inventario = ['Laptop', 'Ratón', 'Monitor', 'HDMI']

'''2) utiliza un metodo para agregar impresora y teclado al final de la lista '''
inventario.append('Impresora')
inventario.append('Teclado')
print(inventario)
'''3) utiliza un metodo para mostrar cuantos elementos hay en la lista '''
print(len(inventario))

'''4) Modifica 'Teclado' por 'Teclado mecanico' '''
inventario[5] = 'Teclado mecanico'

'''5) Crea una lista promocion que contenga solo tres primeros elementos de la lista original '''
promocion = inventario[:3]
print(promocion)

'''6) Mostrar la lista de inventario ordenado alfabeticamente '''
print(sorted(inventario))

'''7) Elimina el ultimo elemento de la lista inventario y luego enseñalo junto la lista original '''
wasted = inventario.pop()

print(inventario)
print(wasted)