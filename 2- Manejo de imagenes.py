import tkinter
from PIL import Image, ImageTk
import os

carpetaDeTodosLosArchivos = os.path.dirname(__file__)

carpetaIma = os.path.join(carpetaDeTodosLosArchivos,
                          "Carp_Imagenes/Imagenes/2")
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")

ventana = tkinter.Tk()
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))

tipo1 = ("Comic Sans MS", 10, "bold")
ventana.title("Apunte N° 2")
ventana.geometry("614x350")
#################################################################################################

etiqueta1 = """ "Así que nuestra vida familiar está siendo calificada... 
Vaya, mira la hora. Ya es 1984." """

foto1 = ImageTk.PhotoImage(Image.open(os.path.join(
    carpetaIma, "daria.png")))

tkinter.Label(ventana, image=foto1, bg="black", bd="2px").pack(side="left")
tkinter.Label(ventana, text=etiqueta1, bg="white",
              fg="red", font=tipo1).place(x="110", y="10")

tipo = ("Comic Sans MS", 10, "italic", "bold")
tkinter.Label(ventana, text="~ VictoriaVMC", font=tipo).place(x="490", y="320")

# COMPOUN QUEDA MEDIO DE LA IMAGEN; PERO NMG.
# Import tkinter as tk
# tkinter.Label(ventana, text=etiqueta1, image=foto1,bg="black", bd="4px", compound=tk.CENTER).pack()
ventana.mainloop()
