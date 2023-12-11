#importar un modulo
import re

def usando_expresiones_regulares(patron, texto, modificador=None):

    if modificador:
        coincidencia = re.search(patron, texto, modificador)
    else:
        coincidencia = re.search(patron, texto)

    if coincidencia:
        print(f"Se encontró una coincidencia: {coincidencia.group()}")
        print(f"La coincidencia empieza en el índice {coincidencia.start()}")
        print(f"La coincidencia termina en el índice {coincidencia.end()}")
    else:
        print("No se encontró ninguna coincidencia")

##Modificadores
texto = "Me gusta programar en Python"
patron = "python"
usando_expresiones_regulares(patron, texto, re.I)


texto = """Hola, soy Javier
Me gusta viajar por el pais, hola.
hola¿Qué lugar deseas visitar?
hora"""

patron = "^[hH]o*"

list_coincidencias = re.findall(patron, texto, re.MULTILINE)

print(f"Se encontraron {len(list_coincidencias)} coincidencias")

print(list_coincidencias)