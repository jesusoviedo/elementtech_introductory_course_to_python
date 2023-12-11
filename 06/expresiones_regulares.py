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


# primer ejemplo
texto = "Hola, me llamo Ana y tengo 20 años"
patron = "a\w*o"
usando_expresiones_regulares(patron, texto)


# ver los siguientes archivos
# metacaracteres.py
# clases_caracteres.py
# modificadores.py







