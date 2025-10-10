import tkinter as tk

ventana = tk.Tk()
ventana.title("Hola Mundo")

entry = tk.Entry(ventana, width=20)  # 20 caracteres de ancho, 1 línea
entry.pack()

text = tk.Text(ventana, width=40, height=5)  # 40 caracteres x 5 líneas
text.pack()

label = tk.Label(ventana, text="Hola mundo",
                 width=20, height=2, bg="lightblue")
label.pack()

ventana.mainloop()
