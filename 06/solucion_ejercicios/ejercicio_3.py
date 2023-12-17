"""
Escribir una expresión regular que valide una URL. Por ejemplo, https://pythondiario.com/ es una URL válida, pero htp://pythondiario.com no lo es.
"""

import re


def validar_expresion(texto_ingresado):

    patron = "^(https|http)://\w{5,50}.\w{3,15}/?$"

    if re.search(patron, texto_ingresado):
        return "La URL es valida"
    return "La URL no es valida"

print(validar_expresion("http://pythondiario.com/"))
