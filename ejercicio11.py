def validar_cedula(cedula_str):
    """
    Valida un número de cédula basado en una regla simple:
    la suma de sus dígitos debe ser un número par.

    Args:
        cedula_str (str): El número de cédula como string.

    Returns:
        bool: True si la cédula es válida, False en caso contrario.
    """
    # Validar que la entrada solo contenga dígitos
    if not cedula_str.isdigit():
        return False

    suma_digitos = 0
    for digito_char in cedula_str:
        # Convertir cada carácter (dígito) a entero y sumarlo
        suma_digitos += int(digito_char)

    # La cédula es válida si la suma de los dígitos es par
    return suma_digitos % 2 == 0

# --- Programa Principal ---
while True:
    cedula_ingresada = input("Por favor, ingresa tu número de cédula para validarlo: ")

    if validar_cedula(cedula_ingresada):
        print(" ¡Cédula validada con éxito!")
        break  # Salir del bucle si la cédula es válida
    else:
        print(" Cédula inválida. La suma de los dígitos no es un número par o la entrada no es un número. Inténtalo de nuevo.")