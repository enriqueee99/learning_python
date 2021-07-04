sueldo_empleados = []
cantidad = int(input('Cuantos empleados tiene la empresa?: '))

for x in range(cantidad):
    sueldo_individual = float(input('Ingrese el sueldo del empleado: '))
    sueldo_empleados.append(sueldo_individual)

print(sorted(sueldo_empleados))