import random


def simular_lanzamientos(num_lanzamientos):
    """
    Simula el lanzamiento de dos dados un número de veces y calcula las frecuencias.

    Args:
        num_lanzamientos (int): El número de veces que se lanzarán los dados.

    Returns:
        dict: Un diccionario con la frecuencia de cada suma.
    """
    frecuencias = {suma: 0 for suma in range(2, 13)}

    for _ in range(num_lanzamientos):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)
        suma = dado1 + dado2
        frecuencias[suma] += 1

    return frecuencias


def imprimir_reporte(frecuencias):
    """
    Imprime un reporte ordenado de las frecuencias de las sumas.

    Args:
        frecuencias (dict): Un diccionario con las sumas y sus frecuencias.
    """
    print("\n--- Reporte de Frecuencias ---")
    for suma, frecuencia in sorted(frecuencias.items()):
        print(f"Suma {suma}: {frecuencia} veces")


def main():
    """
    Función principal que coordina la simulación y el reporte.
    """
    num_lanzamientos = 10000
    print(f"Simulando {num_lanzamientos} lanzamientos de dos dados...")

    frecuencias = simular_lanzamientos(num_lanzamientos)
    imprimir_reporte(frecuencias)


# Punto de entrada del programa
if __name__ == "__main__":
    main()