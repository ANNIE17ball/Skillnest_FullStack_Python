import random
print("Hola Mundo ◝(ᵔᗜᵔ)◜")

nombre = input("Ingresa tu nombre: ")
print("hola", nombre.upper(), "(con coma)")
print("hola "+ nombre + " (con suma)")

nume = random.randint(0, 10)
num = str(nume)
print("Tú número de la buena suerte es:", num)

nume2 = random.randint(0, 10)
num2 = str(nume2)
print("Tú número de la mala suerte es: "+ num2)

com1 = input("Ingresa comida uno: ")

if com1 == "":
    print("Por favor ingresar valor uno")
else:
    com2 = input("Ingresa comida dos: ")
    if com2 == "":
        print("Por favor ingresar valor dos")
    else:
        print(f"Mis comidas favoritas son {com1} y {com2} (Con f-strings)")
        print("Mis comidas favoritas son {} y {} (Con format())".format(com2, com1))