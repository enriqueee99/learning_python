import mysql.connector
def ins():
    c1=mysql.connector.connect(host="localhost",
                           user="root",
                           passwd="",
                           database="bd1")
    cr=c1.cursor()
    sql="insert into articulos(descripcion,precio) values(%s,%s)"
    des=input("Ingrese la descripcion: ")
    pre=float(input("Ingrese el precio: "))
    datos=(des,pre)
    cr.execute(sql,datos)
    c1.commit()
    c1.close()





def lis():
    c1=mysql.connector.connect(host="localhost",
                            user="root",
                            passwd="",
                            database="bd1")
    cr=c1.cursor()
    cr.execute("select codigo,descripcion,precio from articulos")
    for fila in cr:
        print(fila)
    c1.close()




def bus():
    c1=mysql.connector.connect(host="localhost",
                           user="root",
                           passwd="",
                           database="bd1")
    cr=c1.cursor()
    codigo=int(input("Ingrese el codigo a buscar: "))
    codigo=(codigo,)
    sql="select codigo,descripcion,precio from articulos where codigo = %s"
    cr.execute(sql,codigo)
    for fila in cr:
        print(fila)
        c1.close()

    print("Articulo No Existe")
    c1.close()



def menu():
    op="0"
    while op!="s":
        print("_____________________\n")
        op=input("1) Ingreso de articulos.\n2)Ver todos los articulos.\n3)Buscar un articulo.\n[S] Salir del programa.\nOpcion: ")
        print("_____________________\n")
        if(op=="1"):
            ins()
        else:
            if(op=="2"):
                lis()
            else:
                if(op=="3"):
                    bus()
    return op

diccionario=menu()
