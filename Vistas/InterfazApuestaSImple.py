from tkinter import *
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk, Image
import numpy as np
import matplotlib.pyplot as plt
plt.style.use('ggplot')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from Modelos.Apuesta import Apuesta

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
        texSaldo=StringVar()
        self.enSaldo = Entry(
            marco,
            font="Raleway",
            relief="flat",
            textvariable=texSaldo
        )
        self.enSaldo.grid(
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
        self.enValorApuesta = Entry(
            marco,
            font="Raleway",
            relief="flat"
        )
        self.enValorApuesta.grid(
            row=1,
            column=1,
            padx=3,
            pady=10
        )
        # Probabilidad de ganar
        lbProbabilidadDeGanar = Label(
            marco,
            font="Raleway",
            text="Probabilidad de ganar",
            bg="slateblue3",
            fg="white"
        )
        lbProbabilidadDeGanar.grid(
            row=2,
            column=0,
            padx=3,
            pady=10,
        )
        self.enProbabilidadDeGanar = Entry(
            marco,
            font="Raleway",
            relief="flat"
        )
        self.enProbabilidadDeGanar.grid(
            row=2,
            column=1,
            padx=3,
            pady=10
        )
        # Cuota de apuesta
        texto = StringVar()
        texto.set(f"La cuota de apuesta es: {0.00}")

        self.lbCuotaApuesta = Label(
            marco,
            font=("Raleway", 15),
            textvariable=texto,
            bg="slateblue3",
            fg="white",

        )
        self.lbCuotaApuesta.grid(
            row=0,
            column=2,
            padx=32,
            pady=10
        )

        # Resultado
        textoResultado = StringVar()
        textoResultado.set("")

        self.lbResultado = Label(
            marco,
            font=("Raleway", 15),
            textvariable=textoResultado,
            bg="slateblue3",
            fg="white",

        )
        self.lbResultado.grid(
            row=1,
            column=2,
            padx=32,
            pady=10
        )


        # Botón apostar
        self.btnApostar = tk.Button(
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
        self.btnApostar.grid(
            row=3,
            columnspan=2,
            padx=30
        )

        #Evento Entry
        def calCuota(event):
            try:
                saldo=self.enSaldo.get()
                valorApuesta= self.enValorApuesta.get()
                probGanar=self.enProbabilidadDeGanar.get()
                apuesta = Apuesta(int(saldo),int(valorApuesta),float(probGanar))
                texto.set(f"La cuota de apuesta es: {apuesta.setCuotaDeApuesta()}")
                print("Exito")
            except:
                global popobject
                pop = Toplevel(self.ventana)
                pop.title("My Popup")
                pop.maxsize(width=250,height=150)
                pop.minsize(width=250,height=150)
                pop.config(bg="slateblue1")
                
                global me
                me = PhotoImage(file="Recursos/sign-warning-icon.png")
                pop.configure(
                    bg="slateblue1"
                )
                my_frame = Frame(pop, bg="slateblue1")
                my_frame.pack(pady=5)
                me_pic = Label(my_frame, image=me, borderwidth=0,bg="slateblue1")
                me_pic.pack()
                msg = Label(
                    my_frame,
                    text="Verifica Los datos ingresados",
                    bg="slateblue1",
                    fg="white"
                ).pack()
        self.enProbabilidadDeGanar.bind('<Return>',calCuota)
        #Eventos boton
        def apuesta():
            try:
                saldo = float(self.enSaldo.get())
                valorApuesta = float(self.enValorApuesta.get())
                probGanar = float( self.enProbabilidadDeGanar.get())
                if (saldo <= 0 or valorApuesta > saldo):
                    self.enSaldo.configure(state="disabled")
                    self.enValorApuesta.configure(state="disabled")
                    self.enProbabilidadDeGanar.configure(state="disabled")
                    self.btnApostar.configure(state="disabled")
                    global popobject
                    pop2 = Toplevel(self.ventana)
                    pop2.title("My Popup")
                    pop2.maxsize(width=250, height=150)
                    pop2.minsize(width=250, height=150)
                    pop2.config(bg="slateblue1")

                    global me
                    me = PhotoImage(file="Recursos/sign-warning-icon.png")
                    pop2.configure(
                    bg="slateblue1"
                    )
                    my_frame = Frame(pop2, bg="slateblue1")
                    my_frame.pack(pady=5)
                    me_pic = Label(my_frame, image=me, borderwidth=0, bg="slateblue1")
                    me_pic.pack()

                    def ActiveAndClear():
                        self.enSaldo.configure(state="normal")
                        self.enValorApuesta.configure(state="normal")
                        self.enProbabilidadDeGanar.configure(state="normal")
                        self.enSaldo.delete(0, 'end')
                        self.enValorApuesta.delete(0, 'end')
                        self.enProbabilidadDeGanar.delete(0, 'end')
                        self.btnApostar.configure(state="normal")

                    self.btnSeguirApostando = tk.Button(
                    pop2,
                    text="Seguir apostando",
                    font="Raleway",
                    activebackground="white",
                    bg="dark slate blue",
                    fg="white",
                    bd=5,
                    relief="flat",
                    width=20,
                    command=ActiveAndClear
                )
                    self.btnSeguirApostando.pack()
                    msg = Label(
                    my_frame,
                        text="Te quedaste sin saldo",
                        bg="slateblue1",
                        fg="white"
                    ).pack()
                apta = Apuesta(float(saldo),float(valorApuesta),float(probGanar))
                resultado= apta.apuesta()
                texSaldo.set(f" {round(apta.getSaldoActual(),2)}")

                if(resultado==0):
                    print("Gano")
                    textoResultado.set("Gano")
                else:
                    print("perdio")
                    textoResultado.set("Perdio")
            except:
                global popobject
                pop = Toplevel(self.ventana)
                pop.title("My Popup")
                pop.maxsize(width=250, height=150)
                pop.minsize(width=250, height=150)
                pop.config(bg="slateblue1")
                #global me
                me = PhotoImage(file="Recursos/sign-warning-icon.png")
                pop.configure(
                    bg="slateblue1"
                )
                my_frame = Frame(pop, bg="slateblue1")
                my_frame.pack(pady=5)
                me_pic = Label(my_frame, image=me, borderwidth=0, bg="slateblue1")
                me_pic.pack()
                msg = Label(
                    my_frame,
                    text="Verifica Los datos ingresados",
                    bg="slateblue1",
                    fg="white"
                ).pack()
        self.btnApostar.configure(command=apuesta)
