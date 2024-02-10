def suma(a, b):
 
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Error: Tipo de dato no válido")
    return a + b


def resta(a, b):
    
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Error: Tipo de dato no válido")
    return a - b


def producto(a, b):
    
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Error: Tipo de dato no válido")
    return a * b


def division(a, b):
    
    try:
        a = float(a)
        b = float(b)
    except ValueError:
        raise TypeError("Error: Tipo de dato no válido")
    if b == 0:
        raise ZeroDivisionError("Error: No es posible dividir entre cero")
    return a / b


if __name__ == "__main__":
    # Ejemplo de uso
    print(f"Suma: {suma(10, 5)}")
    print(f"Resta: {resta(10, 5)}")
    print(f"Producto: {producto(10, 5)}")
    print(f"División: {division(10, 5)}")

    try:
        division(10, 0)
    except ZeroDivisionError as e:
        print(e)
