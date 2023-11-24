"""
Escriba un programa que cree un diccionario con los nombres de algunos países y sus capitales.
Luego, pida al usuario que ingrese el nombre de un país y muestre la capital correspondiente.
Si el país no está en el diccionario, el programa debe mostrar un mensaje.
"""

dict_capitales = {"Argentina": "Buenos Aires",
                  "Brasil": "Brasilia",
                  "Chile": "Santiago",
                  "Colombia": "Bogota",
                  "Peru": "Lima",
                  "Paraguay": "Asunción"}

pais = input("Ingrese el nombre de un país: ")

if pais in dict_capitales:
    print(f"La capital de {pais} es {dict_capitales[pais]}")
else:
    print(f"Lo siento no tengo información sobre el pais {pais}")