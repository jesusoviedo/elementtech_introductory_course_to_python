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


##Metacaracteres

# .  coincide con cualquier carácter excepto el salto de línea.
texto = "a-c"
patron = "a.c"
usando_expresiones_regulares(patron, texto)


# ^ coincide con el inicio de la cadena o de una línea.
texto = "amigo asdasd sadasdas asdasdas"
patron = "^A"
usando_expresiones_regulares(patron, texto)


# $ coincide con el final de la cadena o de una línea.
texto = "amigA"
patron = "A$"
usando_expresiones_regulares(patron, texto)


# * coincide con cero o más repeticiones del carácter o expresión anterior.
texto = "uen amigo"
patron = "b*"
usando_expresiones_regulares(patron, texto)


# + coincide con una o más repeticiones del carácter o expresión anterior.
texto = "hola mi amigo"
patron = "b+"
usando_expresiones_regulares(patron, texto)


# ? coincide con cero o una repetición del caracter o expresión anterior.
texto = "AAaana"
patron = "A?"
usando_expresiones_regulares(patron, texto)


# {n} coincide con exactamente n repeticiones del caracter o expresión anterior.
texto = "AALAaaana"
patron = "a{3}"
usando_expresiones_regulares(patron, texto)


# {n,m} coincide con entre n y m repeticiones del caracter o expresión anterior.
texto = "AAAAAAAAaaana"
patron = "A{2,6}"
usando_expresiones_regulares(patron, texto)


# [...] coincide con cualquier caracter que esté dentro de los corchetes}
texto = "hola amigo, que tal?"
patron = "[eusth]"
usando_expresiones_regulares(patron, texto)


# [^...] coincide con cualquier caracter que no esté dentro de los corchetes.
texto = "amigo,"
patron = "[^holamig,]"
usando_expresiones_regulares(patron, texto)


# | coincide con la expresión anterior o la siguiente.
texto = "igo mio como estas"
patron = "a|b|c|d"
usando_expresiones_regulares(patron, texto)


# (...) agrupa una parte de la expresión regular y la guarda como un grupo.
texto = "at como estas"
patron = "(a|b|c)(l|o)"
usando_expresiones_regulares(patron, texto)