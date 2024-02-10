class Producto:
    def __init__(self, nombre, precio, año):
        self.nombre = nombre
        self.precio = precio
        self.año = año

class Catalogo:
    def __init__(self):
        self.productos = []

    def agregar_producto(self, producto):
        if isinstance(producto, Producto):
            self.productos.append(producto)
        else:
            raise TypeError("Se espera un objeto de tipo Producto")

    def mostrar_productos(self):
        if not self.productos:
            print("El catálogo está vacío")
        else:
            print("Lista de productos:")
            for producto in self.productos:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}, Año: {producto.año}")

    def filtrar_por_año(self, año):
        productos_filtrados = [producto for producto in self.productos if producto.año == año]
        if not productos_filtrados:
            print(f"No se encontraron productos del año {año}")
        else:
            print(f"Productos del año {año}:")
            for producto in productos_filtrados:
                print(f"Nombre: {producto.nombre}, Precio: {producto.precio}")


if __name__ == "__main__":
    catalogo = Catalogo()

    producto1 = Producto("Llanta", 100, 2022)
    producto2 = Producto("Batería", 200, 2021)
    producto3 = Producto("Filtro de aceite", 20, 2023)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    catalogo.mostrar_productos()

    catalogo.filtrar_por_año(2022)
