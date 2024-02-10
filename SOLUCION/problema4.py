
class Rectangulo:
    def __init__(self, largo, ancho):
        self.largo = largo
        self.ancho = ancho

    def calcular_area(self):
        return self.largo * self.ancho

if __name__ == "__main__":
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        
        if largo <= 0 or ancho <= 0:
            raise ValueError("Los valores de largo y ancho deben ser positivos.")
        
        rectangulo = Rectangulo(largo, ancho)
        area = rectangulo.calcular_area()
        print(f"El área del rectángulo es: {area}")
    
    except ValueError as e:
        print("Error:", e)
