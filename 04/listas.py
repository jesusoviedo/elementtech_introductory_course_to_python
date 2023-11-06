# Crear lista
mi_lista = [1, 2, 30, 5]

#posicion - valor
# 0 - 1
# 1 - 2
# 2 - 30
# 3 - 5

if 3 in mi_lista:
    print("El número 3 está en la lista.")
else:
    print("El número 3 no está en la lista.")

# Lista vacia
lista_nu = []
lista_nu = list()

# Agregar elementos a la lista con append()
lista_nu.append(-150)
lista_nu.append(-10)
lista_nu.append(10)
lista_nu.append(20)
lista_nu.append(30)

for elemento in lista_nu:
    print(elemento)
print()

# Agregar elementos de otra lista con extend()
otra_lista = [4, 5, 6]
lista_nu.extend(otra_lista)

for elemento in lista_nu:
    print(elemento)
print()

#modificar valor de un elemento
lista_nu[0] = -15

for elemento in lista_nu:
    print(elemento)
print()

# Insertar un elemento en una posición específica con insert()
lista_nu.insert(1, 458)

for elemento in lista_nu:
    print(elemento)
print()

# Eliminar el primer elemento con el valor especificado con remove()
lista_nu.remove(4)
lista_nu.remove(-15)

for elemento in lista_nu:
    print(elemento)
print()

# Eliminar el último elemento de la lista con pop()
valor_a = lista_nu.pop()
print(valor_a)

valor_a = lista_nu.pop()
print(valor_a)
print()

for elemento in lista_nu:
    print(elemento)
print()

# Encontrar la posición del primer elemento con el valor especificado con index()
numero = 20
if numero in lista_nu:
    posicion = lista_nu.index(numero)
    print(posicion)
    print()

lista_nu.append(10)
lista_nu.append(20)
lista_nu.append(30)
lista_nu.append(10)
lista_nu.append(20)
lista_nu.append(10)

# Contar el número de elementos con el valor especificado con count()
cantidad = lista_nu.count(300)
print(cantidad)
print()

for elemento in lista_nu:
    print(elemento)
print()

# Ordenar los elementos de la lista en orden ascendente reverse=False o descendente reverse=True con sort()
lista_nu.sort(reverse=True)

for elemento in lista_nu:
    print(elemento)
print()

otra_lista = [4, 5, 6, 2]

# Invertir el orden de los elementos en la lista con reverse()
otra_lista.reverse()

for elemento in otra_lista:
    print(elemento)
print()