import tkinter
import os
from PIL import Image, ImageTk
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaIma = os.path.join(carpetaDeTodosLosArchivos,
                          "Carp_Imagenes/Imagenes")
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")
##############################################################################################
tipo = ("Comic Sans MS", 12, "italic")
##############################################################################################
ventana = tkinter.Tk()
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))

ventana.title("Plantilla")

jaja = ImageTk.PhotoImage(Image.open(os.path.join(carpetaIma, "dame5.png")))
tkinter.Label(ventana, image=jaja).pack()

tkinter.Label(ventana, text="~ VictoriaVMC", font=tipo).pack(side="bottom")

ventana.mainloop()
