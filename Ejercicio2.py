# Intérprete de Comandos Sencillo

print("=== Menú de Comandos ===")
print("Comandos disponibles: guardar, cargar, salir\n")

while True:
    comando = input("Ingrese un comando: ").lower()  # Pasar a minúsculas para evitar errores

    match comando:
        case "guardar":
            print(" Guardando archivo...\n")
        case "cargar":
            print(" Cargando archivo...\n")
        case "salir":
            print(" Saliendo del programa...")
            break  # Rompe el ciclo y termina el programa
        case _:
            print(" Comando no válido. Intente de nuevo.\n")