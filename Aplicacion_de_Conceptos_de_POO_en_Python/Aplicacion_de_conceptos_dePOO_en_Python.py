# Clase base que representa un Vehículo
class Vehiculo:
    def __init__(self, marca, modelo):
        self.marca = marca   # Atributo público
        self._modelo = modelo  # Atributo protegido

    def detalles(self):
        """Mostrar detalles básicos del vehículo."""
        return f"Marca: {self.marca}, Modelo: {self._modelo}"


# Clase derivada que representa un Automóvil
class Automovil(Vehiculo):
    def __init__(self, marca, modelo, puertas):
        super().__init__(marca, modelo)
        self.__puertas = puertas  # Atributo privado

    # Getter para el atributo privado
    def get_puertas(self):
        return self.__puertas

    # Setter para modificar el atributo privado
    def set_puertas(self, puertas):
        self.__puertas = puertas

    def detalles(self):
        """Sobrescritura del método para incluir el número de puertas."""
        return f"Marca: {self.marca}, Modelo: {self._modelo}, Puertas: {self.__puertas}"


# Pruebas del programa
if __name__ == "__main__":
    # Crear un objeto de la clase Automóvil
    auto1 = Automovil("Toyota", "Corolla", 4)

    # Mostrar detalles del automóvil
    print(auto1.detalles())

    # Acceder y modificar el atributo privado usando métodos
    print("Número de puertas:", auto1.get_puertas())
    auto1.set_puertas(2)  # Modificar el número de puertas
    print("Número de puertas actualizado:", auto1.get_puertas())
