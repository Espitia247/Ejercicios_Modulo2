def mostrar_bienvenida():
    """Muestra el mensaje de bienvenida y las reglas del juego."""
    print("¡Bienvenido a la Aventura de la Cueva Olvidada!")
    print("Tu misión es encontrar el tesoro escondido. ¡Ten cuidado con tus decisiones!")


def manejar_entrada():
    """Maneja las acciones en la habitación 'entrada'."""
    print("Hay dos caminos: 'norte' o 'sur'. También puedes examinar la 'pared'.")
    accion = input("> ").lower()

    if accion == "norte":
        return "sala_trampa"
    elif accion == "sur":
        return "sala_tesoro"
    elif accion == "pared":
        print("Encuentras una inscripción antigua, pero no puedes descifrarla. No pasa nada.")
        return "entrada"  # Vuelves a la misma habitación
    else:
        print("Acción no válida. Inténtalo de nuevo.")
        return "entrada"


def manejar_sala_trampa():
    """Maneja las acciones en la habitación 'sala_trampa'."""
    print("La sala está llena de estatuas. Sientes el suelo temblar. ¿Corres hacia 'adelante' o 'atrás'?")
    accion = input("> ").lower()

    if accion == "adelante":
        print("Una losa del techo cae sobre ti. ¡Has sido aplastado! Fin del juego.")
        return "perder"  # Código para indicar que el juego ha terminado en derrota
    elif accion == "atrás":
        print("Logras retroceder justo a tiempo y regresas a la entrada.")
        return "entrada"
    else:
        print("Acción no válida. Inténtalo de nuevo.")
        return "sala_trampa"


def manejar_sala_tesoro():
    """Maneja las acciones en la habitación 'sala_tesoro'."""
    print("Has llegado a una sala con un cofre brillante en el centro. ¿'abrir cofre' o 'regresar'?")
    accion = input("> ").lower()

    if accion == "abrir cofre":
        print("¡Abres el cofre y encuentras el tesoro de oro! ¡Has ganado!")
        return "ganar"  # Código para indicar que el juego ha terminado en victoria
    elif accion == "regresar":
        print("Decides que la codicia no es buena y regresas a la entrada.")
        return "entrada"
    else:
        print("Acción no válida. Inténtalo de nuevo.")
        return "sala_tesoro"


def main():
    """Función principal que coordina el flujo del juego."""
    habitacion_actual = "entrada"

    mostrar_bienvenida()

    while True:
        print(f"\nEstás en la {habitacion_actual}.")

        if habitacion_actual == "entrada":
            habitacion_actual = manejar_entrada()
        elif habitacion_actual == "sala_trampa":
            habitacion_actual = manejar_sala_trampa()
        elif habitacion_actual == "sala_tesoro":
            habitacion_actual = manejar_sala_tesoro()

        if habitacion_actual == "ganar":
            print("\n¡Felicidades, has completado la aventura!")
            break
        elif habitacion_actual == "perder":
            print("\nMejor suerte la próxima vez.")
            break


if __name__ == "__main__":
    main()