import tkinter
import os

carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaIma = os.path.join(carpetaDeTodosLosArchivos,
                          "Carp_Imagenes/Imagenes/7")
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")
##############################################################################################
tipo = ("Comic Sans MS", 12, "italic")
##############################################################################################
ventana = tkinter.Tk()
ventana.geometry("300x220")
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))

ventana.title("Apunte N° 7")

tkinter.Label(ventana, text="~ VictoriaVMC", font=tipo).pack(side="bottom")
##############################################################################################
# CheckButton (Puedes seleccionar uno o todos.)
##############################################################################################

tkinter.Label(ventana, text="De que hablo mucho?", font=tipo).pack()


def opciones():
    mensaje = ""

    if primeraOpcion.get() == 1:
        mensaje = mensaje + " Pepsi - "
    if segundaOpcion.get() == 1:
        mensaje = mensaje+" Coca Cola - "
    if terceraOpcion.get() == 1:
        mensaje = mensaje+" Agua - "

    if primeraOpcion.get() == 1 and segundaOpcion.get() == 1 and terceraOpcion.get() == 1:
        mensaje = "Haz seleccionado las tres opciones!"
    else:
        mensaje = "Haz marcado:" + mensaje
    lblMensaje.config(text=mensaje, font=tipo)


# Variables para conocer el estado de los checkbox
primeraOpcion = tkinter.IntVar()
segundaOpcion = tkinter.IntVar()
terceraOpcion = tkinter.IntVar()

# CREAR CHECKBOX
tkinter.Checkbutton(
    ventana, text="PEPSI", variable=primeraOpcion).place(x="10", y="35")
tkinter.Checkbutton(
    ventana, text="COCA COLA", variable=segundaOpcion).place(x="10", y="75")
tkinter.Checkbutton(
    ventana, text="AWUA de UwU", variable=terceraOpcion).place(x="10", y="115")

# Para que funcione la selección se utiliza un botón:
tkinter.Button(ventana, text="Enviar",
               command=opciones).place(x="110", y="140")

# Etiqueta para mostrar el mensaje que esta dentro de la función anterior.
lblMensaje = tkinter.Label(ventana)
lblMensaje.place(x="10", y="170")

ventana.mainloop()
