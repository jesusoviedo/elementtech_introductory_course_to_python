"""
Escriba un programa que pida al usuario un número entero entre 1 y 10,
y luego le muestre la tabla de multiplicar de ese número usando un bucle for.

Si el usuario ingresa un número fuera del rango válido,
el programa debe mostrar un mensaje de error y volver a pedir
el número hasta que sea correcto.
"""

numero = int(input("Ingrese un numero entre 1 y 10: "))

while numero < 1 or numero > 10:
    print("Numero ingreso fueran del rango permitido (1-10)")
    print("")
    numero = int(input("Ingrese un numero entre 1 y 10: "))

print("")
print(f"Table de multiplicar del {numero}")

for elemento in range(1, 11):
    #producto = numero * elemento
    print("{1} x {2} = {0}".format(numero * elemento, numero, elemento))