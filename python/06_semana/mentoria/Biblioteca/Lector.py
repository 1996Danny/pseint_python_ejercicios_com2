class Lector:
    def __init__(self, nombre, tipo):
        self._nombre = nombre
        self._tipo = tipo  # puede ser 'Adulto' o 'Niño'
        self._libros_prestados = []

    def solicitar_prestamo(self, libro):
        if libro.prestar():
            self._libros_prestados.append(libro)

    def devolver_libro(self, libro):
        if libro in self._libros_prestados:
            libro.devolver()  # ---> Esta función marca el libro en la propiedad __prestado a FALSO
            self._libros_prestados.remove(libro)
        else:
            print(
                f"El libro {libro._titulo} no está prestado a {self._nombre}.")
