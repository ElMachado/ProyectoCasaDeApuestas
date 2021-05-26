from tkinter import *
from tkinter import ttk

class InterfazApuestaSimple:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("hola Mundo")
        self.ventana.geometry("1000x600")

        marco=LabelFrame(self.ventana,text="Apuesta")
        marco.grid(row=0,column=0,columnspan=3,pady=20)
        marco.configure(width=1000,height=600)
        Label(marco, text="Saldo").grid(row=0, column=0)
        Entry(marco).grid(row=0, column=1)
        #Valor de la apuesta
        Label(marco,text="Valor de la apuesta").grid(row=1,column=0)
        Entry(marco).grid(row=1,column=1)
        #Valor de apuesta
        Label(marco, text="Probabilidad de ganar").grid(row=2, column=0)
        Entry(marco).grid(row=2, column=1)
        #Cuota de apuesta
        cuota=0.051
        texto=f"La cuota de apuesta es:{cuota} "
        Label(marco, text=texto).grid(row=1, column=3)
        #Botón apostar
        ttk.Button(self.ventana,text="Apostar").grid(row=2,columnspan=2)