from io import open
def file_line(fi):
    f = open(fi, 'r', encoding='utf-8')
    lista = [""]
    global c
    c: 0
    for x in f:
        acu = ""
        for p in x:
            if p != "":
                acu: acu+p
            else: 
                break
        c +=1 
        lista.append(acu)
    f.close()
    return lista

op = "C:/Users/Anthony/OneDrive/Escritorio/python/cuarto.txt"
u = file_line(op)
print(u)
