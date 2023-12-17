"""
Escribir una expresión regular que valide una fecha en formato dd/mm/aaaa` Por ejemplo, 13/02/1982 es una fecha válida, pero 32/49/1982 no lo es.
"""

import re


def validar_expresion(texto_ingresado):

    #patron = "^\d{2}/\d{2}/\d{4}$"

    patron = "^(0?[1-9]|[12][0-9]|3[01])/(0?[1-9]|1[012])/\d{4}$" #/((19|20)dd)$

    if re.search(patron, texto_ingresado):
        return "La fecha es valida"
    return "La fecha no es valida"

print(validar_expresion("01/12/2018"))
