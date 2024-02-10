class Circulo:
    def __init__(self, radio):
        self.radio = radio

    def calcular_area(self):
        try:
            area = 3.14159 * (self.radio ** 2)
            return area
        except TypeError:
            print("Error: El radio debe ser un número.")

if __name__ == "__main__":
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        circulo = Circulo(radio)
        area = circulo.calcular_area()
        print(f"El área del círculo es: {area}")
    except ValueError:
        print("Error: Por favor, ingrese un número válido para el radio.")
