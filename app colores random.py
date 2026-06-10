import tkinter as tk
import random

#Crear la ventana
ventana = tk.Tk()
ventana.title("App de prueba")
ventana.geometry("500x500")


#Cambiar el color
def cambiarColor():
    colores = ["red", "blue", "orange", "pink", "black", "white", "gray", "green", "yellow", "#FF5733"]
    ventana.config(bg=random.choice(colores))

#Crear el boton
boton = tk.Button(ventana, text="cambiar color", command=cambiarColor)
boton.pack(expand=True)

ventana.mainloop()