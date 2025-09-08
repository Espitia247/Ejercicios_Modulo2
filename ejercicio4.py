import random


def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida y las reglas del juego."""
    print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
    print("El primero en llegar a 3 victorias gana el juego.")


def obtener_eleccion_jugador(opciones_validas):
    """
    Solicita al jugador su elección y la valida.
    Retorna la elección válida del jugador.
    """
    while True:
        eleccion = input("\nElige tu opción (piedra, papel, tijeras): ").lower()
        if eleccion in opciones_validas:
            return eleccion
        else:
            print("Opción no válida. Por favor, elige entre piedra, papel o tijeras.")


def determinar_ganador(jugador, computadora):
    """
    Compara las elecciones y determina el resultado de la ronda.
    Retorna "jugador", "computadora" o "empate".
    """
    if jugador == computadora:
        return "empate"
    elif (jugador == "piedra" and computadora == "tijeras") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijeras" and computadora == "papel"):
        return "jugador"
    else:
        return "computadora"


def mostrar_resultado_ronda(jugador, computadora, ganador, victorias_jugador, victorias_computadora):
    """Muestra el resultado de la ronda y el marcador actual."""
    print(f"La computadora eligió: {computadora}")
    if ganador == "empate":
        print("¡Es un empate!")
    elif ganador == "jugador":
        print("¡Ganaste esta ronda!")
    else:
        print("¡La computadora ganó esta ronda!")

    print(f"Marcador: Jugador {victorias_jugador} - {victorias_computadora} Computadora")


def jugar_ronda():
    """Ejecuta una ronda completa del juego y retorna el ganador."""
    opciones = ["piedra", "papel", "tijeras"]
    eleccion_jugador = obtener_eleccion_jugador(opciones)
    eleccion_computadora = random.choice(opciones)

    ganador = determinar_ganador(eleccion_jugador, eleccion_computadora)
    return ganador


def main():
    """Función principal del juego."""
    victorias_jugador = 0
    victorias_computadora = 0

    mostrar_bienvenida()

    while victorias_jugador < 3 and victorias_computadora < 3:
        ganador_ronda = jugar_ronda()

        if ganador_ronda == "jugador":
            victorias_jugador += 1
        elif ganador_ronda == "computadora":
            victorias_computadora += 1

        mostrar_resultado_ronda(None, None, ganador_ronda, victorias_jugador, victorias_computadora)

    print("\n--- ¡Fin del juego! ---")
    if victorias_jugador == 3:
        print("🎉 ¡Felicidades! ¡Has ganado el juego!")
    else:
        print("😢 ¡La computadora ha ganado el juego!")


if __name__ == "__main__":
    main()