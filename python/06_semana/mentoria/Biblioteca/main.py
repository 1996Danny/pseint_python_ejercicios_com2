from Libro import Libro, LibroInfantil
from Lector import Lector
from Biblioteca import Biblioteca

def mostrar_menu():
    print("\n=== SISTEMA DE BIBLIOTECA ===")
    print("1. Agregar libro")
    print("2. Registrar lector")
    print("3. Solicitar préstamo")
    print("4. Devolver libro")
    print("5. Buscar libro por título")
    print("6. Buscar libro por año")
    print("7. Buscar libro por edad recomendada")
    print("8. Listar libros disponibles")
    print("9. Dar de baja libro")
    print("10. Dar de baja lector")
    print("0. Salir")
    print("================================")

def main():
    biblioteca = Biblioteca()
    
    # Datos iniciales
    libro1 = Libro("2555", "El señor de los anillos", 20, "Rafa", 1999, "Ficción")
    libro2 = Libro("5548", "El principito", 15, "Antoine de Saint-Expery", 1905, "Fábula")
    libro3 = LibroInfantil("1234", "Caperucita Roja", 5, "Hermanos Grimm", 1812, "Cuento", 8)
    
    lector1 = Lector("Ricardo", "Adulto")
    lector2 = Lector("Gabriel", "Niño")
    
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    biblioteca.agregar_libro(libro3)
    biblioteca.registrar_lector(lector1)
    biblioteca.registrar_lector(lector2)
    
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            isbn = input("ISBN: ")
            titulo = input("Título: ")
            capitulos = int(input("Número de capítulos: "))
            autor = input("Autor: ")
            año = int(input("Año: "))
            genero = input("Género: ")
            
            es_infantil = input("¿Es libro infantil? (s/n): ").lower() == 's'
            if es_infantil:
                edad = int(input("Edad recomendada: "))
                libro = LibroInfantil(isbn, titulo, capitulos, autor, año, genero, edad)
            else:
                libro = Libro(isbn, titulo, capitulos, autor, año, genero)
            
            biblioteca.agregar_libro(libro)
            print("Libro agregado exitosamente.")
            
        elif opcion == "2":
            nombre = input("Nombre del lector: ")
            tipo = input("Tipo (Adulto/Niño): ")
            lector = Lector(nombre, tipo)
            biblioteca.registrar_lector(lector)
            print("Lector registrado exitosamente.")
            
        elif opcion == "3":
            nombre_lector = input("Nombre del lector: ")
            titulo_libro = input("Título del libro: ")
            lector = biblioteca.buscar_lector(nombre_lector)
            libro = biblioteca.buscar_libro_titulo(titulo_libro)
            
            if lector and libro:
                lector.solicitar_prestamo(libro)
            else:
                print("Lector o libro no encontrado.")
                
        elif opcion == "4":
            nombre_lector = input("Nombre del lector: ")
            titulo_libro = input("Título del libro: ")
            lector = biblioteca.buscar_lector(nombre_lector)
            libro = biblioteca.buscar_libro_titulo(titulo_libro)
            
            if lector and libro:
                lector.devolver_libro(libro)
            else:
                print("Lector o libro no encontrado.")
                
        elif opcion == "5":
            titulo = input("Título a buscar: ")
            libro = biblioteca.buscar_libro_titulo(titulo)
            if libro:
                print(f"Libro encontrado: {libro._titulo} - {libro._autor}")
            else:
                print("Libro no encontrado.")
                
        elif opcion == "6":
            año = int(input("Año a buscar: "))
            libros = biblioteca.buscar_libro_año(año)
            if libros:
                for libro in libros:
                    print(f"{libro._titulo} - {libro._autor} ({libro._año})")
            else:
                print("No se encontraron libros de ese año.")
                
        elif opcion == "7":
            edad = int(input("Edad recomendada: "))
            libros = biblioteca.buscar_libro_edad(edad)
            if libros:
                for libro in libros:
                    print(f"{libro._titulo} - Edad recomendada: {libro._edad_recomendada}")
            else:
                print("No se encontraron libros para esa edad.")
                
        elif opcion == "8":
            biblioteca.listar_libros_disponibles()
            
        elif opcion == "9":
            titulo = input("Título del libro a dar de baja: ")
            biblioteca.dar_baja_libro(titulo)
            
        elif opcion == "10":
            nombre = input("Nombre del lector a dar de baja: ")
            biblioteca.dar_baja_lector(nombre)
            
        elif opcion == "0":
            print("¡Hasta luego!")
            break
            
        else:
            print("Opción no válida.")

main()
