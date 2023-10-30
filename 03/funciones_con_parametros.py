
"""
 Función con parámetros posicionales
"""
def multiplicacion(numero_1, numero_2):
    return numero_1 *  numero_2

#resultado = multiplicacion(4, 5)
#print(resultado)
print(multiplicacion(4, 5))
print("")

"""
 Función con parámetros por defecto
"""
def multiplicacion(numero_1, numero_2 = 5, resta_valor = 0):
    return numero_1 *  numero_2 - resta_valor

print(multiplicacion(4,8))
print("")

print(multiplicacion(70))
print("")

print(multiplicacion(15,2,10))


"""
 Función con parámetros por nombre
"""
def multiplicacion(numero_1, numero_2, resta_valor):
    return numero_1 *  numero_2 - resta_valor

print(multiplicacion(15, 10, 1))
print("")

print(multiplicacion(resta_valor=1, numero_1= 15, numero_2=10))
print("")

print(multiplicacion(15, numero_2=10, resta_valor=1))


"""
 Función con parámetros por nombre + Función con parámetros por defecto
"""
def multiplicacion(numero_1, numero_2, resta_valor=2):
    return numero_1 * numero_2 - resta_valor

print(multiplicacion(numero_1=15, numero_2=10))

"""
tupla
"""
tup_enteros = (1, 2, 3, 4)
for elemento in tup_enteros:
    print(elemento)

"""
diccionario
"""
dic_notas = {"Ariel": 91, "Javier": 85}
for clave, valor in dic_notas.items():
    print(clave, valor, sep=" -> ")

"""
  Función con  parámetros arbitrarios *
"""
def sumarN(*args):
    resultado = 0
    for elemento in args:
        #resultado = resultado +  elemento
        resultado += elemento

    print("La suma de los numeros es {0}".format(resultado))

sumarN()
sumarN(12)
sumarN(12, 45)
sumarN(12, 45, 45, 45, 78, 12, 415, 54)


"""
  Función con  parámetros arbitrarios **
"""
def imprimir(**kwargs):
    for key, value in kwargs.items():
        print(f"La clave es {key} y su valor es {value}")

imprimir()
imprimir(Nombre="Javier")
print()
imprimir(Name="Javier", Apellido="Riquelme")
print()
imprimir(Alias="Javier", Apodo="Riquelme", Edad= 31, Altura= 185)