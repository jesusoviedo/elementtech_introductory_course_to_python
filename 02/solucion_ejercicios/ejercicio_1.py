"""
Escriba un programa que pida al usuario su nombre
y su edad, y luego le muestre un mensaje de bienvenida
y le diga cuántos años tendrá dentro de 10 años.
"""

nombre = input("¿Cómo te llamas? ")

edad = int(input("¿Cuántos años tienes? "))

edad += 10
#edad = edad + 10

print("")
print(f"Hola, {nombre}. Bienvenido a Python.")
print("Dentro de 10 años tendras {0} años".format(edad))
