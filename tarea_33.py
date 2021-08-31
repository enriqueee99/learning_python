#mostrar dos controles de Radiobutton con las etiquetas "Varon" y "Mujer", cuando se presione un boton actualizar una label con el RadioButton seleccionado:
""""
import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.seleccion=tk.IntVar()
        self.seleccion.set(2)
        self.radio1=tk.Radiobutton(self.ventana1, text="Varon", variable=self.seleccion, value=1)
        self.radio1.grid(column=0, row=0)
        self.radio2=tk.Radiobutton(self.ventana1, text="Mujer", variable=self.seleccion, value=2)
        self.radio2.grid(column=0, row=1)
        self.boton1 = tk.Button(self.ventana1, text="Mostrar seleccionado", command = self.mostrarseleccionado)
        self.boton1.grid(column=0, row=2)
        self.label1=tk.Label(self.ventana1, text="opcion seleccionada")
        self.label1.grid(column=0, row=3)
        self.ventana1.mainloop()

    def mostrarseleccionado(self):
        if self.seleccion.get()==1:
            self.label1.configure(text="opcion seleccionada=Varon")
        if self.seleccion.get()==2:
            self.label1.configure(text="opcion seleccionada=Mujer")
      
        
aplicacion1=Aplicacion()
"""

#disponer dos controles de tipo Entry para el ingreso de enteros. Mediante dos controles RadioButton permitir selecccionar si queremos sumarlos o restarlos. Al presionar un botón mostrar el resultado de la operacion seleccionada.

import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1=tk.Tk()
        self.label1=tk. Label(self.ventana1, text="Ingrese primer valor.")
        self.label1.grid(column=0, row=0)
        self.dato1=tk.StringVar()
        self.entry1=tk.Entry(self.ventana1, width=20, textvariable=self.dato1)
        self.entry1.grid(column=1, row=0)
        self.label2 = tk.Label(self.ventana1, text="Ingrese segundo valor.")
        self.label2.grid(column=0, row=1)
        self.dato2=tk.StringVar()
        self.entry2=tk.Entry(self.ventana1, width=20,textvariable=self.dato2)
        self.entry2.grid(column=1, row=1)
        self.seleccion=tk.IntVar()
        self.radio1=tk.Radiobutton(self.ventana1, text="Sumar", variable=self.seleccion, value=1)
        self.radio1.grid(column=1,row=2)
        self.radio2=tk.Radiobutton(self.ventana1, text="Restar", variable=self.seleccion, value="2")
        self.radio2.grid(column=1, row=3)
        self.boton1=tk.Button(self.ventana1, text="Operar", command=self.operar)
        self.boton1.grid(column=1, row=4)
        self.label3=tk.Label(self.ventana1, text="resultado")
        self.label3.grid(column=1, row=5)
        self.ventana1.mainloop()
    def operar(self):
        if self.seleccion.get()==1:
            suma=int(self.dato1.get())+int(self.dato2.get())
            self.label3.configure(text=suma)
        if self.seleccion.get()==2:
            resta=int(self.dato1.get())-int(self.dato2.get())
            self.label3.configure(text=resta)
aplicacion1 = Aplicacion()



#disponer dos controles de tipo Entry para el ingreso de enteros. Mediante dos controles RadioButton permitir selecccionar si queremos sumarlos o restarlos. Al presionar un botón mostrar el resultado de la operacion seleccionada.
"""
import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.seleccion1=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1, text="Python",
        variable=self.seleccion1)
        self.check1.grid(column=0, row=0)
        self.seleccion2=tk.IntVar()
        self.check2=tk.Checkbutton(self.ventana1,text="C++",
        variable=self.seleccion2)
        self.check2.grid(column=0, row=1)
        self.seleccion3=tk.IntVar()
        self.check3=tk.Checkbutton(self.ventana1,text="Java", variable=self.seleccion3)
        self.check3.grid(column=0, row=2)
        self.boton1=tk.Button(self.ventana1, text="Verificar", command=self.verificar)
        self.boton1.grid(column=0, row=4)
        self.label1=tk.Label(self.ventana1, text="cantidad: ")
        self.label1.grid(column=0, row=5)
        self.ventana1.mainloop()

    def verificar(self):
        cant=0
        if self.seleccion1.get()==1:
            cant+=1
        if self.seleccion2.get()== 1:
            cant+=1
        if self.seleccion3.get()==1:
            cant+=1
        self.label1.configure(text="cantidad: "+ str(cant))

aplicacion1=Aplicacion()
"""

"""
import tkinter as tk
class Aplicacion:
    def __init__(self):
        self.ventana1 = tk.Tk()
        self.seleccion=tk.IntVar()
        self.check1=tk.Checkbutton(self.ventana1, text="Está de acuerdo con los términos y condiciones",
        variable = self.seleccion, command=self.cambiarestado)
        self.check1.grid(column=0, row=0)
        self.boton1=tk.Button(self.ventana1, text="Entrar", state="disabled", command=self.ingresar)
        self.boton1.grid(column=0, row=1)
        self.ventana1.mainloop()

    def cambiarestado(self):
        if self.seleccion.get()==1:
            self.boton1.configure(state="normal")
        if self.seleccion.get()==0:
            self.boton1.configure(state="disabled")
    def ingresar(self):
        self.ventana1.title("Ingresando..")

aplicacion1=Aplicacion()
"""


