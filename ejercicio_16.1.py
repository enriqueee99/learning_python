personas = {}
for x in range(3):
    numero = int(input('Ingrese el numero de la persona: '))
    nombre = input('Ingrese el nombre de la persona: ')
    personas[numero] = nombre

print('Listado completo de las personas: ')
for numero in personas:
    print(numero, personas[numero])

num_consulta = int(input('¿Qué numero desea consultar?: '))
if num_consulta in personas:
    print(f'La persona es: ', personas[numero] )
else:
    print('La persona no existe.')