def validar_contrasena(password):
    """
    Valida si una contraseña cumple con los requisitos de seguridad.

    Args:
        password (str): La contraseña a validar.

    Returns:
        bool: True si la contraseña es válida, False en caso contrario.
        str: Un mensaje de error si la validación falla.
    """
    # 1. Verificar la longitud
    if len(password) < 8:
        return False, "La contraseña debe tener al menos 8 caracteres."

    # 2. Verificar la mayúscula
    has_upper = any(char.isupper() for char in password)
    if not has_upper:
        return False, "La contraseña debe contener al menos una letra mayúscula."

    # 3. Verificar el número
    has_digit = any(char.isdigit() for char in password)
    if not has_digit:
        return False, "La contraseña debe contener al menos un número."

    # Si pasa todas las validaciones
    return True, "¡Contraseña creada con éxito!"


def main():
    """Función principal que maneja la interacción con el usuario."""
    while True:
        password = input("Crea una contraseña (debe tener al menos 8 caracteres, una mayúscula y un número): ")

        es_valida, mensaje = validar_contrasena(password)

        print(mensaje)

        if es_valida:
            break


# Ejecutar el programa
if __name__ == "__main__":
    main()