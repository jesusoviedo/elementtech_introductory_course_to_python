"""
Crea una lista con las palabras que empiezan y terminan con la misma letra de la siguiente cadena, usando una comprensión de lista

"El elefane es elegante y elocuente"
"""

#mensaje = "El elefane es elegante y elocuente"
#palabras_list = mensaje.split(" ")

mensaje = input("Ingrese una frase: ")
mensaje = mensaje.lower()

listado_final = [palabra.upper() for palabra in mensaje.split(" ") if palabra[0] == palabra[-1] and len(palabra) > 1]

print(listado_final)