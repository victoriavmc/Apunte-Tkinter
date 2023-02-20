import tkinter
import os

carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")

ventana = tkinter.Tk()
ventana.iconbitmap(os.path.join(carpetaLogo, "umaru.ico"))
ventana.title("Apunte N°3")
#################################################################################################
etiqueta = "Este es un texto hipermegaultrahichermegalargo pero se va a separar. Permite colocar texto multilinea, pero no definimos por el cambio de linea."

# MESSAGE (se adapta a la ventana tal cual)
tkinter.Message(ventana, text=etiqueta).pack()

# INDICAMOS EL ANCHO que deseamos, y vemos como se ajusta
tkinter.Message(ventana, text=etiqueta, width=400).pack()

# Cambiamos el estilo. (Para ello debemos poner nombre, es decir hacer variable:)
texto = "Mamá resiente tener que trabajar tanto, y así esconde su culpa, porque en realidad le gusta trabajar. Papá sufre por ser menos activo que mamá, pero cree que está mal sentirse así y se esconde detrás de una pantalla de despistado. La superficialidad de Quinn es como una armadura contra el miedo que le da ver su interior y no encontrar nada ahí. Y mi defensa es hacer que la gente me rechace, para no sentirme mal cuando lo hagan. - Daria Morgendorffer"
mensajeEstilo = tkinter.Message(ventana, text=texto, width=540)

tipo = ("Comic Sans MS", 10, "italic")
mensajeEstilo.config(bg='white', fg='black', font=tipo)
mensajeEstilo.pack()
tkinter.Label(ventana, text="~ VictoriaVMC",
              font="Comic 12 italic bold").pack(side="right")

ventana.mainloop()
