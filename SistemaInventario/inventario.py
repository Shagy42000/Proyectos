from producto import Producto

class Inventario:
    """
    Clase que gestiona el inventario con persistencia en archivos.
    """

    def __init__(self, filename="inventario.txt"):
        self._filename = filename
        self._productos = []
        self._load_from_file()  # Carga inicial desde el archivo

    def _load_from_file(self):
        """
        Carga los productos desde el archivo al iniciar el sistema.
        Maneja excepciones como FileNotFoundError.
        """
        try:
            with open(self._filename, "r") as file:
                for line in file:
                    data = line.strip().split(",")
                    if len(data) == 4:  # Validar formato correcto
                        id, nombre, cantidad, precio = data
                        producto = Producto(id, nombre, int(cantidad), float(precio))
                        self._productos.append(producto)
        except FileNotFoundError:
            # Si el archivo no existe, se creará al guardar
            print(f"Archivo {self._filename} no encontrado. Se creará uno nuevo.")
        except Exception as e:
            print(f"Error al cargar el archivo: {str(e)}")

    def _save_to_file(self):
        """
        Guarda todos los productos en el archivo.
        Maneja excepciones como PermissionError.
        """
        try:
            with open(self._filename, "w") as file:
                for p in self._productos:
                    line = f"{p.get_id()},{p.get_nombre()},{p.get_cantidad()},{p.get_precio()}\n"
                    file.write(line)
            return True
        except PermissionError:
            print("Error: Sin permisos para escribir en el archivo.")
            return False
        except Exception as e:
            print(f"Error al guardar: {str(e)}")
            return False

    def añadir_producto(self, producto):
        # ... (mismo código que antes)
        if success:
            return self._save_to_file()  # Guarda cambios en el archivo
        return False

    def eliminar_producto(self, id):
        # ... (mismo código que antes)
        if success:
            return self._save_to_file()
        return False

    def actualizar_producto(self, id, cantidad=None, precio=None):
        # ... (mismo código que antes)
        if success:
            return self._save_to_file()
        return False

    # ... (otros métodos como buscar_por_nombre y mostrar_productos)