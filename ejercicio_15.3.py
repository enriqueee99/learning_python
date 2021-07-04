lista = []
cantidad = 1

for x in range(50):
    lista.append([])
    valor = 1
    for y in range(cantidad):
        lista[x].append(valor)
        valor = valor + 1
    cantidad = cantidad + 1

print(lista)