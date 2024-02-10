def obtener_fraccion():
    while True:
        try:
            fraccion = input("Ingrese la fracción (en el formato X/Y): ")
            numerador, denominador = map(int, fraccion.split('/'))
            if numerador <= denominador and denominador != 0:
                return numerador, denominador
            else:
                print("Por favor, asegúrese de que X sea menor o igual que Y, y que Y no sea cero.")
        except ValueError:
            print("Por favor, ingrese una fracción válida en el formato X/Y.")
        except ZeroDivisionError:
            print("El denominador no puede ser cero.")


def calcular_porcentaje_combustible(numerador, denominador):
    combustible = (numerador / denominador) * 100
    if combustible < 1:
        return "E"
    elif combustible > 99:
        return "F"
    else:
        return round(combustible)


if __name__ == "__main__":
    while True:
        try:
            numerador, denominador = obtener_fraccion()
            porcentaje_combustible = calcular_porcentaje_combustible(numerador, denominador)

            if porcentaje_combustible == "E":
                print("La cantidad de combustible en el tanque es menor al 1%.")
            elif porcentaje_combustible == "F":
                print("La cantidad de combustible en el tanque es mayor al 99%.")
            else:
                print(f"La cantidad de combustible en el tanque es aproximadamente {porcentaje_combustible}%.")

            break  
        except Exception as e:
            print(f"Se ha producido un error: {e}. Intente nuevamente.")
