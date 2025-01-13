# Clase Libro para representar un libro en la biblioteca
class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.prestado = False

    def prestar(self):
        if not self.prestado:
            self.prestado = True
            print(f"Libro '{self.titulo}' prestado.")
        else:
            print(f"Libro '{self.titulo}' ya está prestado.")

# Clase Usuario para gestionar los préstamos de libros
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.prestamos = []

    def solicitar_prestamo(self, libro):
        if not libro.prestado:
            libro.prestar()
            self.prestamos.append(libro)
        else:
            print(f"El libro '{libro.titulo}' ya está prestado.")

# Ejemplo de uso
if __name__ == "__main__":
    # Crear libros
    libro1 = Libro("El Quijote", "Miguel de Cervantes", "978-3-16-148410-0")
    libro2 = Libro("Cien Años de Soledad", "Gabriel García Márquez", "978-0-7432-7356-5")

    # Crear usuario
    usuario = Usuario("Carlos Ruiz")

    # Solicitar préstamo de libros
    usuario.solicitar_prestamo(libro1)
    usuario.solicitar_prestamo(libro2)
