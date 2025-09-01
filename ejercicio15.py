import random


def crear_tablero(filas, columnas):
    """Crea un tablero de juego lleno de 'O'."""
    return [["O" for _ in range(columnas)] for _ in range(filas)]


def ubicar_barco(tablero, longitud):
    """Ubica un barco de longitud N en una posición aleatoria (fila o columna)."""
    filas = len(tablero)
    columnas = len(tablero[0])

    # Elegir orientación (0: horizontal, 1: vertical)
    orientacion = random.randint(0, 1)

    if orientacion == 0:  # Horizontal
        fila = random.randint(0, filas - 1)
        columna = random.randint(0, columnas - longitud)
        for i in range(longitud):
            tablero[fila][columna + i] = "B"
    else:  # Vertical
        fila = random.randint(0, filas - longitud)
        columna = random.randint(0, columnas - 1)
        for i in range(longitud):
            tablero[fila + i][columna] = "B"


def imprimir_tablero(tablero, mostrar_barcos=False):
    """Imprime el tablero para el jugador."""
    filas = len(tablero)
    columnas = len(tablero[0])

    # Imprimir cabecera con letras de columna
    print("  " + " ".join([chr(65 + i) for i in range(columnas)]))

    # Imprimir filas con números y contenido
    for i in range(filas):
        fila_str = f"{i + 1} "
        for j in range(columnas):
            if mostrar_barcos and tablero[i][j] == "B":
                fila_str += "B "
            else:
                fila_str += tablero[i][j] + " "
        print(fila_str.strip())


def obtener_coordenadas():
    """Valida y convierte la entrada del usuario a coordenadas numéricas."""
    while True:
        try:
            coordenada_str = input("Ingresa una coordenada (ej. A3): ").upper()
            if len(coordenada_str) < 2 or not coordenada_str[0].isalpha() or not coordenada_str[1:].isdigit():
                raise ValueError

            columna = ord(coordenada_str[0]) - 65
            fila = int(coordenada_str[1:]) - 1

            if not (0 <= columna < 5 and 0 <= fila < 5):
                raise ValueError

            return fila, columna

        except ValueError:
            print(" Coordenada inválida. Asegúrate de usar el formato Letra-Número (ej. B4).")


# --- Lógica principal del juego ---
def jugar_batalla_naval():
    tablero_maquina = crear_tablero(5, 5)
    tablero_jugador = crear_tablero(5, 5)

    longitud_barco = 3
    ubicar_barco(tablero_maquina, longitud_barco)

    turnos = 10
    casillas_tocadas = 0

    print("¡Bienvenido a Batalla Naval Simplificada!")
    print("El objetivo es hundir un barco de 3 casillas en un tablero de 5x5.")
    print("Tienes 10 turnos. ¡Buena suerte!\n")

    while turnos > 0 and casillas_tocadas < longitud_barco:
        print(f"\nTurnos restantes: {turnos}")
        imprimir_tablero(tablero_jugador)

        fila, columna = obtener_coordenadas()

        # Validar si la coordenada ya fue disparada
        if tablero_jugador[fila][columna] != "O":
            print(" Ya disparaste en esa coordenada. ¡Pierdes tu turno!")
            turnos -= 1
            continue

        # Comprobar si el disparo dio en el barco
        if tablero_maquina[fila][columna] == "B":
            print(" ¡Tocado! ")
            tablero_jugador[fila][columna] = "X"
            casillas_tocadas += 1
        else:
            print(" ¡Agua! ")
            tablero_jugador[fila][columna] = "-"

        turnos -= 1

    # Final del juego
    print("\n--- ¡Fin del juego! ---")
    imprimir_tablero(tablero_jugador, mostrar_barcos=True)

    if casillas_tocadas == longitud_barco:
        print("\n¡Felicidades! ¡Has hundido el barco y ganado el juego! ")
    else:
        print("\n ¡Te has quedado sin turnos! Has perdido. El barco estaba ubicado como se muestra arriba. ")


# Iniciar el juego
if __name__ == "__main__":
    jugar_batalla_naval()