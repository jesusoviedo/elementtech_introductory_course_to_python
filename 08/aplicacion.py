import matematicas
#import mi_modulo as mp
import logica.sublogica.mi_modulo as mp
#import logica.calculo_salario as cs
from logica.calculo_salario import calcular_salario_2 as cs
from math import sqrt as raiz

import io

area = matematicas.area_circulo(15)
suma = mp.suma(4, 5)
resta = mp.resta(17, 5)



print(area, suma, resta)


empleado = {
    "salario_base": 1000,
    "horas_extra": 20,
    "tarifa_hora_extra": 200,
}

salario = cs(empleado)
print(salario)

print(raiz(25))