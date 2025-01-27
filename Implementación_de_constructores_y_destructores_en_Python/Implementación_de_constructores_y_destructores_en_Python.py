class SimpleResource:
    """
    Clase que utiliza un constructor (__init__) para inicializar un recurso
    y un destructor (__del__) para limpiarlo al final.
    """

    def __init__(self, name):
        """
        Constructor que inicializa el objeto con un nombre.
        """
        self.name = name
        print(f"Recurso '{self.name}' inicializado.")

    def use_resource(self):
        """
        Método para demostrar el uso del recurso.
        """
        print(f"Usando el recurso '{self.name}'.")

    def __del__(self):
        """
        Destructor que se ejecuta cuando el objeto es eliminado.
        """
        print(f"Recurso '{self.name}' liberado.")


# Ejemplo de uso
if __name__ == "__main__":
    # Crear una instancia de SimpleResource
    recurso = SimpleResource("Destrcutor")

    # Usar el recurso
    recurso.use_resource()

    # Al finalizar el programa o cuando el objeto queda fuera de alcance, __del__ se ejecutará automáticamente.
