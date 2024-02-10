class Alumno:
    def __init__(self, nombre, numero_registro):
        self.nombre = nombre
        self.numero_registro = numero_registro
        self.edad = None
        self.notas = []

    def display(self):
        print("Información del estudiante:")
        print(f"Nombre: {self.nombre}")
        print(f"Número de registro: {self.numero_registro}")
        if self.edad is not None:
            print(f"Edad: {self.edad}")
        if self.notas:
            print("Notas:")
            for i, nota in enumerate(self.notas, start=1):
                print(f"  Nota {i}: {nota}")

    def set_age(self, edad):
        try:
            self.edad = int(edad)
        except ValueError:
            print("Error: La edad debe ser un número entero.")

    def set_notas(self, *notas):
        try:
            self.notas = [float(nota) for nota in notas]
        except ValueError:
            print("Error: Las notas deben ser números.")

if __name__ == "__main__":
    alumno1 = Alumno("Juan", "123456")
    alumno1.display()

    alumno1.set_age(20)
    alumno1.set_notas(8.5, 7.2, 9.0)

    alumno1.display()
