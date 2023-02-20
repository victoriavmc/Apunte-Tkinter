import tkinter
import os

carpetaDeTodosLosArchivos = os.path.dirname(__file__)

carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")
##############################################################################################
tipo = ("Comic Sans MS", 12, "italic")
##############################################################################################
ventana = tkinter.Tk()
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
ventana.geometry("300x210")
ventana.title("Apunte N° 8")

tkinter.Label(ventana, text="Qué te gusta?", font=tipo,
              background="#FF335D").pack(fill=tkinter.X)
##############################################################################################
# Entry (El usuario ingresa el dato.)
##############################################################################################
# Que se hará con los datos ingresados
def usarDatos():
    mensaje = "Te gusta: \n" + datoIngresado.get()
    lblMensaje.config(text=mensaje, font=tipo)

# El nombre del dato ingresado
datoIngresado = tkinter.StringVar()
# El entry
tkinter.Entry(ventana, textvariable=datoIngresado).pack(
    fill=tkinter.X, padx=20, pady=10)

# Etiqueta para mostrar el mensaje:
lblMensaje = tkinter.Label(
    ventana, text="Se vera lo que le gusta. \n ...", font=tipo)
lblMensaje.pack()

# Para que funcione la selección se utiliza un botón:
tkinter.Button(ventana, text="Eso...", bg="#F9EE28", font=tipo,
               command=usarDatos).place(x=125, y=130)

tkinter.Label(ventana, text="~ VictoriaVMC", font=tipo).place(x=165, y=180)

ventana.mainloop()
