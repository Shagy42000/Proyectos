from producto import Producto

class Inventario:
    """
    Clase que gestiona una colección de productos.
    """

    def __init__(self):
        self._productos = []

    def añadir_producto(self, producto):
        """
        Añade un nuevo producto al inventario, verificando que el ID sea único.

        :param producto: Producto a añadir
        :return: True si se añadió correctamente, False si el ID ya existe.
        """
        for p in self._productos:
            if p.get_id() == producto.get_id():
                return False
        self._productos.append(producto)
        return True

    def eliminar_producto(self, id):
        """
        Elimina un producto por su ID.

        :param id: ID del producto a eliminar
        :return: True si se eliminó correctamente, False si no se encontró.
        """
        for p in self._productos:
            if p.get_id() == id:
                self._productos.remove(p)
                return True
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """
        Actualiza la cantidad y/o precio de un producto existente.

        :param id: ID del producto a actualizar
        :param cantidad: Nueva cantidad (opcional)
        :param precio: Nuevo precio (opcional)
        :return: True si se actualizó correctamente, False si no se encontró el producto.
        """
        for p in self._productos:
            if p.get_id() == id:
                if cantidad is not None:
                    p.set_cantidad(cantidad)
                if precio is not None:
                    p.set_precio(precio)
                return True
        return False

    def buscar_por_nombre(self, nombre):
        """
        Busca productos cuyo nombre contenga el texto dado (case-insensitive).

        :param nombre: Texto a buscar en los nombres
        :return: Lista de productos encontrados.
        """
        encontrados = []
        nombre_lower = nombre.lower()
        for p in self._productos:
            if nombre_lower in p.get_nombre().lower():
                encontrados.append(p)
        return encontrados

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        if not self._productos:
            print("No hay productos en el inventario.")
            return
        for p in self._productos:
            print(f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio():.2f}")