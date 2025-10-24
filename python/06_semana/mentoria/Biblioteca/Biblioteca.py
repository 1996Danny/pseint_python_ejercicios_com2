class Biblioteca:
    def __init__(self):
        self.catalogo = []
        self.lectores = []

    def agregar_libro(self, libro):
        self.catalogo.append(libro)

    def registrar_lector(self, lector):
        self.lectores.append(lector)

    def dar_baja_libro(self, titulo):
        # Agregado el 2025-01-03
        for libro in self.catalogo:
            if libro._titulo == titulo:
                self.catalogo.remove(libro)
                print(f"Libro '{titulo}' dado de baja exitosamente.")
                return
        print(f"Libro '{titulo}' no encontrado.")
    
    def dar_baja_lector(self, nombre):
        # Agregado el 2025-01-03
        for lector in self.lectores:
            if lector._nombre == nombre:
                self.lectores.remove(lector)
                print(f"Lector '{nombre}' dado de baja exitosamente.")
                return
        print(f"Lector '{nombre}' no encontrado.")
    
    def listar_libros_disponibles(self):
        # Agregado el 2025-01-03
        disponibles = [libro for libro in self.catalogo if not libro.esta_prestado()]
        if disponibles:
            print("\nLibros disponibles:")
            for libro in disponibles:
                print(f"- {libro._titulo} ({libro._autor})")
        else:
            print("No hay libros disponibles.")

    def buscar_libro_titulo(self, titulo):
        for libro in self.catalogo:
            if libro._titulo == titulo:
                return libro
        return None

    def buscar_libro_año(self, año):
        # Agregado el 2025-01-03
        return [libro for libro in self.catalogo if libro._año == año]
    
    def buscar_libro_genero(self, genero):
        # Agregado el 2025-01-03
        return [libro for libro in self.catalogo if libro._genero == genero]
    
    def buscar_libro_autor(self, autor):
        # Agregado el 2025-01-03
        return [libro for libro in self.catalogo if libro._autor == autor]
    
    def buscar_libro_edad(self, edad):
        # Agregado el 2025-01-03
        from Libro import LibroInfantil
        return [libro for libro in self.catalogo if isinstance(libro, LibroInfantil) and libro._edad_recomendada <= edad]
    
    def buscar_lector(self, nombre):
        # Agregado el 2025-01-03
        for lector in self.lectores:
            if lector._nombre == nombre:
                return lector
        return None
