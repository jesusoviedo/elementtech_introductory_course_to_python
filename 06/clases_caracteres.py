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


##Clases de caracteres

# \d coincide con cualquier dígito. Es lo mismo que [0-9].
texto = "77 000at como estas "
patron = "\d{3}" #\d\d\d
usando_expresiones_regulares(patron, texto)


# \D coincide con cualquier carácter que no sea un dígito. Es lo mismo que [^0-9].
texto = "777451221h ola"
patron = "\D{3}"
usando_expresiones_regulares(patron, texto)


# \w coincide con cualquier carácter alfanumérico o guión bajo. Es lo mismo que [a-zA-Z0-9_].
texto = "Aa_7 como estas"
patron = "\w{6}"
usando_expresiones_regulares(patron, texto)


# \W coincide con cualquier carácter que no sea alfanumérico o guión bajo. Es lo mismo que [^a-zA-Z0-9_].
texto = "Aa_7-- --como estas"
patron = "\W{5}"
usando_expresiones_regulares(patron, texto)


# \s coincide con cualquier espacio en blanco, tabulación o salto de línea.
texto = "Aa_7--   --comoestas"
patron = "\s{2,4}"
usando_expresiones_regulares(patron, texto)


# \S coincide con cualquier carácter que no sea un espacio en blanco, tabulación o salto de línea.
texto = "wa_7--   --comoestas"
patron = "\S{6}"
usando_expresiones_regulares(patron, texto)