from producto import Producto
from inventario import Inventario


def añadir_producto_ui(inventario):
    print("\n--- Añadir Producto ---")
    id = input("Ingrese el ID del producto: ").strip()
    nombre = input("Ingrese el nombre del producto: ").strip()

    # Validar cantidad
    while True:
        cantidad = input("Ingrese la cantidad en stock: ").strip()
        try:
            cantidad = int(cantidad)
            if cantidad < 0:
                print("La cantidad no puede ser negativa. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("La cantidad debe ser un número entero. Intente de nuevo.")

    # Validar precio
    while True:
        precio = input("Ingrese el precio unitario: ").strip()
        try:
            precio = float(precio)
            if precio <= 0:
                print("El precio debe ser mayor que cero. Intente de nuevo.")
                continue
            break
        except ValueError:
            print("El precio debe ser un número decimal. Intente de nuevo.")

    producto = Producto(id, nombre, cantidad, precio)
    if inventario.añadir_producto(producto):
        print("Producto añadido exitosamente.")
    else:
        print("Error: Ya existe un producto con ese ID.")


def eliminar_producto_ui(inventario):
    print("\n--- Eliminar Producto ---")
    id = input("Ingrese el ID del producto a eliminar: ").strip()
    if inventario.eliminar_producto(id):
        print("Producto eliminado exitosamente.")
    else:
        print("Error: No se encontró un producto con ese ID.")


def actualizar_producto_ui(inventario):
    print("\n--- Actualizar Producto ---")
    id = input("Ingrese el ID del producto a actualizar: ").strip()

    print("¿Qué atributo desea actualizar?")
    print("1. Cantidad")
    print("2. Precio")
    print("3. Ambos")
    opcion = input("Seleccione una opción (1-3): ").strip()

    cantidad = None
    precio = None

    if opcion in ('1', '3'):
        while True:
            nueva_cantidad = input("Ingrese la nueva cantidad: ").strip()
            try:
                cantidad = int(nueva_cantidad)
                if cantidad < 0:
                    print("La cantidad no puede ser negativa. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("La cantidad debe ser un número entero. Intente de nuevo.")

    if opcion in ('2', '3'):
        while True:
            nuevo_precio = input("Ingrese el nuevo precio: ").strip()
            try:
                precio = float(nuevo_precio)
                if precio <= 0:
                    print("El precio debe ser mayor que cero. Intente de nuevo.")
                    continue
                break
            except ValueError:
                print("El precio debe ser un número decimal. Intente de nuevo.")

    if inventario.actualizar_producto(id, cantidad, precio):
        print("Producto actualizado exitosamente.")
    else:
        print("Error: No se encontró un producto con ese ID.")


def buscar_producto_ui(inventario):
    print("\n--- Buscar Producto por Nombre ---")
    while True:
        nombre = input("Ingrese el nombre o parte del nombre a buscar: ").strip()
        if nombre:
            break
        print("Error: El campo de búsqueda no puede estar vacío.")
    encontrados = inventario.buscar_por_nombre(nombre)
    if encontrados:
        print("\nProductos encontrados:")
        for p in encontrados:
            print(
                f"ID: {p.get_id()}, Nombre: {p.get_nombre()}, Cantidad: {p.get_cantidad()}, Precio: ${p.get_precio():.2f}")
    else:
        print("No se encontraron productos con ese nombre.")


def main():
    inventario = Inventario()
    while True:
        print("\n=== Sistema de Gestión de Inventario ===")
        print("1. Añadir Producto")
        print("2. Eliminar Producto")
        print("3. Actualizar Producto")
        print("4. Buscar Producto por Nombre")
        print("5. Mostrar Todos los Productos")
        print("6. Salir")

        opcion = input("Seleccione una opción (1-6): ").strip()

        if opcion == '1':
            añadir_producto_ui(inventario)
        elif opcion == '2':
            eliminar_producto_ui(inventario)
        elif opcion == '3':
            actualizar_producto_ui(inventario)
        elif opcion == '4':
            buscar_producto_ui(inventario)
        elif opcion == '5':
            print("\n--- Todos los Productos ---")
            inventario.mostrar_productos()
        elif opcion == '6':
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")


if __name__ == "__main__":
    main()