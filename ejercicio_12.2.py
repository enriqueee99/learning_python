nombres = []
for x in range(3):
    nom = input('Ingrese un nombre: ')
    nombres.append(nom)
nombres_ordenados = sorted(nombres, reverse=True)
print(f'La persona menor en orden alfabetico es: ',nombres_ordenados.pop())
