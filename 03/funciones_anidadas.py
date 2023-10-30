"""
closure
"""

#funcion externa
def saludo(nombre):
    mensaje = "Hola"

    # funcion interna
    def mostrar(apellido):
        print(mensaje, nombre, apellido)

    #retornar la funcion interna
    return mostrar


funcion_interna = saludo("Jesus Javier")
funcion_interna("Oviedo")


"""
 forma 1 decorador
"""
def decorar(funcion):
    def nueva_funcion():
        print("Antes de usar la funcion saludo")
        funcion()        
        print("Despues de usar la funcion saludo")

    return nueva_funcion


def saludo():
    print("Hola soy la funcion saludo")


var_decorar = decorar(saludo)
var_decorar()


"""
 forma 2 decorador
"""
def decorar_forma_2(funcion):
    def nueva_funcion_forma_2():
        print("Antes de usar la funcion saludo")
        funcion()
        print("Despues de usar la funcion saludo")

    return nueva_funcion_forma_2

@decorar_forma_2
def saludo_forma_3():
    print("Hola soy la funcion saludo 2")

saludo_forma_3()