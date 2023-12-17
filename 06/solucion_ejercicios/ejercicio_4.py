"""
Escribir una expresión regular que extraiga todas las palabras que contengan una letra con tilde o una ñ.
Por ejemplo, en el texto `Niño, Acción, Perro, Lobo, Expresión, Español` se deben extraer `Niño, Acción, Expresión, Español`.
"""

import re


def validar_expresion(texto_ingresado):

    patron = "\w*[áéíóúñÀÈÌÒÙÑ]\w*"
    return re.findall(patron, texto_ingresado)

print(validar_expresion("Niño, Acción, Perro, Lobo, Expresión, Español"))
