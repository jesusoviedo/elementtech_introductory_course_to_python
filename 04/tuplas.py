# Crear una tupla
mi_tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 4, 4)

print(mi_tupla[0])

# error al querer modificar
#mi_tupla[0] = 5

# Contar el número de veces que aparece un elemento con count()
valor = 4

conteo = mi_tupla.count(valor)
print(f"{valor} aparece {conteo} veces")

# Encontrar el índice de la primera aparición de un elemento con index()
valor = 7

if valor in mi_tupla:
    posicion = mi_tupla.index(valor)
    print(f"{valor} esta en la posicion {posicion}")

for tup in mi_tupla:
    print(tup)