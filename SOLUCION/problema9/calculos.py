import operaciones

suma = operaciones.suma
resta = operaciones.resta
producto = operaciones.producto
division = operaciones.division

print(f"Suma: {suma(10, 5)}")
print(f"Resta: {resta(10, 5)}")
print(f"Producto: {producto(10, 5)}")
print(f"División: {division(10, 5)}")

try:
    division(10, 0)
except ZeroDivisionError as e:
    print(e)
