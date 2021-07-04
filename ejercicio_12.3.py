lista = []

for x in range(5):
    num = input('Ingrese un numero: ')
    lista.append(num)

print(f'El mayor de la lista es: ',max(lista))
print(f'El numero {num} se repite {lista.count(num)} veces')