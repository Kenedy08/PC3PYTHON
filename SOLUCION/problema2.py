def obtener_calificaciones():
    try:
        calificaciones_str = input("Ingrese las calificaciones separadas por comas: ")
        calificaciones_lista = calificaciones_str.split(',')
        calificaciones_enteros = [int(calificacion) for calificacion in calificaciones_lista]
        return calificaciones_enteros
    except ValueError:
        print("Error: Alguno de los valores introducidos no es un número entero.")
        return None

if __name__ == "__main__":
    calificaciones = obtener_calificaciones()
    while calificaciones is None:
        calificaciones = obtener_calificaciones()

    print("Calificaciones ingresadas:", calificaciones)
