"""
Crea un diccionario con las letras del alfabeto y el número de veces que aparecen en la siguiente cadena, usando una comprensión de diccionario
"""

#cadena = "Zorroperezo O O o osoconej4 5144".lower()

cadena = input("Ingrese una cadena cualquiera: ").lower()

contador_letras = {"caracter_" + caracter: cadena.count(caracter) for caracter in cadena if caracter in "abcdefghijklmnopqrstuvwxyz"}

print(contador_letras)