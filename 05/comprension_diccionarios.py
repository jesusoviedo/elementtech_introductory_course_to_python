personas = {"Ana": 25, "Beto": 30, "Carla": 35}

dict_personas_2 = {}
for clave, valor  in personas.items():
   dict_personas_2[clave.upper()] = valor + 1

dict_personas_2 = {clave.upper(): valor + 1 for clave, valor in personas.items()}
print(dict_personas_2)

personas = {"Ana": 15, "Beto": 22, "Carla": 35, "David": 40, "Elena": 45}

mayores = {clave: valor for clave, valor in personas.items() if valor > 23.5}
print(mayores)

menores = {clave: valor for clave, valor in personas.items() if valor < 23.5}
print(menores)

compuesto = {clave.upper() if valor % 2 != 0 else clave : valor * 2 if valor % 2 == 0 else valor ** 3 for clave, valor in personas.items()}
print(compuesto)

# Crear un diccionario con los números del 1 al 10 como claves y sus cuadrados como valores.
diccionario = {x: x**2 for x in range(1, 11)}
print(diccionario)

# Crear un diccionario con las palabras de una frase como claves y sus longitudes como valores.
frase = "Python es un lenguaje de programación interpretado"
diccionario = {palabra: len(palabra) for palabra in frase.split()}
print(diccionario)

# Crear un diccionario con los elementos de otro diccionario que son múltiplos de 3 o de 5 como claves y sus valores incrementados en 1.
diccionario1 = {12: "a", 15: "b", 18: "c", 20: "d", 25: "e", 27: "f", 30: "g", 33: "h", 35: "i", 36: "j", 40: "k", 42: "l", 45: "m", 48: "n", 50: "o"}
diccionario2 = {k: chr(ord(v) + 1) for k, v in diccionario1.items() if k % 3 == 0 or k % 5 == 0}
print(diccionario2)