"""
Escribir una función llamada factorial que reciba un número entero positivo n como parámetro y que
devuelva el factorial de n. El factorial de un número es el producto de todos los números naturales
desde 1 hasta ese número. Por ejemplo, el factorial de 5 es 5 x 4 x 3 x 2 x 1 = 120.
"""

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))