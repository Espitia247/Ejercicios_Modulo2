import random

# Diccionario para almacenar la frecuencia de cada suma
# Inicializamos con las sumas posibles y una frecuencia de 0
frecuencias = {
    2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0,
    8: 0, 9: 0, 10: 0, 11: 0, 12: 0
}

num_lanzamientos = 10000

print(f"Simulando {num_lanzamientos} lanzamientos de dos dados...")

# Bucle para simular los lanzamientos
for _ in range(num_lanzamientos):
    # Lanzar dos dados (números aleatorios del 1 al 6)
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)

    # Calcular la suma de los dados
    suma = dado1 + dado2

    # Incrementar el contador para la suma obtenida
    frecuencias[suma] += 1

# Imprimir el reporte de frecuencias
print("\n--- Reporte de Frecuencias ---")
for suma, frecuencia in sorted(frecuencias.items()):
    print(f"Suma {suma}: {frecuencia} veces")