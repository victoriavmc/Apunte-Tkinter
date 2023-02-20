import tkinter
import os

carpetaDeTodosLosArchivos = os.path.dirname(__file__)

carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")

ventana = tkinter.Tk()
ventana.iconbitmap(os.path.join(carpetaLogo, "umaru.ico"))
ventana.title("Apunte N°4")
ventana.geometry("600x200")

tipo = ("Comic Sans MS", 10, "italic", "bold")
tkinter.Label(ventana, text="~ VictoriaVMC", font=tipo).place(x="490", y="170")
#################################################################################################
#                         Botón Básico, se toca el botón y se acomoda solo.
#################################################################################################


def primerBoton():
    tkinter.Label(ventana, text="أعطني بيبسي").pack(side="right")
    print("Traduci si desconfías...")


tkinter.Button(ventana, text="Soy un Boton", fg="red",
               command=primerBoton).place(x="10", y="20")
#################################################################################################
#                         Botón Básico, se toca el botón pero se queda fijo el texto al tocar.
#################################################################################################

texto = """ "Solo por que seas "Novato" no significa que tengas que pensar como uno." """


def segundoBoton():
    tkinter.Label(ventana, text=texto).place(x="180", y="150")
    print("No que sofisticado? \n Quiero cambiar las cosas Cerebro!!")


tkinter.Button(ventana, text="Soy un Botón más sofisticado", fg="blue",
               command=segundoBoton).place(x="10", y="150")

ventana.mainloop()
