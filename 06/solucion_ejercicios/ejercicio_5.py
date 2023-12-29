"""
Escribir una expresión regular que valide un número de teléfono en formato +xx (xxx) xxx-xxxx,
donde x es un dígito. Por ejemplo, +54 (911) 123-4567 es un número de teléfono válido,
pero +55 911 123-4567 no lo es.
"""

import re

def validar_expresion(texto_ingresado):

    patron = "^\+\d{2}\s\(\d{3}\)\s\d{3}-\d{4}$"
    return re.findall(patron, texto_ingresado)

cadena = input("Ingrese un numero de telefono con el formato +xx (xxx) xxx-xxxx:")

#"+55 (911) 123-4567"
print(validar_expresion(cadena))