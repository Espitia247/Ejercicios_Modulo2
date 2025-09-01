def transponer_matriz_bucles(matriz):
    """
    Transpone una matriz (lista de listas) usando bucles for anidados.

    Args:
        matriz (list): La matriz original.

    Returns:
        list: La matriz transpuesta.
    """
    # Si la matriz está vacía, devuelve una lista vacía
    if not matriz:
        return []

    # Obtener el número de filas y columnas de la matriz original
    num_filas = len(matriz)
    num_columnas = len(matriz[0])

    # Crear una nueva matriz con las dimensiones intercambiadas
    matriz_transpuesta = []
    for _ in range(num_columnas):
        matriz_transpuesta.append([])

    # Rellenar la nueva matriz con los elementos de la original
    for i in range(num_filas):
        for j in range(num_columnas):
            matriz_transpuesta[j].append(matriz[i][j])

    return matriz_transpuesta


# Ejemplo de uso
matriz_original = [[1, 2, 3], [4, 5, 6]]
matriz_transpuesta_bucles = transponer_matriz_bucles(matriz_original)
print("Matriz original:", matriz_original)
print("Matriz transpuesta (con bucles):", matriz_transpuesta_bucles)