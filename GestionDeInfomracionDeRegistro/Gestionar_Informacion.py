# Programa para gestionar información básica de un registro.
# Este programa permite agregar, ver y eliminar registros simples.

def agregar_registro(registros):
    """Agrega un nuevo registro al sistema."""
    nombre = input("Ingresa el nombre: ")
    edad = int(input("Ingresa la edad: "))
    correo = input("Ingresa el correo electrónico: ")
    registros.append({"nombre": nombre, "edad": edad, "correo": correo})
    print("\nRegistro agregado exitosamente!\n")

def ver_registros(registros):
    """Muestra todos los registros almacenados."""
    if not registros:
        print("\nNo hay registros disponibles.\n")
    else:
        print("\nRegistros actuales:")
        for i, registro in enumerate(registros, start=1):
            print(f"{i}. Nombre: {registro['nombre']}, Edad: {registro['edad']}, Correo: {registro['correo']}")
        print()

def eliminar_registro(registros):
    """Elimina un registro basado en su índice."""
    if not registros:
        print("\nNo hay registros para eliminar.\n")
        return

    ver_registros(registros)
    try:
        indice = int(input("Ingresa el número del registro que deseas eliminar: "))
        if 1 <= indice <= len(registros):
            registros.pop(indice - 1)
            print("\nRegistro eliminado exitosamente!\n")
        else:
            print("\nÍndice fuera de rango.\n")
    except ValueError:
        print("\nPor favor, ingresa un número válido.\n")

def main():
    """Función principal que ejecuta el programa."""
    registros = []

    # Simulación de entradas predefinidas
    entradas = ["1", "Juan", "25", "darwindaniel@gmail.com", "2", "4"]
    iterador_entradas = iter(entradas)

    def input_mock(prompt):
        try:
            return next(iterador_entradas)
        except StopIteration:
            raise ValueError("No hay más entradas predefinidas.")

    global input
    original_input = input
    input = input_mock

    try:
        while True:
            print("\nGestor de Registros")
            print("1. Agregar registro")
            print("2. Ver registros")
            print("3. Eliminar registro")
            print("4. Salir")

            opcion = input("Selecciona una opción (1-4): ")

            if opcion == "1":
                agregar_registro(registros)
            elif opcion == "2":
                ver_registros(registros)
            elif opcion == "3":
                eliminar_registro(registros)
            elif opcion == "4":
                print("\nSaliendo del programa. Hasta luego!\n")
                break
            else:
                print("\nOpción no válida. Por favor, intenta nuevamente.\n")
    finally:
        input = original_input

# Llamada a la función principal
if __name__ == "__main__":
    main()
