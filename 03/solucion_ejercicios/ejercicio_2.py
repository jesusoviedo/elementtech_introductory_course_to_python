"""
Escribir una función llamada potencia que reciba dos números a y b como parámetros
y que devuelva el resultado de elevar a a la potencia b. Por ejemplo, potencia(2, 3) debe devolver 8.
"""

def potencia(a, b):
    if b == 0:
        return 1
    else:
        return a * potencia(a, b - 1)

print(potencia(2, 2))