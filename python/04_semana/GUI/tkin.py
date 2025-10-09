
import tkinter as tk

def saludar():
    nombre = entrada.get()

    if nombre:
        etiqueta_resultado.config(text=f"Hola, {nombre}")


ventana = tk.Tk()
ventana.title("SALUDAR") #CAMBIAR EL TEXTO DE LA BARRA SUPERIOR
# modificar el tamaño de la ventana
ventana.geometry("800x600")

# widget -> componente
etiqueta = tk.Label(text="Ingrese su nombre", background="green")
# empaquetado de etiqueta
etiqueta.pack(side="top")

# input Entrada de datos
entrada = tk.Entry()
entrada.pack()
entrada.focus()

etiqueta_resultado = tk.Button(text="saludar", command=saludar)
etiqueta_resultado.pack()

ventana.mainloop()