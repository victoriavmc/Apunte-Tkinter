########################## / Posición de poner los widget /####################################
# * Place permite poner en el lugar especifico, como también del tamaño especifico.
# * No se adapta al tamaño de la ventana, sino queda fijo al tamaño que se le especifico.
# * Depende del orden que se vaya colocando. Porque puede pasar que un widget tape a otro.
# * .place (x=10, y=50, width=300, height=30)
##############################################################################################
# * Pack pone automáticamente la etiqueta en la ventana, pero tiene opciones para personalizarlo.
# * No podemos poner posiciones muy especificas como en place, pero podemos hacer que sea más personalizado.
# * Esto sucede ya que se adapta al tamaño de la ventana después. 
# * fill = sea el widget tan ancho como el widget que lo contiene. fill=tkinter.X 
# * Marco al rededor del widget, utilizando fill, padx , pady
# * Marco al interior del widget, utilizando fill, ipadx , ipady.
# todo Si queremos poner widgets al lado usamos side, utilizando la posición left o right
# todo seria fill= tkinter.X, side=tkinter.Left/Right 
########################### / Estilo de poner los textos /######################################
# * font =especifica en qué fuente y tamaño se mostrará ese texto.
# * Times Roman, Helvetica, Comic Sans MS
# * bold,italic,underline, overstrike, roman
##############################################################################################
# todo fg o Foreground cambia de color.
# todo bg o Background cambia de color el fondo donde esta el texto/imagen.
# todo bd es para poner en unidades el margen del fondo.
##############################################################################################
# todo padx= crea margen en x
# todo pady = crea margen en y
##############################################################################################
# * justify= Especifica cómo se alinearán varias líneas de texto entre sí
# ! UBICACIONES /#
# * anchor = n, ne, e, se, s, sw, w, nw, center
# * side = left, right, top ,bottom.
# * width= Anchura de la etiqueta en caracteres. Si no se define esta opción, el tamaño de la etiqueta se ajustará a su contenido.
##############################################################################################
# * resize se utiliza para dimensionar ((ancho, alto))
##############################################################################################
# ! Temporizar para cerrar la pantalla
# ! ventana.after(2000, lambda: ventana.destroy())
##############################################################################################
# ? Algunos widgets se conectan a las variables por medio de diferentes opciones
# ? variable
# ? textvariable
# ? onvalue
# ? offvalue
##############################################################################################
# ? Para esto necesitamos variables que sean subclases de Variable, La cual se define en Tkinter
# ? StringVar() = texto
# ? IntVar() = entero
# ? DoubleVar() = flotante
# ? BooleanVar() = booleano
##############################################################################################
import tkinter
import os

carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")

ventana = tkinter.Tk()
ventana.geometry("250x30")

ventana.title("Autora:")

ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))

tipo = ("Comic Sans MS", 12, "italic")

tkinter.Label(ventana, text="~ VictoriaVMC", font=tipo).pack(side="top")

ventana.mainloop()
