from tkinter import *
import tkinter as tk
from tkinter import ttk


class InterfazApuestaSimple:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Apuestas simples")
        self.ventana.configure(bg="slateblue1")
        self.ventana.minsize(width=1000, height=600)
        self.ventana.maxsize(width=1000, height=600)
        # Marco
        marco = LabelFrame(
            self.ventana,
            text="Apuesta",
            width=600,
            height=200,
            font=("Raleway", 30),
            relief="flat",
            bg="slateblue3",
            fg="white",
            labelanchor="n",
            padx=0,
        )
        marco.grid(
            row=0,
            column=0,
            columnspan=3,
            ipady=10,
            ipadx=100,
            padx=45,
            pady=20,
            sticky=N + W + E + S
        )
        # Saldo
        lbSaldo = Label(
            marco,
            text="Saldo",
            font="Raleway",
            bg="slateblue3",
            fg="white"
        )
        lbSaldo.grid(
            row=0,
            column=0,
            padx=3,
            pady=10,
        )
        enSaldo = Entry(
            marco,
            font="Raleway",
            relief="flat"
        )
        enSaldo.grid(
            row=0,
            column=1,
            padx=3,
            pady=10,
        )
        # Valor de la apuesta

        lbValorApuesta = Label(
            marco,
            font="Raleway",
            text="Valor de la apuesta",
            bg="slateblue3",
            fg="white"
        )
        lbValorApuesta.grid(
            row=1,
            column=0,
            padx=3,
            pady=10,
        )
        enValorApuesta = Entry(
            marco,
            font="Raleway",
            relief="flat"
        )
        enValorApuesta.grid(
            row=1,
            column=1,
            padx=3,
            pady=10
        )
        # Probabilidad de ganar
        lbProbabilidadDeGanar = Label(
            marco,
            font="Raleway",
            text="Valor de la apuesta",
            bg="slateblue3",
            fg="white"
        )
        lbProbabilidadDeGanar.grid(
            row=2,
            column=0,
            padx=3,
            pady=10,
        )
        enProbabilidadDeGanar = Entry(
            marco,
            font="Raleway",
            relief="flat"
        )
        enProbabilidadDeGanar.grid(
            row=2,
            column=1,
            padx=3,
            pady=10
        )
        # Cuota de apuesta
        cuota = 0.051
        texto = f"La cuota de apuesta es:{cuota}"

        lbCuotaApuesta = Label(
            marco,
            font=("Raleway", 15),
            text=texto,
            bg="slateblue3",
            fg="white",

        )
        lbCuotaApuesta.grid(
            row=0,
            column=2,
            padx=32,
            pady=10
        )

        # Botón apostar
        btnApostar = tk.Button(
            self.ventana,
            text="Apostar",
            font="Raleway",
            activebackground="white",
            bg="dark slate blue",
            fg="white",
            bd=5,
            relief="flat",
            width=20
        )
        btnApostar.grid(
            row=3,
            columnspan=2,
            padx=30
        )
