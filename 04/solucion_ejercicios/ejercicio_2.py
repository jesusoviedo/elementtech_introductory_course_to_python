"""
Escriba un programa que cree una tupla con algunos nombres de frutas
y luego permita al usuario ingresar el nombre de una fruta.
El programa debe verificar si la fruta ingresada por el usuario está en la tupla y mostrar un mensaje apropiado.
"""

tup_frutas = ("manzana", "naranja", "plátano", "kiwi", "mango")

fruta_usuario = input("Ingrese el nombre de una fruta: ")

if fruta_usuario in tup_frutas:
    print("Sí, esa fruta está en la tupla.")
else:
    print("Lo siento, esa fruta no está en la tupla.")
