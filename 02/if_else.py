#if else
numero = int(input("Ingrese un valor numerico: "))

if numero % 2 == 0:
    print(f"El valor ingresado es par: {numero}, y su division con 3 es {numero/3.5:.2f}")
else:
    print(f"El valor ingresado no es par: {numero}, y su division con 3 es {numero/3.5:.2f}")



#if elif
calificacion = int(input("Ingrese una calificacion: "))

if calificacion > 90:
    print("Aprobaste con 5")
elif calificacion > 80:
    print("Aprobaste con 4")
elif calificacion > 70:
    print("Aprobaste con 3")
elif calificacion > 60:
    print("Aprobaste con 2")
else:
    print("No aprobaste")


año = int(input("Ingrese el año: "))
if año % 4 == 0:
    if año % 100 == 0:
        if año % 400 == 0:
            print("El año es bisiesto")
        else:
            print("El año no es bisiesto")
    else:
        print("El año es bisiesto")
else:
    print("El año no es bisiesto")


#operador ternario
numero = int(input("Ingrese un valor numerico: "))

if numero % 2 == 0:
    print(f"El valor ingresado es par: {numero}")
else:
    print(f"El valor ingresado no es par: {numero}")


resultado = "El valor ingresado es par" if numero % 2 == 0 else "El valor ingresado no es par"
print(resultado)


x = -5
signo = "negativo" if x < 0 else "positivo"
print(signo)


edad = 18
print("Mayor de edad" if edad >= 18 else "Menor de edad")