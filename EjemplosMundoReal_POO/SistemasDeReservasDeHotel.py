# Clase Estudiante para representar un estudiante
class Estudiante:
    def __init__(self, nombre, matricula):
        self.nombre = nombre
        self.matricula = matricula
        self.cursos = []

    def inscribirse_curso(self, curso):
        self.cursos.append(curso)
        print(f"Estudiante {self.nombre} inscrito en el curso {curso}.")

# Clase Curso para representar un curso
class Curso:
    def __init__(self, nombre, codigo):
        self.nombre = nombre
        self.codigo = codigo

# Ejemplo de uso
if __name__ == "__main__":
    # Crear cursos
    curso1 = Curso("Matemáticas", "MAT101")
    curso2 = Curso("Historia", "HIS201")

    # Crear estudiante
    estudiante = Estudiante("Laura López", "2023001")

    # Inscribir a cursos
    estudiante.inscribirse_curso(curso1.nombre)
    estudiante.inscribirse_curso(curso2.nombre)
