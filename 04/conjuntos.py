# Crear un conjunto
mi_conjunto = {1, 2, 3}

# Agregar un elemento con add()
mi_conjunto.add(4)

for conjunto in mi_conjunto:
    print(conjunto)
print()

# Crear una copia con copy()
otro_conjunto = mi_conjunto.copy()
print()
print(len(mi_conjunto))
print()
# Eliminar todos los elementos con clear()
mi_conjunto.clear()

for conjunto in otro_conjunto:
    print(conjunto)
print()

print(len(mi_conjunto))
print()

# Eliminar un elemento con discard()
otro_conjunto.discard(30)
for conjunto in otro_conjunto:
    print(conjunto)
print()

# Eliminar un elemento con remove()
otro_conjunto.remove(2)
for conjunto in otro_conjunto:
    print(conjunto)
print()

# Eliminar y devolver un elemento aleatorio con pop()
elemento = otro_conjunto.pop()
for conjunto in otro_conjunto:
    print(conjunto)
print()

# Unir dos conjuntos con union()
mi_conjunto = {1, 2, 3, 4, 5, 6}
union = otro_conjunto.union(mi_conjunto)
for conjunto in union:
    print(conjunto)
print()

# Encontrar la diferencia entre dos conjuntos con difference()
diferencia = {1, 2, 3}.difference({2, 3, 4})
print(diferencia)

# Encontrar la intersección entre dos conjuntos con intersection()
interseccion = {1, 2, 3}.intersection({2, 3, 4})
print(interseccion)

# Verificar si dos conjuntos son disjuntos con isdisjoint()
disjunto = {1, 2, 3}.isdisjoint({4, 5, 6})
print(disjunto)

# Verificar si un conjunto es subconjunto de otro con issubset()
subconjunto = {1, 2, 5}.issubset({1, 2, 3, 5})
print(subconjunto)

# Verificar si un conjunto es superconjunto de otro con issuperset()
superconjunto = {1, 2, 3, 5}.issuperset({1, 2, 5})
print(superconjunto)

# Encontrar la diferencia simétrica entre dos conjuntos con symmetric_difference()
diferencia_simetrica = {1, 2, 3}.symmetric_difference({2, 3, 4})
print(diferencia_simetrica)