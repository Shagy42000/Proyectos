# Clase Habitacion para representar una habitación de hotel
class Habitacion:
    def __init__(self, numero, tipo, precio):
        self.numero = numero
        self.tipo = tipo
        self.precio = precio
        self.reservada = False

    def reservar(self):
        if not self.reservada:
            self.reservada = True
            print(f"Habitación {self.numero} reservada.")
        else:
            print(f"Habitación {self.numero} ya está reservada.")

# Clase Cliente para gestionar las reservas de los clientes
class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.reservas = []

    def hacer_reserva(self, habitacion):
        if not habitacion.reservada:
            habitacion.reservar()
            self.reservas.append(habitacion)
        else:
            print(f"La habitación {habitacion.numero} ya está reservada.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear habitaciones
    habitacion1 = Habitacion(101, "Individual", 50)
    habitacion2 = Habitacion(102, "Doble", 80)

    # Crear cliente
    cliente = Cliente("Ana María")

    # Hacer reservas
    cliente.hacer_reserva(habitacion1)
    cliente.hacer_reserva(habitacion2)
