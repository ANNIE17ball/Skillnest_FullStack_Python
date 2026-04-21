"""
Practica funciones basicas practica dos
"""

# 1-. Calcula experiencia -------------------------------------------------------------------------------------
lista = []
def multiplica_por_2(num):
    for i in range(num + 1):
        lista.append( 2 * i )
    return lista

print(multiplica_por_2(5))

# 2-. Analiza publicaciones ------------------------------------------------------------------------------------------------------
def suma_y_resta(a):
    print(a[0] + a[1])
    return a[0] - a[1]

print(suma_y_resta([120, 115]))
# Imprime: 235 y retorna: 5

# 3-. Puntaje ajustado -------------------------------------------------------------------------------------------------------------
def sumatoria_menos_longitud(b):
    suma_total = 0
    for i in range(len(b)):
        suma_total += b[i]
    print(f"Suma total = {suma_total}, longitud = {len(b)}")
    return suma_total - len(b)

print(sumatoria_menos_longitud([10, 5, 3, 7]))

# 4-. Ajusta visualizaciones -----------------------------------------------------------------------------------------------

def valores_multiplicados_segundo(c):
    resultado = []
    print(len(c))
    for i in range(len(c)):
        resultado.append(c[i] * (len(c)-1))
    
    return resultado

print(valores_multiplicados_segundo([100, 3, 50, 20]))
# Imprime: 4 y retorna: [300, 9, 150, 60]
print(valores_multiplicados_segundo([100]))
# Imprime: 1 y retorna: []

# 5-. Genera precio fijo --------------------------------------------------------------------------------------------------------------
def valor_multiplicado_longitud(a, b):
    resultado = []
    for i in range(b):
        resultado.append(a * b)
    return resultado

print(valor_multiplicado_longitud(5, 2))
# Debe retornar: [10, 10]

print(valor_multiplicado_longitud(7, 5))
# Debe retornar: [35, 35, 35, 35, 35]