#for y range
valor_final = int(input("Ingrese el valor tope de la operacion:"))


for elemento in range(valor_final):
    print(elemento)
print("*" * 50)


for x in range(valor_final):
    print(x**2)
print("*" * 50)


for x in range(valor_final - 5, valor_final):
    print(x)
print("*" * 50)


for x in range(valor_final - 20, valor_final, 2):
    print(x)
print("*" * 50)

list_nombres = ["Jesus", "Javier", "Lola", "Itachi", "Tiri"]

for nombre in list_nombres:
    print(nombre)

list_numeros = [0, 100, 50, 11, 150, 45, 541, 454, 1215, 415456, 3, 5]

#break y continue
for numero in list_numeros:
    if numero == 45:
        break
    if numero % 2 == 0:
        continue
    print(numero)

# Generar una secuencia desde 0 hasta 9
for i in range(10):
    print(i, end=", ")

# Generar una secuencia desde 5 hasta 14
for i in range(5, 15):
    print(i, end=", ")

# Generar una secuencia desde -10 hasta -1
for i in range(-10, 0):
    print(i, end=", ")

# Generar una secuencia desde 0 hasta 20 de dos en dos
for i in range(0, 21, 2):
    print(i, end=", ")

# Generar una secuencia desde 10 hasta -10 de tres en tres
for i in range(10, -11, -3):
    print(i, end=", ")