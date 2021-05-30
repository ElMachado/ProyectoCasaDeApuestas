import tkinter as tk
from tkinter import *

import matplotlib.pyplot as plt
import numpy as np

from Modelos.AptAuto import AptAuto

plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


# noinspection SpellCheckingInspection
class InterfazApuestaAutomatizada:

    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.title("Apuestas simples")
        self.ventana.configure(bg="slateblue1")
        self.ventana.minsize(width=1000, height=800)
        self.ventana.maxsize(width=1000, height=800)

        # Marco
        self.marco = LabelFrame(
            ventana,
            text="Apuestas en modo automático",
            width=900,
            height=750,
            font=("Raleway", 30),
            relief="flat",
            bg="slateblue3",
            fg="white",
            labelanchor="n"
        )
        self.marco.place(
            x=50,
            y=25
        )
        lb = Label(
            self.marco,
            font="Raleway",
            text="Número de apuestas",
            bg="slateblue3",
            fg="white"
        )
        lb.place(
            relx=0.25,
            rely=0.01
        )
        self.nSimulaciones = Entry(
            self.marco,
            font="Raleway",
            relief="flat",
            width=10
        )
        self.nSimulaciones.place(
            relx=0.45,
            rely=0.01
        )

        frameContenedor = Frame(
            self.marco,
            width=300,
            height=300,
            bg="slateblue4",
            relief="sunken",
            bd=2.5,
            padx=0,
            pady=0
        )
        frameContenedor.place(
            relx=0.20,
            rely=0.08

        )
        frameizquierdo = Frame(
            frameContenedor,
            width=100,
            height=50,
            bg="slateblue4",
            relief="sunken",
            bd=2.5,
            padx=10,
            pady=0,
        )
        frameizquierdo.grid(
            row=3,
            column=4,
            ipady=50,
            ipadx=70,
            sticky=E

        )
        Label(
            frameizquierdo,
            font=("Raleway", 15),
            text="Probabilidad de ganar",
            bg="slateblue4",
            fg="white",
            pady=5
        ).place(
            relx=0.001,
            rely=0.10
        )
        # Variables selectoras
        rBtnsIzquierda = IntVar()

        r1 = Radiobutton(
            frameizquierdo,
            borderwidth=0,
            text="Estrategia conservadora",
            activebackground="slateblue4",
            highlightbackground="slateblue4",
            # highlightcolor="slateblue4",
            activeforeground="white",
            selectcolor="slateblue4",
            bg="slateblue4",
            fg="white",
            bd=0,
            pady=10,
            value=0,
            indicatoron=1,
            variable=rBtnsIzquierda
        )
        r1.place(
            relx=0.07,
            rely=0.40
        )
        r2 = Radiobutton(
            frameizquierdo,
            text="Estrategia arriesgada",
            activebackground="slateblue4",
            highlightbackground="slateblue4",
            highlightcolor="slateblue4",
            activeforeground="white",
            selectcolor="slateblue4",
            bg="slateblue4",
            fg="white",
            bd=0,
            pady=10,
            value=1,
            indicatoron=1,
            variable=rBtnsIzquierda

        )
        r2.place(
            relx=0.07,
            rely=0.60
        )

        frameDerecho = Frame(
            frameContenedor,
            width=100,
            height=50,
            relief="sunken",
            bg="slateblue4",
            bd=2.5,
            padx=10,
            pady=0,
        )
        frameDerecho.grid(
            row=3,
            column=6,
            ipady=50,
            ipadx=70,
            sticky=N + E + S + W + NE + NW + SE + SW
        )
        Label(
            frameDerecho,
            font=("Raleway", 15),
            text="Valor Apostado",
            bg="slateblue4",
            fg="white",
            pady=5
        ).place(
            relx=0.04,
            rely=0.10
        )
        # Variables selectoras
        rBtnsDerecha = IntVar()

        r3 = Radiobutton(
            frameDerecho,
            text="Estrategia economizadora",
            activebackground="slateblue4",
            highlightbackground="slateblue4",
            # highlightcolor="slateblue4",
            activeforeground="white",
            selectcolor="slateblue4",
            bg="slateblue4",
            fg="white",
            bd=0,
            pady=10,
            value=0,
            indicatoron=1,
            variable=rBtnsDerecha,
        )
        r3.place(
            relx=0.05,
            rely=0.40
        )
        r4 = Radiobutton(
            frameDerecho,
            text="Estrategia derrochadora",
            activebackground="slateblue4",
            highlightbackground="slateblue4",
            # highlightcolor="slateblue4",
            activeforeground="white",
            selectcolor="slateblue4",
            bg="slateblue4",
            fg="white",
            bd=0,
            pady=10,
            indicatoron=1,
            value=1,
            variable=rBtnsDerecha,
        )
        r4.place(
            relx=0.05,
            rely=0.60
        )
        # Frame gráfica
        grafica_frame = tk.Frame(
            self.ventana,
            bg='slateblue4',
            bd=1.5,
            width=820,
            height=400,
            padx=0,
            pady=0
        )
        grafica_frame.place(
            anchor=NW,
            x=100,
            y=360,
            height=400,
            width=800
        )

        # Gráfica
        figure = plt.Figure(figsize=(100, 100), dpi=80)
        ax = figure.add_subplot(111)
        ax.set_title('$Apuestas hechas$')
        ax.grid(True), ax.set_xlabel('$Número de apuestas$'), ax.set_ylabel('$Saldo actual$')
        line = FigureCanvasTkAgg(figure, grafica_frame)
        line.get_tk_widget().pack(side=tk.LEFT, fill=tk.BOTH, expand=10000)

        self.historicoSaldo = np.array([])
        self.index = np.array([])

        def apuesta():
            historicoSaldo = np.array([])
            index = np.array([])
            AptAuto.setSaldoInicial()
            for i in range(int(self.nSimulaciones.get())):
                AptAuto.apuesta(rBtnsIzquierda,rBtnsDerecha)
                data = AptAuto.saldoActual
                index = np.append(index, int(i))
                historicoSaldo = np.append(historicoSaldo, data)
                # Graficación de la linea.
                # ax.clear()
                ax.plot(index,historicoSaldo)
                ax.grid(True)
                line.draw()
                print("el saldo actual es:", AptAuto.saldoActual)
                if (AptAuto.saldoActual <= 0):
                    break;
        # Botón apuestas
        self.btnRealizarApuestas = Button(
            self.marco,
            text="Apostar",
            font="Raleway",
            activebackground="white",
            bg="dark slate blue",
            fg="white",
            bd=0,
            relief="flat",
            width=20,
            command=apuesta
        ).place(
            x=300,
            y=234
        )
