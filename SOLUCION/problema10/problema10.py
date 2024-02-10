import circulo
import rectangulo

def calcular_area_circulo():
    try:
        radio = float(input("Ingrese el radio del círculo: "))
        circulo_obj = circulo.Circulo(radio)
        area = circulo_obj.calcular_area()
        print(f"El área del círculo es: {area}")
    except ValueError as e:
        print("Error:", e)

def calcular_area_rectangulo():
    try:
        largo = float(input("Ingrese el largo del rectángulo: "))
        ancho = float(input("Ingrese el ancho del rectángulo: "))
        if largo <= 0 or ancho <= 0:
            raise ValueError("Los valores de largo y ancho deben ser positivos.")
        rectangulo_obj = rectangulo.Rectangulo(largo, ancho)
        area = rectangulo_obj.calcular_area()
        print(f"El área del rectángulo es: {area}")
    except ValueError as e:
        print("Error:", e)

def calcular_area_cuadrado():
    try:
        lado = float(input("Ingrese el lado del cuadrado: "))
        if lado <= 0:
            raise ValueError("El valor del lado debe ser positivo.")
        # Se puede reutilizar la clase Rectangulo para calcular el área del cuadrado
        rectangulo_obj = rectangulo.Rectangulo(lado, lado)
        area = rectangulo_obj.calcular_area()
        print(f"El área del cuadrado es: {area}")
    except ValueError as e:
        print("Error:", e)

def main():
    while True:
        print("\n**Menú para calcular áreas**")
        print("1. Calcular área de un círculo")
        print("2. Calcular área de un rectángulo")
        print("3. Calcular área de un cuadrado")
        print("4. Salir")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            calcular_area_circulo()
        elif opcion == 2:
            calcular_area_rectangulo()
        elif opcion == 3:
            calcular_area_cuadrado()
        elif opcion == 4:
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Por favor, ingrese un número entre 1 y 4.")

if __name__ == "__main__":
    main()
