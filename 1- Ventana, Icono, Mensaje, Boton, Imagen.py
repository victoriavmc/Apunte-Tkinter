import tkinter
##############################################################################################
#! IMPORTO OS PARA PONER LAS IMÁGENES.
import os
from PIL import Image, ImageTk
#! --- Creo directorios ---
#! Primero de la Carpeta principal (están todos los documentos/imágenes/carpetas)
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
#! Saco la carpeta de imágenes o la que necesite
carpetaIma = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Imagenes/1")
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")
##############################################################################################
# defino tipo de letra que quiero que tenga el texto
tipo = ("Comic Sans MS", 12, "italic")
tipoBoton = ("Comic Sans MS", 12, "bold")
##############################################################################################
# * Crear la ventana.
ventana = tkinter.Tk()

# * Definir tamaño a la ventana.
ventana.geometry("700x230")

# * Logo en la ventana.
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))

# * Titulo de la ventana.
ventana.title("Apunte N° 1")
##############################################################################################
#! Mensaje de texto en varias lineas.
mensaje = """Este modelo es de:
Un Mensaje de texto en varias lineas.
"""
#! LABEL DEFINE DONDE SE MOSTRARA."el contenedor donde estará, y lo que se mostrará."
#! el .pack() ubica automáticamente el label.
tkinter.Label(ventana, text=mensaje, font=tipo,justify=tkinter.CENTER).pack(anchor="nw", padx="20", pady="10")

#! También el mensaje de texto puede presentarse en el Label (pero queda poco estético)
#! .place se define con x e y donde se ubicara el label.
tkinter.Label(ventana, text="~ VictoriaVMC \n", font=tipo).place(x="550", y="200")
##############################################################################################
# ? Poner imagen.
# Cargar la imagen. De donde sale el archivo.
foto = ImageTk.PhotoImage(Image.open(os.path.join(carpetaIma, "umaru_Pepsi.png")).resize((325, 180)))

# Mostrar
tkinter.Label(ventana, image=foto, bg="black", bd="4px").place(x="330", y="10")
##############################################################################################
# * Botón con función
def funcionAnda():
    texto = ("""Funciona Lic.
             Mire la consola!""")
    print(f"Siii... Funcionaaaaa lesto.. Quiero una pepsi...")
    tkinter.Label(ventana, text=texto, font=tipo).place(x=120, y=80)

def funcionFinalizar():
    ventana.destroy()

texto = (""" <- Realiza un:
         Cierre Automático.""")
tkinter.Label(ventana, text=texto, font=tipo).place(x=100, y=150)
buttonVerificar = tkinter.Button(
    ventana, text="Mira", fg="Green", font=tipoBoton, command=funcionAnda).place(x=60, y=80)

buttonSalir = tkinter.Button(ventana, text="Salir", fg="Red",
                             font=tipoBoton, command=funcionFinalizar).place(x=60, y=150)
# ! Abrir la ventana. ULTIMO
ventana.mainloop()
