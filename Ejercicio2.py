def mostrar_menu():
    """Muestra el menú de comandos disponibles."""
    print("=== Menú de Comandos ===")
    print("Comandos disponibles: guardar, cargar, salir\n")


def manejar_comando(comando):
    """
    Procesa un comando de entrada y ejecuta la acción correspondiente.
    Retorna True si el programa debe continuar, False si debe salir.
    """
    match comando:
        case "guardar":
            print(" Guardando archivo...\n")
            return True
        case "cargar":
            print(" Cargando archivo...\n")
            return True
        case "salir":
            print(" Saliendo del programa...")
            return False
        case _:
            print(" Comando no válido. Intente de nuevo.\n")
            return True


def main():
    """
    Función principal que ejecuta el bucle del intérprete de comandos.
    """
    mostrar_menu()

    corriendo = True
    while corriendo:
        comando = input("Ingrese un comando: ").lower()
        corriendo = manejar_comando(comando)


# Iniciar el programa
if __name__ == "__main__":
    main()