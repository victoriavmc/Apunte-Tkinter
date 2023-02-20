import tkinter
import os

carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")

#################################################################################################
#                         Botón Cambia el texto al tocarlo.
#################################################################################################
class Prueba:
    def __init__(self):
        self.ventana = tkinter.Tk()
        self.ventana.title("Apunte N° 5")
        self.ventana.geometry("300x80")
        self.ventana.iconbitmap(os.path.join(carpetaLogo, "umaru.ico"))
        # Se crea una variable tipo StringVar para cambiar el texto del widget
        self.texto = tkinter.StringVar()
        # Le daremos un valor inicial
        self.texto.set("Primer valor que tengo...\n Avanzando Pinky...")
        tkinter.Label(self.ventana, textvariable=self.texto).pack()
        # Creamos el botón
        tkinter.Button(self.ventana, text="-> Cambia el texto <-",
                       command=self.cambioTexto).pack()
        tipo = ("Comic Sans MS", 10, "italic", "bold")
        tkinter.Label(self.ventana, text="~ VictoriaVMC", font=tipo).pack(side="right")
        self.ventana.mainloop()

    def cambioTexto(self):
        self.texto.set("Eso es todo... \n Cierre automático.")
        self.ventana.after(1000, lambda: self.ventana.destroy())


app = Prueba()
