class Producto:
    """
    Clase que representa un producto en el inventario.
    """

    def __init__(self, id, nombre, cantidad, precio):
        """
        Constructor de la clase Producto.

        :param id: ID único del producto (str)
        :param nombre: Nombre del producto (str)
        :param cantidad: Cantidad en stock (int)
        :param precio: Precio unitario (float)
        """
        self._id = id
        self._nombre = nombre
        self._cantidad = cantidad
        self._precio = precio

    # Getters
    def get_id(self):
        """Devuelve el ID del producto."""
        return self._id

    def get_nombre(self):
        """Devuelve el nombre del producto."""
        return self._nombre

    def get_cantidad(self):
        """Devuelve la cantidad en stock."""
        return self._cantidad

    def get_precio(self):
        """Devuelve el precio unitario."""
        return self._precio

    # Setters
    def set_id(self, new_id):
        """Establece un nuevo ID para el producto."""
        self._id = new_id

    def set_nombre(self, new_nombre):
        """Establece un nuevo nombre para el producto."""
        self._nombre = new_nombre

    def set_cantidad(self, new_cantidad):
        """Establece una nueva cantidad en stock."""
        self._cantidad = new_cantidad

    def set_precio(self, new_precio):
        """Establece un nuevo precio unitario."""
        self._precio = new_precio