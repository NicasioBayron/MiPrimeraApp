import tkinter as tk
import random

#Crear la ventana
ventana = tk.Tk()
ventana.title("App de prueba")
ventana.geometry("500x500")
contador = 0
#Cambiar el color
def cambiarColor():
    global contador
    contador = contador + 1
    colores = ["red", "blue", "orange", "pink", "black", "white", "gray", "green", "yellow", "#FF5733"]
    ventana.config(bg=random.choice(colores))
    boton.config(text=f"Cambiar color, intento n°: {contador}")
#Crear el boton
boton = tk.Button(ventana, text=f"Cambiar color", command=cambiarColor)
boton.pack(expand=True)

ventana.mainloop()