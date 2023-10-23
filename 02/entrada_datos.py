nombre_ingresado = input("Ingrese su nombre: ")
print(nombre_ingresado)

anho_actual = 2023
anho_nacimiento = input("Ingrese el año de nacimiento:")
edad = anho_actual - int(anho_nacimiento)
print(edad)

altura = float(input("Ingrese su altura:"))
casado = bool(int(input("Estas casado 1 o 0:")))

print(altura)
print(casado)

print(bool(" *"))

#funcion int
s = "123"
n = int(s)
print(n)
print(type(n))

s = "12.3"
n = int(s)
# #ValueError: invalid literal for int() with base 10: '12.3'

#funcion float
s = "12.3"
n = float(s)
print(n)
print(type(n))

s = "hola"
n = float(s)
# ValueError: could not convert string to float: 'hola'

#funcion bool
s = "True"
b = bool(s)
print(b)
print(type(b))

s1 = "False"
s2 = ""
b1 = bool(s1)
b2 = bool(s2)
print(b1)
print(b2)

s1 = 1
s2 = 0
b1 = bool(s1)
b2 = bool(s2)
print(b1)
print(b2)