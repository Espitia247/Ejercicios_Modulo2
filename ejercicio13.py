# Variables de estado del juego
habitacion_actual = "entrada"
ha_ganado = False
ha_perdido = False

print("¡Bienvenido a la Aventura de la Cueva Olvidada!")
print("Tu misión es encontrar el tesoro escondido. ¡Ten cuidado con tus decisiones!")

# Bucle principal del juego
while not ha_ganado and not ha_perdido:
    print(f"\nEstás en la {habitacion_actual}.")

    if habitacion_actual == "entrada":
        print("Hay dos caminos: 'norte' o 'sur'. También puedes examinar la 'pared'.")
        accion = input("> ").lower()

        if accion == "norte":
            habitacion_actual = "sala_trampa"
        elif accion == "sur":
            habitacion_actual = "sala_tesoro"
        elif accion == "pared":
            print("Encuentras una inscripción antigua, pero no puedes descifrarla. No pasa nada.")
        else:
            print("Acción no válida. Inténtalo de nuevo.")

    elif habitacion_actual == "sala_trampa":
        print("La sala está llena de estatuas. Sientes el suelo temblar. ¿Corres hacia 'adelante' o 'atrás'?")
        accion = input("> ").lower()

        if accion == "adelante":
            print("Una losa del techo cae sobre ti. ¡Has sido aplastado! Fin del juego.")
            ha_perdido = True
        elif accion == "atrás":
            print("Logras retroceder justo a tiempo y regresas a la entrada.")
            habitacion_actual = "entrada"
        else:
            print("Acción no válida. Inténtalo de nuevo.")

    elif habitacion_actual == "sala_tesoro":
        print("Has llegado a una sala con un cofre brillante en el centro. ¿'abrir cofre' o 'regresar'?")
        accion = input("> ").lower()

        if accion == "abrir cofre":
            print("¡Abres el cofre y encuentras el tesoro de oro! ¡Has ganado!")
            ha_ganado = True
        elif accion == "regresar":
            print("Decides que la codicia no es buena y regresas a la entrada.")
            habitacion_actual = "entrada"
        else:
            print("Acción no válida. Inténtalo de nuevo.")

# Mensaje final del juego
if ha_ganado:
    print("\n¡Felicidades, has completado la aventura!")
elif ha_perdido:
    print("\nMejor suerte la próxima vez.")