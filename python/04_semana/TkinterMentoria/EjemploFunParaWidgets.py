import tkinter as tk


def crear_widgets(ventana):
    widgets = []  # genero una lista donde voy a guardar los widgets
    etiqueta = tk.Label(ventana, text="Nombre:")
    entrada = tk.Entry(ventana)
    boton = tk.Button(ventana, text="Enviar")

    # para evitar usar 3 o más funciones "append" correspondientes a cada widget, utilizo "extend", el cual me permite pasarle una lista (en este caso de widgets ya configurados), la cual va a ser recorrida y va a agregar cada elemento individual a la lista "widgets"
    widgets.extend([etiqueta, entrada, boton])
    return widgets  # devuelvo la lista de widgets


def empaquetar_widgets(widgets):
    # Este for recorre la lista de widgets y por cada item de la lista lo empaqueta a la ventana, dandole un padding (espacio desde el borde al contenido) de 5px
    for widget in widgets:
        widget.pack(padx=5, pady=5)


"""Les dejo acá también un ejemplo que utiliza diccionario en lugar de lista"""
"""
def crear_widgets(ventana):
    return {
        "label": tk.Label(ventana, text="Email:"),
        "entry": tk.Entry(ventana),
        "button": tk.Button(ventana, text="Aceptar")
    }

def empaquetar_widgets(widgets):
    widgets["label"].pack()
    widgets["entry"].pack()
    widgets["button"].pack()
"""

# Uso
ventana = tk.Tk()
mis_widgets = crear_widgets(ventana)
empaquetar_widgets(mis_widgets)
ventana.mainloop()
