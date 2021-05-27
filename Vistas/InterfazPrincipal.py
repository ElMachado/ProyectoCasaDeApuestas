from tkinter import *
import tkinter as tk
from PIL import ImageTk, Image
from Vistas.InterfazApuestaSImple import InterfazApuestaSimple


class InterfacePrincipal:

    def initAsimples(self):
        win = Toplevel()
        InterfazApuestaSimple.__init__(self, win)

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Bienvenido a la Casa de apuestas")
        self.ventana.configure(bg="slateblue1")
        self.ventana.minsize(width=1500,height=800)
        self.ventana.maxsize(width=1500,height=800)


        canvas = tk.Canvas(ventana, width=800, height=500)
        canvas.grid(columnspan=4)
        # logo
        logo = Image.open('Recursos/Auditoria-juego-de-apuestas-online.jpg')
        logo = ImageTk.PhotoImage(logo)
        logo_label = tk.Label(image=logo)
        logo_label.image = logo
        logo_label.grid(column=2, row=0, sticky=W + E + N + S)

        marco = LabelFrame(
            self.ventana,
            text="Seleccione su tipo de apuesta",
            width=100,
            font="Raleway",
            relief="flat",
            bg="slateblue1",
            fg="white"
        )
        marco.grid(row=0, column=0, pady=0, padx=0, ipadx=0, ipady=335)

        btnApuestaSimple = tk.Button(marco, text="Apuesta Simple")
        btnApuestaSimple.config(
            font="Raleway",
            activebackground="white",
            bg="dark slate blue",
            fg="white",
            bd=5,
            relief="flat",
            width=20,
            command=self.initAsimples
        )
        btnApuestaSimple.grid(padx=5, pady=5, row=2, columnspan=2, sticky=W+E)
        btnApuestaAutomatizada = tk.Button(marco)
        btnApuestaAutomatizada.configure(
            text="Apuestas automatizadas",
            font="Raleway",
            activebackground="white",
            bg="dark slate blue",
            fg="white",
            bd=5,
            relief="flat",
            width=20
        )
        btnApuestaAutomatizada.grid(padx=5, pady=5, row=3, columnspan=2, sticky=W+E)
