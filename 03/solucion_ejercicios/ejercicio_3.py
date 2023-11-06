"""
Escribir una función llamada suma que reciba un número variable
de argumentos posicionales y que devuelva la suma de todos ellos.
Por ejemplo, suma(1, 2, 3) debe devolver 6. Si no se pasa ningún argumento, se debe devolver 0.
"""

def suma(*args):
  resultado = 0

  for arg in args:
    resultado += arg

  return resultado

print(suma(4,5, 8, 9, 7, 784, 145))