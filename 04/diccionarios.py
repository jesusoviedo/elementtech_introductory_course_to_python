# Diccionario vacio

dict_vacio = dict()
dict_vacio = {}

# Crear un diccionario
mi_diccionario = {"nombre": "Juan",
                  "edad": 30,
                  "ciudad": "Buenos Aires"}

# Obtener todas las claves con keys()
claves = mi_diccionario.keys()
for clav in claves:
    print(clav)
print()

# Obtener todos los valores con values()
valores = mi_diccionario.values()
for val in valores:
    print(val)
print()

# Obtener todos los pares clave-valor con items()
items = mi_diccionario.items()
print(items)
print()

for clav, val in mi_diccionario.items():
    print(f"{clav} -> {val}")
print()

# Obtener el valor asociado con una clave específica con get()
val = mi_diccionario.get("edad")
print(val)
print()

# Obtener el valor asociado con una clave específica con get()
val = mi_diccionario.get("edaD", "clav_invalida")
print(val)
print()

# Actualizar el diccionario con update()
mi_diccionario.update( {"edad": 31, "profesión": "programador"}  )
for clav, val in mi_diccionario.items():
    print(f"{clav} -> {val}")
print()

# Agregar par clav valor
mi_diccionario["pais"] = "paraguay"

# Eliminar todos los elementos del diccionario con clear()
mi_diccionario.clear()
print(len(mi_diccionario))