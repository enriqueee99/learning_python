empleados = []
faltas = []

for x in range(3):
    nombres = input('Nombre del empleado: ')
    empleados.append(nombres)
    dias = int(input('Cuantos dias faltó?: '))
    faltas.append([])
    for y in range(dias):
        dia = int(input('Qué dias faltó?: '))
        faltas[x].append(dia)

print('Empleados y los dias que faltaron')       
for x in range(3):
    print(empleados[x])
    for y in range(len(faltas[x])):
        print(faltas[x][y])

print('Empleados y la cantidad de inasistencias')
for x in range(3):
   print(f'El empleado {empleados[x]} faltó {len(faltas[x])} dias')

print('Empleado que faltó menos')
menos = len(faltas[0])
for x in range(1,3):
    if len(faltas[x]) < menos:
        menos = len(faltas[x])

for x in range(3):
    if len(faltas[x]) == menos:
        print(empleados[x])