archivo = open("archivos\\ejemplo.txt", mode='w', encoding='utf-8')
archivo.write("Hola mundo Ñ úúuu\n")
archivo.close()


archivo = open("archivos\\nota.txt", mode='r', encoding='utf-8')
for linea in archivo.readlines():
    print(linea,end='')
archivo.close()


nueva_lineas = []
with open("archivos\\nota.txt", mode='r', encoding='utf-8') as archivo:
    lineas = archivo.readlines()
    nueva_lineas = ["NOMBRE:" + l.upper() for l in lineas]

with open("archivos\\nota_final.txt", mode='w', encoding='utf-8') as salida:
    salida.writelines(nueva_lineas)


"""
Leer un archivo de texto llamado "numeros.txt" que contiene una serie de números 
enteros separados por espacios, y calcular su suma.
"""
with open("archivos\\numeros.txt", mode='r', encoding='utf-8') as archivo_leido:
    contenido = archivo_leido.read()
    list_numeros_str = contenido.split()
    list_numeros = [int(numero) for numero in list_numeros_str]
    print(f"La suma de los numeros son {sum(list_numeros)}")


"""
Crear un archivo de texto llamado "nombres.txt" y escribir 
en él los nombres de cinco personas, cada uno en una línea.
"""
with open("archivos\\nombres.txt", mode="w", encoding='utf-8') as f:
    f.write("Ana Nuñez\n")
    f.write("Luis\n")
    f.write("Pedro\n")
    f.write("María\n")
    f.write("Carlos\n")

"""
Copiar el contenido de un archivo binario llamado "imagen.jpg" 
a otro archivo llamado "copia.jpg"
"""
imagen = None

with open("archivos\\imagen.jpg", mode='rb') as archivo_binario:
    imagen = archivo_binario.read()

with open("archivos\\copia.jpg", mode='wb') as archivo_binario_copia:
    archivo_binario_copia.write(imagen)