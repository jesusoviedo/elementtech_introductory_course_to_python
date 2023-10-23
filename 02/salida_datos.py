#print
print("Hola", "Mundo")
print("Hola", "Mundo", "Como",  "Estan", sep=":")
print("Me llamo", "Isa", end="_", sep=":")
print("Belen")


print("Nombre", "Edad", "Altura", sep=":", end="\n\n")
print("Ana", 25, 1.65, sep=":", end="\t\t\t")
print("Luis", 30, 1.75, sep=":", end="\n\n\n\n")


#format
nombre = "Lilian"
edad = 30
altura = 1.6545123457421

print("Mi nombre es {0} tengo {1} años y mi altura es de {2}".format(nombre,edad,altura))

print("Mi nombre es {nom} tengo {ed} años y mi altura es de {alt}".format(ed=edad, alt=altura, nom=nombre))

print("Mi nombre es {nom:*<10} tengo {ed} años y mi altura es de {alt:.4f}".format(ed=edad, alt=altura, nom=nombre))

#*>5 Alinea a la derecha y rellena con asteriscos
#<5 Alinea a la izquierda
#^5 Centra
#b Convierte a binario


#f-string
nombre = "Lilian"
edad = 30
altura = 1.6545123457421

print(f"Mi nombre es {nombre} tengo {edad} años y mi altura es de {altura}")

print(f"Mi nombre es {nombre:-^15} tengo {edad} años y mi altura es de {altura:.3f}")