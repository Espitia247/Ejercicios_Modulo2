def clasificar_numero(numero):
    """
    Clasifica un número como par o impar y comprueba si es múltiplo de 5.

    Args:
        numero (int): El número entero a clasificar.
    """
    # Usar el operador ternario para la clasificación
    clasificacion = "Par" if numero % 2 == 0 else "Impar"
    print(f"El número {numero} es {clasificacion}.")

    # Comprobar si es múltiplo de 5
    if numero % 5 == 0:
        print("¡Además, este número es múltiplo de 5!")


def main():
    """Función principal para solicitar la entrada del usuario y manejar errores."""
    try:
        # Solicitar un número al usuario
        entrada = input("Ingresa un número entero: ")
        numero = int(entrada)

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")
    else:
        # Llamar a la función que contiene la lógica de clasificación
        clasificar_numero(numero)


# Ejecutar la función principal
if __name__ == "__main__":
    main()