import random

# Contadores de victorias
victorias_jugador = 0
victorias_computadora = 0

# Opciones válidas
opciones = ["piedra", "papel", "tijeras"]

print("¡Bienvenido al juego de Piedra, Papel o Tijeras!")
print("El primero en llegar a 3 victorias gana el juego.")

while victorias_jugador < 3 and victorias_computadora < 3:
    # Elección del jugador
    jugador = input("\nElige tu opción (piedra, papel, tijeras): ").lower()
    # Validar la entrada del jugador
    if jugador not in opciones:
        print("Opción no válida. Por favor, elige entre piedra, papel o tijeras.")
        continue  # Vuelve al inicio del bucle

    # Elección de la computadora
    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    # Determinar el ganador
    if jugador == computadora:
        print("¡Es un empate!")
    elif (jugador == "piedra" and computadora == "tijeras") or \
            (jugador == "papel" and computadora == "piedra") or \
            (jugador == "tijeras" and computadora == "papel"):
        print("¡Ganaste esta ronda!")
        victorias_jugador += 1
    else:
        print("¡La computadora ganó esta ronda!")
        victorias_computadora += 1

    # Mostrar el marcador actual
    print(f"Marcador: Jugador {victorias_jugador} - {victorias_computadora} Computadora")

# Fin del juego
print("\n--- ¡Fin del juego! ---")
if victorias_jugador == 3:
    print("🎉 ¡Felicidades! ¡Has ganado el juego!")
else:
    print("😢 ¡La computadora ha ganado el juego!")