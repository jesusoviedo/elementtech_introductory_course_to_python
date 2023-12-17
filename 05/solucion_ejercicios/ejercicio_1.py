"""
Crea una lista con los números del 1 al 100 que sean múltiplos de 3 o de 5, usando una comprensión de lista
"""

limite_rango = int(input("Ingrese el limite del rango de numeros a recorrer que va ir desde 1: "))


multiplos = [numero for numero in range(1, limite_rango + 1) if numero % 3 == 0 or numero % 5 == 0]
print(multiplos)