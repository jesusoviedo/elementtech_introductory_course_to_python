"""
Escribir una expresión regular que valide una dirección IP. Una dirección IP es una secuencia
de cuatro números del 0 al 255, separados por puntos.
Por ejemplo, 192.168.0.1 es una dirección IP válida, pero 192.168.0.256 no lo es.
"""

import re

def validar_expresion(texto_ingresado):
    #"^(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$"
    patron = "^((25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)\.){3}(25[0-5]|2[0-4]\d|1\d\d|[1-9]\d|\d)$"

    return re.findall(patron, texto_ingresado)

cadena = input("Ingrese una direccion IP válida:")

print(validar_expresion(cadena))