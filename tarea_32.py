#interfaces
"""
import tkinter as tk

class Aplication:
    
        ventana1 = tk.Tk()
        ventana1.title('Hola Dallerlyn')
        ventana1.mainloop()
"""



#interfaces graficas ejemplo 1
"""
import tkinter as tk
class Aplicacion:
        def __init__(self):
                self.ventana1 = tk.Tk()
                self.ventana1.title('Hola Dallerlyn')
                self.ventana1.mainloop()
aplicacion1 = Aplicacion()
"""


#tkinter: controles y label - ejemplo 1
#mostrar una ventana y en su interior dos botones y un label. El label muestra inicialmente el valor 1. Cada uno de los botones permiten incrementar o decrementar en uno el contenido del label

"""
import tkinter as tk
class Aplicacion:
        def __init__(self):
                self.valor=1
                self.ventana1=tk.Tk()
                #creamos el objeto
                self.ventana1.title("Controles Button y Label")
                self.label1=tk.Label(self.ventana1, text=self.valor) 
                #creamos el objeto
                self.label1.grid(column=0, row=0)
                self.label1.configure(foreground="red")

                self.boton1=tk.Button(self.ventana1, text="Incrementar",
        command=self.incrementar)
                #creamos el objeto
                self.boton1.grid(column=0, row=1)

                self.boton2=tk.Button(self.ventana1, text="Decrementar",
        command=self.decrementar)
                #creamos el objeto
                self.boton2.grid(column=0, row=2)

                self.ventana1.mainloop()

        def incrementar(self):
                self.valor=self.valor+1
                self.label1.config(text=self.valor)

        def decrementar(self):
                self.valor=self.valor-1
                self.label1.config(text=self.valor)
aplicacion1 = Aplicacion()
"""




#Tkinter: control entrey - ejemplo 1
#Confeccionar una aplicación que permite ingresar un numero entero por teclado y al presionar un boton muestre dicho valor al cuadrado en un label

import tkinter as tk

class Aplicacion:
        def __init__(self):
                self.ventana1 = tk.Tk()
                self.label1 = tk.Label(self.ventana1, text='Ingrese un número: ')
                self.label1.grid(column=0, row=0)
                self.dato = tk.StringVar()
                self.entry1 = tk.Entry(self.ventana1, width=10, textvariable=self.dato)
                self.entry1.grid(column=0, row=1)
                self.boton1 = tk.Button(self.ventana1, text='Calcular cuadrado',
        command = self.calcularcuadrado)
                self.boton1.grid(column=0, row=2)
                self.label2 = tk.Label(self.ventana1, text='resultado')
                self.label2.grid(column=0, row=3)
                self.ventana1.mainloop()

        def calcularcuadrado(self):
                valor = int(self.dato.get())
                cuadrado = valor * valor
                self.label2.configure(text='cuadrado')
        
aplicacion1 = Aplicacion()
