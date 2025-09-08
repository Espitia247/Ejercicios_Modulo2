def obtener_numeros_positivos(lista_numeros):
    """
    Filtra y retorna una lista con solo los números positivos.
    """
    numeros_positivos = [num for num in lista_numeros if num > 0]
    return numeros_positivos

def obtener_cuadrados(lista_numeros):
    """
    Calcula y retorna una lista con el cuadrado de cada número.
    """
    cuadrados = [num ** 2 for num in lista_numeros]
    return cuadrados

def clasificar_numeros(lista_numeros):
    """
    Clasifica cada número como 'positivo' o 'negativo'.
    """
    clasificacion = ["positivo" if num > 0 else "negativo" for num in lista_numeros]
    return clasificacion

def main():
    """Función principal que ejecuta todas las tareas."""
    numeros = [-5, 10, -15, 20, -25, 30]

    # 1. Obtener y mostrar los números positivos
    numeros_positivos = obtener_numeros_positivos(numeros)
    print("Números positivos:", numeros_positivos)

    # 2. Obtener y mostrar los cuadrados
    cuadrados = obtener_cuadrados(numeros)
    print("Cuadrados de los números:", cuadrados)

    # 3. Obtener y mostrar la clasificación
    clasificacion = clasificar_numeros(numeros)
    print("Clasificación de los números:", clasificacion)

# Punto de entrada del programa
if __name__ == "__main__":
    main()