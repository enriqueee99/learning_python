# from io import open
# op = "C:/Users/Anthony/OneDrive/Escritorio/python/sistemas_de_archivos.py"
# f = open('cuarto.txt', 'w', encoding='utf-8')
# f.close()


# #anexar texto a un archivo preexistente
# op = "C:/Users/Anthony/OneDrive/Escritorio/python/cuarto.txt"
# f = open(op, 'a+', encoding='utf-8')
# f.write('\n' + 'hola mundo')
# f.close()


# op = "C:/Users/Anthony/OneDrive/Escritorio/python/cuarto.txt"
# f = open(op, 'a+', encoding='utf-8')
# f.write('\n' + 'hola mundo')
# f.close()
# f = open(op, 'r+', encoding='utf-8')
# leer = f.read()
# print(leer)
# f.close()


#permite sacar la primera
def file_line(fi):
f = open(fi, "r", encoding='utf-8')
lista =[""]
global c
c = 0

for x in f:
    acu = ""
    for p in x:
        if p != "":
            acu : acu + p
        else:
            break
    c += 1

    lista.append(acu)
f.close()
return lista

op="C:/Users/Anthony/OneDrive/Escritorio/python/cuarto.txt"
j = file_line(op)
print(j)



# #eliminar
# from os import remove
# op="C:/Users/Anthony/OneDrive/Escritorio/python/cuarto.txt"
# remove(op)

# from os import rmdir
# rmdir('carpeta vacia')

# from shutil import rmtree
# rmtree('carpeta')










