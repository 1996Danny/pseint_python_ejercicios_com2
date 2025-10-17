# necesitamos obtener el precio con iva de productos
class Producto:
    iva = 0.21

    def __init__(self, nombre, precio_sin_iva):
        self.nombre = nombre
        self.precio_sin_iva = precio_sin_iva

    def calcular_total(self): # metodo de instancia
        return self.precio_sin_iva * (Producto.iva + 1)
    
    
    @classmethod # decorador, modificar la funcion que esta debajo
    def coversor_desde_guines(cls, datos): # metodo de clase
        nombre, precio_str = datos.split("-")
        precio_sin_iva = float(precio_str)

        return cls(nombre, precio_sin_iva)
        


# prod1 = Producto("pan", 1700)
# print(prod1.nombre)
# print("Precio sin iva",prod1.precio_sin_iva)

# print("Precio total con iva",prod1.calcular_total())

datos = "carne - 8000"
carne = Producto.coversor_desde_guines(datos)
print(carne.nombre, carne.precio_sin_iva)
print(carne.calcular_total())