# from tkinter import *
# root = Tk()
# root.title("Ventana de pruebas ")
# root.geometry("1000x600")
# frame = Frame(root)
# frame.pack(
#     fill="both",
#     expand=True,
#     side=LEFT,
#     anchor=N
# )
# frame.config(
#     width=1000,
#     height=600,
#     cursor="pirate",
#     bg="gray",
#     relief="sunken",
#     bd=1object0
# )
# root.mainloop()
from tkinter import *
from Vistas.InterfazPrincipal import InterfacePrincipal

if __name__ == '__main__':
    ventana=Tk()
    aplicacion=InterfacePrincipal(ventana)
    ventana.mainloop()