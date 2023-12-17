"""
Escribir una expresión regular que valide un correo electrónico. Por ejemplo, pythondiario@gmail.com es un correo válido, pero pythondiario@.com no lo es.
"""

import re


def validar_expresion(texto_ingresado):

    patron = "\w+@\w+.[a-zA-Z]{3,15}$"

    if re.search(patron, texto_ingresado):
        return "El correo es valido"
    #else:
    #    return "El correo no es valido"
    return "El correo no es valido"

print(validar_expresion("pythondiario@.com"))
