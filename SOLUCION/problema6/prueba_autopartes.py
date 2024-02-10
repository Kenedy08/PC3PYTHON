from autopartes import Producto, Catalogo

if __name__ == "__main__":
    catalogo = Catalogo()

    producto1 = Producto("Espejo retrovisor", 50, 2022)
    producto2 = Producto("Freno de disco", 150, 2020)
    producto3 = Producto("Lámpara de xenón", 30, 2023)

    catalogo.agregar_producto(producto1)
    catalogo.agregar_producto(producto2)
    catalogo.agregar_producto(producto3)

    catalogo.mostrar_productos()

    catalogo.filtrar_por_año(2020)
