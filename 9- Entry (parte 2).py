from tkinter import *
import os
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")
##############################################################################################
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
ventana = Tk()
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
ventana.geometry("300x210")
ventana.title("Apunte N° 9")
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
# Entry (El usuario ingresa el dato.)
##############################################################################################
# Que se hará con los datos ingresados
def accion():
    n1 = numIngresado.get()
    n2 = numIngresado2.get()
    sumar = n1 + n2
    return resultado.set(sumar)

Label(ventana, text="Cuanto gasto en:", font=tipotexto).place(x=40, y=10)
Label(ventana, font=tipotexto, text="Coca Cola:").place(x=20, y=40)
Label(ventana, font=tipotexto, text="Pepsi:").place(x=20, y=60)
##############################################################################################
# Variables
numIngresado = IntVar()
numIngresado2 = IntVar()
# Para retornar dentro un Entry
resultado = StringVar()
##############################################################################################
Entry(ventana, textvariable=numIngresado).place(x=100, y=40)
Entry(ventana, textvariable=numIngresado2).place(x=100, y=60)
Entry(ventana, textvariable=resultado).place(x=100, y=80)
##############################################################################################
# Para que no ingrese datos dentro del entry donde se vera la respuesta, entonces se utiliza un state=Disable o readonly
Entry(ventana, textvariable=resultado, state="readonly").place(x=150, y=105)
##############################################################################################
Button(ventana, command=accion, text="Sumar",
       font=tipotexto).place(x=60, y=105)
ventana.mainloop()
