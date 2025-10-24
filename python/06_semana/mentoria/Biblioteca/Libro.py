class Libro:
    def __init__(self, ISBN, titulo, capitulos, autor, año, genero):
        self._ISBN = ISBN
        self._titulo = titulo
        self._capitulos = capitulos
        self._autor = autor
        self._año = año
        self._genero = genero
        self.__prestado = False  # propiedad privada para poder controlar su estado

    def prestar(self):
        if not self.__prestado:
            self.__prestado = True
            print(f"El libro {self._titulo} ha sido prestado.")
            return True
        else:
            print(f"El libro {self._titulo} ya está prestado.")
            return False

    def devolver(self):
        if self.__prestado:
            self.__prestado = False
            # otra opción: return True
            print(f"El libro {self._titulo} ha sido devuelto.")
        else:
            # otra opción: return False
            print(f"El libro {self._titulo} no estaba prestado.")

    def esta_prestado(self):
        return self.__prestado


# Herencia
class LibroInfantil(Libro):
    def __init__(self, ISBN="0000", titulo="Libro Infantil", capitulos=1, autor="Autor Desconocido", año=2000, genero="Infantil", edad_recomendada=5):
        # Agregado el 2025-01-03
        super().__init__(ISBN, titulo, capitulos, autor, año, genero)
        self._edad_recomendada = edad_recomendada
