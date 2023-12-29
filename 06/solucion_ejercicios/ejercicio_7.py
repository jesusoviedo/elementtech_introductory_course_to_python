"""
Escribir una expresión regular que valide un número hexadecimal.
Un número hexadecimal es una combinación de dígitos del 0 al 9
y letras de la A a la F (a-f), precedido por el símbolo #.
Por ejemplo, #FF00FF es un número hexadecimal válido, pero #GG00GG no lo es.
"""

import re

def validar_expresion(texto_ingresado):

    patron = "^#([0-9A-Fa-f]{3}|[0-9A-Fa-f]{6})$"
    return re.findall(patron, texto_ingresado)

cadena = input("Ingrese un numero hexadecimal:")

print(validar_expresion(cadena))