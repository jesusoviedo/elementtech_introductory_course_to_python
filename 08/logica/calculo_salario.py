
def calcular_salario(dict_empleado):
    salario_base = dict_empleado["salario_base"]
    horas_extra = dict_empleado["horas_extra"]
    salario_extra = horas_extra * dict_empleado["tarifa_hora_extra"]
    return salario_base + salario_extra

def calcular_salario_2(dict_empleado):
    salario_base = dict_empleado["salario_base"]
    horas_extra = dict_empleado["horas_extra"]
    salario_extra = horas_extra * dict_empleado["tarifa_hora_extra"] * 2
    return salario_base + salario_extra