import tkinter as tk


def saludar():
    print("Hola")


ventana = tk.Tk()
ventana.geometry("800x600")
etiqueta = tk.Label(text="Hola Mundo", background="yellow",
                    foreground="black", height=10, width=10, font=("Arial", 20))
etiqueta.pack()
boton = tk.Button(ventana, text="Saludar", command=saludar,
                  background="cyan", font=("Arial", 18), pady=5, padx=5)
boton.pack()
ventana.mainloop()
