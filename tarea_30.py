

def exis(codigo):
    c1=mysql.connector.connect(host="localhost",
                               user="root",
                               passwd="",
                               database="bd1")
    cr=c1.cursor()
    sql="select codigo from articulos where codigo=%s"
    cr.execute(sql,codigo)
    for fila in cr:
        c1.close()
        return 1
    c1.close()
    return 0



def eli():
    codigo=int(input("Ingrese el codigo a eliminar: "))
    codigo=(codigo,)
    if (exis(codigo)):
        c1=mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="",
                                   database="bd1")
        cr=c1.cursor()
        sql="delete from articulos where codigo=%s"
        cr.execute(sql,codigo)
        c1.commit()
        print("Registro Eliminado!")
        c1.close()
    else:
        print("Registro No Existe")



def act():
    codigo=int(input("Ingrese el codigo del registro a actualizar: "))
    codigo2=codigo
    codigo=(codigo,)
    if(exis(codigo)):
        c1=mysql.connector.connect(host="localhost",
                                   user="root",
                                   passwd="",
                                   database="bd1")
        cr=c1.cursor()
        sql="select codigo,descripcion,precio from articulos where codigo=%s"
        cr.execute(sql,codigo)
        sql="update articulos set descripcion=%s,precio=%s where codigo=%s"
        for fila in cr:
            print(fila)
            des=input("Ingrese la descripcion: ")
            pre=float(input("Ingrese precio: "))
            dat=(des,pre,codigo2)
            print(dat)
            cr.execute(sql,dat)
            c1.commit()
            c1.close()
            return 0
        else:
            print("Articulo No Existe!")


def menu():
    op="0"
    while op!="s":
        print("______________________\n")
        op=input("""1) Ingreso de articulos.
2)Ver todos los articulos.
3)Buscar un articulo.
4)Eliminar un articulo.
5)Actualizar un articulo.
[s]Salir del programa.
Opcion: """)
        print("______________________\n")
        if(op=="1"):
            ins()
        else:
            if(op=="2"):
                lis()
            else:
                if(op=="3"):
                    bus()
                else:
                    if(op=="4"):
                        eli()
                    else:
                        if(op=="5"):
                            act()
    return op
menu()
