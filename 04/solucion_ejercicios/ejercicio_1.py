"""
Escriba un programa que pida al usuario una lista de números enteros y luego calcule la suma de los números en la lista.
"""
def ingresar_numero():
    return int(input("Ingrese un numero o -99 para finalizar el programa: "))


numero = ingresar_numero()
#numero = int(numero)

list_numero = []
#list_numero = list()


while numero != -99:
    list_numero.append(numero)
    numero = ingresar_numero()
    # numero = int(numero)


suma = 0
for elemento in list_numero:
    suma += elemento
    #suma = suma + elemento

print(f"La suma de los numeros es {suma}")