lista_n = [1, 2, 3, 4, 5, 6, 7, 8]

lista_cuadrado = []
for elemento in lista_n:
    lista_cuadrado.append(elemento ** 2)

lista_cuadrado = [elemento ** 2 for elemento in lista_n]
print(lista_cuadrado)

pares = [numero for numero in range(1, 21) if numero % 2 == 0]
print(pares)

impares = [numero for numero in range(1, 21) if numero % 2 != 0]
print(impares)

valores_complejos = [numero / 2 if numero <= 10 else numero ** 2 - 100 for numero in range(1, 21)]
print(valores_complejos)

# Crear una lista con los elementos de otra lista que son múltiplos de 3 o de 5.
lista1 = [12, 15, 18, 20, 25, 27, 30, 33, 35, 36, 40, 42, 45, 48, 50]
lista2 = [x for x in lista1 if x % 3 == 0 or x % 5 == 0]
print(lista2)

# Crear una lista con los nombres de los países que tienen más de 5 letras y que contienen la letra 'a'.
paises = ["Paraguay", "Argentina", "Brasil", "Chile", "Uruguay", "Bolivia", "Perú", "Ecuador", "Colombia", "Venezuela"]
lista = [pais for pais in paises if len(pais) > 5 and 'a' in pais]
print(lista)

# Crear una lista con los números primos del 1 al 100.
def es_primo(n):
  # Función que verifica si un número es primo o no
  if n < 2:
    return False
  for i in range(2, int(n**0.5) + 1):
    if n % i == 0:
      return False
  return True

lista = [x for x in range(1, 101) if es_primo(x)]
print(lista)





