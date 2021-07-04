lista_uno = []
lista_dos = []
lista_tres = []

for x in range(4):
    num = int(input('Fila 1: Ingrese 4 numeros enteros: '))
    lista_uno.append(num)
    lista_tres.append(num)

for x in range(4):
    num = int(input('Fila 2: Ingrese otros 4 numeros enteros: '))
    lista_dos.append(num)
    lista_tres[x] = lista_tres[x] + lista_dos[x]

print(lista_uno)
print(lista_dos)
print(lista_tres)