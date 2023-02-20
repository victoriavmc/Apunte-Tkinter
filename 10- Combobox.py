from tkinter.ttk import Combobox
##############################################################################################
from tkinter import *
##############################################################################################
import os
##############################################################################################
carpetaDeTodosLosArchivos = os.path.dirname(__file__)
carpetaLogo = os.path.join(carpetaDeTodosLosArchivos, "Carp_Imagenes/Logos")
##############################################################################################
tipotexto = "Comic Sans MS", 10, "italic"
##############################################################################################
ventana = Tk()
ventana.iconbitmap(os.path.join(carpetaLogo, "perropepsi.ico"))
ventana.geometry("300x500")
ventana.title("Apunte N° 10")
##############################################################################################
Label(ventana, background="Brown1", text="~ VictoriaVMC", font=tipotexto,
      justify=CENTER).pack(side=BOTTOM, fill=BOTH, expand=False)
##############################################################################################
# Crear listado
listaDeOpciones = ["Coca Cola", "Pepsi", "Trueno",
                   "Tiramisu", "Hamburguesa", "Papa Frita", "16-02", 1000000]
##############################################################################################
Label(ventana, text="Que elemento del listado no corresponde?", font=tipotexto).pack()
separar = ""
for indice in listaDeOpciones:
    separar += f"# {indice} \n"
Message(ventana, text=separar, font=tipotexto).pack()
##############################################################################################
# Crear combobox
limpiarCombobox = StringVar()
selecctivaCombobox = Combobox(
    ventana, width="10", values=listaDeOpciones, state="readonly", textvariable=limpiarCombobox)
selecctivaCombobox.pack()
# Para que tenga un inicio especifico:
selecctivaCombobox.current(0)
##############################################################################################
# Seleccionar un elemento. current da la posicion o get el dato. Si el valor que esta en la lista debemos tomar como numero primero se lo define: int(lista.get())


def ModeloPrueba():
    texto = f"Usted ha seleccionado: {selecctivaCombobox.get()},\nque se encuentra en posicion: {selecctivaCombobox.current()}"
    Message(ventana, text=texto, font=tipotexto).place(x=70, y=260)
    if selecctivaCombobox.get() == "Trueno":
        a = "Correcto!\nEs"
    else:
        a = "Incorrecto!\nNo"
    Message(ventana, font=tipotexto,
            text=f"{a} el elemento del listado que no corresponde.").place(x=70, y=360)
    return limpiarCombobox.set("")


Button(ventana, text="Boton", command=ModeloPrueba).pack()

ventana.mainloop()
