"""
Escribir una expresión regular que valide una contraseña que tenga al menos una letra mayúscula,
una letra minúscula, un dígito y un carácter especial (`!@#$%^&*`).

La longitud mínima de la contraseña debe ser de 8 caracteres.

Por ejemplo, P@ssw0rd! es una contraseña válida, pero password no lo es.
"""

import re

def validar_expresion(texto_ingresado):

    patron = "^(?=.*[A-Z])(?=.*[a-z])(?=.*d)(?=.*[!@#$%^&*]).{8,}$"
    return re.findall(patron, texto_ingresado)

cadena = input("Ingrese una contreseña válida:")

print(validar_expresion(cadena))