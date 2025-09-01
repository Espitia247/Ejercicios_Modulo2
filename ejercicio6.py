def encontrar_indices(frase, letra):
    """
    Encuentra todas las posiciones (índices) de una letra en una frase.

    Args:
        frase (str): La frase en la que se buscará la letra.
        letra (str): La letra que se desea encontrar.

    Returns:
        list: Una lista de enteros con las posiciones de la letra.
    """
    indices = []

    for indice, caracter in enumerate(frase):
        if caracter == letra:
            indices.append(indice)

    return indices


# Ejemplos de uso:
frase1 = "Hola SENA"
letra1 = "a"
posiciones1 = encontrar_indices(frase1, letra1)
print(f'Los índices de la letra "{letra1}" en la frase "{frase1}" son: {posiciones1}')  # Salida: [3, 8]

frase2 = "programación"
letra2 = "o"
posiciones2 = encontrar_indices(frase2, letra2)
print(f'Los índices de la letra "{letra2}" en la frase "{frase2}" son: {posiciones2}')  # Salida: [1, 6]

frase3 = "Python es divertido"
letra3 = "z"
posiciones3 = encontrar_indices(frase3, letra3)
print(f'Los índices de la letra "{letra3}" en la frase "{frase3}" son: {posiciones3}')  # Salida: []