numero = input("Ingrese un numero:")


try:
    operacion = 2 * int(numero)
except:
    print("No se puede realizar operaciones matematicas con cadenas")
else:
    print(operacion)



operacion = 0

try:
    operacion = 2 * int(numero)
except:
    print("No se puede realizar operaciones matematicas con cadenas")

print(operacion)



# Dividir un número por otro y manejar la división por cero
try:
    num1 = int(input("Ingrese el primer número: "))
    num2 = int(input("Ingrese el segundo número: "))
    resultado = num1 / num2
    print(f"El resultado de la división es {resultado}")
except (ZeroDivisionError, ValueError):
    print("No se puede dividir por cero/valor ingresado invalido")
except :
    print("Ocurrio un error inesperado")



# Acceder a un elemento de una lista y manejar el error de índice fuera de rango
lista = [24541, 2781, 300, 74, 557]

try:
    indice = int(input("Ingrese el índice del elemento que desea obtener: "))
    elemento = lista[indice]
except IndexError:
    print("El indice ingresado no es valido")
except:
    print("El indice debe ser un valor entero positivo")
else:
    print(f"El elemento en el índice {indice} es {elemento}")