from tkinter import *
from Vistas.InterfazPrincipal import InterfacePrincipal
from PIL import ImageTk
from PIL import Image



if __name__ == '__main__':
    ventana=Tk()
    ventana.call('wm', 'iconphoto', ventana,PhotoImage(file='Recursos/icon.png'))
    aplicacion=InterfacePrincipal(ventana)
    ventana.mainloop()