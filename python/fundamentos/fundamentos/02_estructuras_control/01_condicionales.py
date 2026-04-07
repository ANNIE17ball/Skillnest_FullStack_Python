num = 15
if num > 20:
    print("Número mayor a 20")
else:
    print("Número menor a 20")
'''
La variable num es menor a 20, por lo que el bloque de código de else será ejecutado.
Es decir que vamos a imprimir "Número menor a 20"
'''
num = 101
if num > 50:
    print("Número mayor a 50")
elif num > 100:
    print("Número mayor a 100")
else:
    print("Número menor a 10")
'''
A pesar de que num es mayor que 50 y 100, la primera condicional que se cumpla es la única que se ejecutará.
Es por eso que solo imprimirá: "Número mayor a 50"
'''
if num < 60:
    print("Número menor a 50")
#No se cumple con la condicional, por lo que no se ejecuta el bloque de código

# tarea: Ingresar tres numeros por teclado e identificar mayor y menor
num1 = int(input("Por favor ingresar numero uno: ")) # es como el parse int
num2 = int(input("Por favor ingresar numero dos: "))
num3 = int(input("Por favor ingresar numero tres: "))

# El mas facil
if num1 >= num2 and num1 >= num3:
    mayor = num1
    if num2 <= num3:
        menor = num2
    else:
        menor = num3
elif num2 >= num1 and num2 >= num3:
    mayor = num2
    if num1 <= num3:
        menor = num1
    else:
        menor = num3
elif num3 >= num1 and num3 >= num2:
    mayor = num3
    if num1 <= num2:
        menor = num1
    else:
        menor = num2
print(f"El numero mayor es {mayor} y el menor es {menor}")

"""# todos iguales
if num1 == num2 and num2 == num3:
    print("Los tres numeros son iguales")
# si los dos primeros son iguales y el ultimo es menor
elif num1 == num2 and num1 > num3:
    print(f"Los prmeros dos numeros son iguales y {num3} es menor")
# si los dos ultimos son iguales y el primero es menor
elif num2 == num3 and num3 > num1:
    print(f"Los ultimos dos numeros son iguales y {num1} es menor")
# si el primer y el ultimo numero son iguales y el otro es menor
elif num3 == num1 and num1 > num2:
    print(f"El primer y el ultimo numero son iguales y {num2} es menor")
# numero uno mayor
elif num1 > num2 and num1 > num3 :
    print(f"El número {num1} es mayor")
    if num2 != num3:
        if num2 < num3:
            print(f"El número {num2} es menor")
        else:
            print(f"El número {num3} es menor")
    else:
        print("No hay un menor")
# numero dos mayor
elif num2 > num1 and num2 > num3:
    print(f"El número {num2} es mayor")
    
    if num1 != num3:
        if num1 < num3:
            print(f"El número {num1} es menor")
        else:
            print(f"El número {num3} es menor")
    else:
        print("No hay un menor")
#numero tres mayor
elif num3 > num1 and num3 > num2:
    print(f"El número {num3} es mayor")
    if num2 != num1:
        if num2 < num1:
            print(f"El número {num2} es menor")
        else:
            print(f"El número {num1} es menor")
    else:
        print("No hay un menor")"""