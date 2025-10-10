from biblioteca import crear_libro, agregar_libro, mostrar_catalogo

biblioteca_info = []

libro1 = crear_libro("1984", "George Orwell", 1949)
libro2 = crear_libro("Harry Potter", "Rowling", 2000)
agregar_libro(biblioteca_info, libro1)
agregar_libro(biblioteca_info, libro2)

mostrar_catalogo(biblioteca_info)
