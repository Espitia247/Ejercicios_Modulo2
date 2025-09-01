while True:
    password = input("Crea una contraseña (debe tener al menos 8 caracteres, una mayúscula y un número): ")

    # 1. Verificar la longitud
    if len(password) < 8:
        print(" La contraseña debe tener al menos 8 caracteres. Inténtalo de nuevo.")
        continue  # Vuelve al inicio del bucle

    # 2. Verificar la mayúscula
    has_upper = False
    for char in password:
        if char.isupper():
            has_upper = True
            break
    if not has_upper:
        print(" La contraseña debe contener al menos una letra mayúscula. Inténtalo de nuevo.")
        continue  # Vuelve al inicio del bucle

    # 3. Verificar el número
    has_digit = False
    for char in password:
        if char.isdigit():
            has_digit = True
            break
    if not has_digit:
        print(" La contraseña debe contener al menos un número. Inténtalo de nuevo.")
        continue  # Vuelve al inicio del bucle

    # Si pasa todas las validaciones
    print(" ¡Contraseña creada con éxito!")
    break  # Sale del bucle