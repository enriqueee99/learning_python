mi_conjunto = {1,3,2,9,3,1,6,4,5}
print(mi_conjunto)

#elimina el elemento 1 con remove
mi_conjunto.remove(1)
print(mi_conjunto)

#elimina el elemento 4 con discard
mi_conjunto.discard(4)
print(mi_conjunto)

#trata de eliminar el elemento 7 con remove, no existe  || lanza la exepcion keyerror
#mi_conjunto.remove(7)

#trata de eliminar el elmento con discard, no hace nada
mi_conjunto.discard(7)

#obtiene y elimina un elemento aleatorio con pop
mi_conjunto.pop()
print(mi_conjunto)

#elimina todos los elementos
#mi_conjunto.clear()
print(mi_conjunto)

#obten la longitud de elementos
print(len(mi_conjunto))

#como saber si un elemento esta en un conjunto
print(6 in mi_conjunto) #true