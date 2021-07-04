empleados = []
dias_faltantes = []
dias_empleados = []

for x in range(3):
    nombres = input('Nombre del empleado: ')
    empleados.append(nombres)
    dias = int(input('Cuantos dias faltó?: '))
    for x in range(dias):
        dia = int(input('Qué dias faltó?: '))
        dias_empleados.append(dia)



dias_faltantes.append(dias_empleados)
    
    # dias = int(input('Qué dias faltó?: '))
    # dias_faltantes.append(dias)

print(empleados)
print(dias_faltantes)