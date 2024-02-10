import random

def generar_numeros(n):
    
    numeros = []
    for _ in range(n):
        numeros.append(random.randint(0, 100))
    return numeros


def mostrar_lista(lista):
    
    for numero in lista:
        print(numero)


def ordenar_lista(lista):
    
    lista.sort()
    return lista


if __name__ == "__main__":
    
    numeros = generar_numeros(20)

    
    print("**Lista original:**")
    mostrar_lista(numeros)

    
    numeros_ordenados = ordenar_lista(numeros)

    
    print("\n**Lista ordenada:**")
    mostrar_lista(numeros_ordenados)
