from tkinter import *
from tkinter import ttk
from Vistas.InterfazApuestaSImple import InterfazApuestaSimple


class InterfacePrincipal:

    def initAsimples(self):
        win = Toplevel()
        win.geometry('50x50')
        InterfazApuestaSimple.__init__(self,win)

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Bienvenido a la Casa de apuestas")
        self.ventana.geometry("260x150")
        marco = LabelFrame(self.ventana, text="Seleccione su tipo de apuesta")
        marco.grid(row=0, column=0, pady=2, padx=2)
        marco.pack(fill="both",
                   expand=True,
                   side=TOP,
                   anchor=N)
        marco.config(
            width=300,
            height=100,
            relief="sunken",
            bd=5
        )

        ttk.Button(marco, text="Apuestas Simples", command=self.initAsimples).grid(padx=40, pady=10, row=1, column=5,
                                                                                     columnspan=2, sticky=W + E)
        ttk.Button(marco, text="Apuestas automatizadas").grid(padx=40, pady=10, row=2, column=5, columnspan=2,
                                                              sticky=W + E)
