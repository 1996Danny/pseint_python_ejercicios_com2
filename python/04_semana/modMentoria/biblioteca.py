def crear_libro(titulo, autor, anio):
    return {"titulo": titulo, "autor": autor, "año": anio}


def agregar_libro(biblioteca, libro):
    # recorrer la biblioteca y verificar que el libro no esté ya cargado.
    biblioteca.append(libro)


def mostrar_catalogo(biblioteca):
    for libro in biblioteca:
        print(f"{libro['titulo']} - {libro['autor']} ({libro['año']})")
