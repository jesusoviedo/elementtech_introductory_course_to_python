"""
Escriba un programa que pida al usuario dos conjuntos de números enteros luego calcule la intersección
de los dos conjuntos. La intersección es el conjunto de elementos que aparecen en ambos conjuntos.
"""

def ingresar_numero():
    return int(input("Ingrese un numero o -99 para finalizar el programa: "))

def cargar_conjunto():
    conjunto_x = set()  # {}
    numero = ingresar_numero()

    while numero != -99:
        conjunto_x.add(numero)
        numero = ingresar_numero()

    return conjunto_x


conjunto_1 = cargar_conjunto()
conjunto_2 = cargar_conjunto()

interseccion = conjunto_1.intersection(conjunto_2)
print(interseccion)