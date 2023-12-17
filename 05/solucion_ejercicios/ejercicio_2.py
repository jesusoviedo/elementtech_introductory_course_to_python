"""
Crea un diccionario con las iniciales y los nombres completos de los siguientes países, usando una comprensión de diccionario

listado:
Argentina
Brasil
Chile
Ecuador
Paraguay
Mexico
"""

paises = ["Argentina", "Brasil", "Chile", "Ecuador", "Paraguay", "Mexico", "Peru"]

paises_dic = { pais[0:2].lower() : pais.upper() for pais in paises}

print(paises_dic)