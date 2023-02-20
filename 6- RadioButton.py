import tkinter
import os
from PIL import Image, ImageTk
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaIma = os.path.join(carpetaDeTodosLosArchivos,
                          "Carp_Imagenes/Imagenes/6")
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")
##############################################################################################
tipo = ("Comic Sans MS", 12, "italic")
##############################################################################################
ventana = tkinter.Tk()
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
ventana.geometry("500x230")
ventana.title("Apunte N° 6")

etiqueta = "Me regalas una Pepsi por la explicaciones?"
tkinter.Label(ventana, text=etiqueta, font=tipo).pack()

foto = ImageTk.PhotoImage(Image.open(
    os.path.join(carpetaIma, "chi.png")).resize((110, 110)))
tkinter.Label(ventana, image=foto, bg="black").place(x="300", y="50")

tkinter.Label(ventana, text="~ VictoriaVMC", font=tipo).place(x="380", y="200")
##############################################################################################
# Radio Botton (ES TOTALMENTE EXCLUYENTE O SE SELECCIONA UNO U OTRO.)
##############################################################################################
# ? StringVar() = texto
# ? IntVar() = entero
# ? DoubleVar() = flotante
# ? BooleanVar() = booleano

# variable a utilizar
selecciono = tkinter.IntVar()

# Armar la función donde se hacen if según lo que marque


def selecciónPri():
    if selecciono.get() == 1:
        print("Que buena onda, Graz <3")
        mensaje = "Has seleccionado la Primer Opción"
    if selecciono.get() == 2:
        print("Una loba como yo no esta para RATAS como tú!")
        mensaje = "Has seleccionado la Segunda Opción"
    if selecciono.get() == 3:
        print("No hay proxima... Vuelve aquí baboso...")
        mensaje = "Has seleccionado la Tercera Opción"

    lblMensaje.config(text=mensaje, font=tipo)


# Armar los Radiobutton para seleccionar y clasifica después con la función previamente armada
tkinter.Radiobutton(ventana, text="Si", variable=selecciono, value=1, command=selecciónPri, font=tipo).place(x="50", y="50")
tkinter.Radiobutton(ventana, text="No", variable=selecciono, value=2, command=selecciónPri, font=tipo).place(x="50", y="90")
tkinter.Radiobutton(ventana, text="La Prox...", variable=selecciono,value=3, command=selecciónPri, font=tipo).place(x="50", y="130")

# Mostrar el mensaje según lo que se selecciono
lblMensaje = tkinter.Label(ventana)
lblMensaje.place(x="150", y="170")

ventana.mainloop()
