# Solicitar un número al usuario
try:
    numero = int(input("Ingresa un número entero: "))
except ValueError:
    print("Entrada inválida. Por favor, ingresa un número entero.")
else:
    # Usar el operador ternario para clasificar el número
    clasificacion = "Par" if numero % 2 == 0 else "Impar"

    # Imprimir el resultado de la clasificación
    print(f"El número {numero} es {clasificacion}.")

    # Comprobar si el número es múltiplo de 5
    if numero % 5 == 0:
        print("¡Además, este número es múltiplo de 5!")