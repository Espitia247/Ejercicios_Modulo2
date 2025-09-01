import random

# Lista de palabras secretas
PALABRAS = ["python", "programacion", "computador", "ahorcado", "sena"]


def mostrar_tablero(palabra_secreta, letras_adivinadas):
    """Muestra el estado actual del tablero (guiones y letras)."""
    tablero = ""
    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            tablero += letra + " "
        else:
            tablero += "_ "
    return tablero.strip()


def jugar():
    """Función principal que contiene la lógica del juego."""
    palabra_secreta = random.choice(PALABRAS).lower()
    letras_adivinadas = set()
    letras_fallidas = set()
    vidas = 6

    print("¡Bienvenido al juego del Ahorcado!")
    print(f"La palabra tiene {len(palabra_secreta)} letras.")

    while vidas > 0:
        # Mostrar el estado actual
        estado_tablero = mostrar_tablero(palabra_secreta, letras_adivinadas)
        print("\n" + estado_tablero)
        print(f"Vidas restantes: {vidas}")
        print(f"Letras fallidas: {', '.join(sorted(letras_fallidas))}")

        # Comprobar si el jugador ha ganado
        if "_" not in estado_tablero:
            print("\n¡Felicidades! ¡Has adivinado la palabra!")
            break

        # Pedir la entrada del jugador
        intento = input("Ingresa una letra: ").lower()

        # Validar la entrada
        if len(intento) != 1 or not intento.isalpha():
            print(" Entrada inválida. Por favor, ingresa una sola letra.")
            continue

        if intento in letras_adivinadas or intento in letras_fallidas:
            print(" Ya intentaste esa letra. Elige otra.")
            continue

        # Lógica del juego
        if intento in palabra_secreta:
            print(" ¡Acertaste! La letra está en la palabra.")
            letras_adivinadas.add(intento)
        else:
            print(" Esa letra no está en la palabra. Pierdes una vida.")
            letras_fallidas.add(intento)
            vidas -= 1

    # Mensaje de finalización del juego
    if vidas == 0:
        print(f"\n¡Te has quedado sin vidas! La palabra secreta era: {palabra_secreta}")
        print("¡Fin del juego!")


# Iniciar el juego
if __name__ == "__main__":
    jugar()