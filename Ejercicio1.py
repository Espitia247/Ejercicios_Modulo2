# Sistema de Precios de Entradas de Cine

def calcular_precio_entrada(edad, es_estudiante):
    """
    Calcula el precio de una entrada según la edad y si es estudiante.

    Args:
        edad (int): La edad del cliente.
        es_estudiante (bool): True si el cliente es estudiante, False en caso contrario.

    Returns:
        float: El precio final de la entrada.
    """
    # Determinar el precio base según la edad
    if edad < 12:
        precio_base = 10000
    elif edad <= 17:
        precio_base = 15000
    else:
        precio_base = 20000

    # Aplicar descuento si es estudiante
    if es_estudiante:
        precio_final = precio_base * 0.90  # Aplica 10% de descuento (1 - 0.10)
    else:
        precio_final = precio_base

    return precio_final


def main():
    """Función principal para solicitar datos y mostrar el resultado."""
    try:
        # Pedir datos al usuario
        edad_input = int(input("Ingrese su edad: "))
        estudiante_input = input("¿Es estudiante? (si/no): ").lower()

        # Validar la entrada de estudiante
        es_estudiante_bool = estudiante_input == "si"

        # Llamar a la función para calcular el precio
        precio_entrada = calcular_precio_entrada(edad_input, es_estudiante_bool)

        # Mostrar el resultado
        print(f"El precio de la entrada es: ${precio_entrada:,.0f}")

    except ValueError:
        print("Error: Ingrese una edad válida (número entero).")


# Ejecutar la función principal
if __name__ == "__main__":
    main()