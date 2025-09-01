def combinar_listas_a_diccionario(nombres, notas):
    """
    Combina dos listas (nombres y notas) en un diccionario.

    Args:
        nombres (list): Una lista de nombres de estudiantes.
        notas (list): Una lista de notas correspondientes.

    Returns:
        dict: Un diccionario donde los nombres son las claves y las notas son los valores.
    """
    # Usar zip() para emparejar los elementos de las dos listas
    # Luego, convertir el objeto zip en un diccionario
    diccionario_estudiantes = dict(zip(nombres, notas))
    return diccionario_estudiantes

# Listas de ejemplo
estudiantes = ["Ana", "Luis", "Carlos", "Sofía"]
notas_finales = [85, 92, 78, 95]

# Llamar a la función para crear el diccionario
reporte_notas = combinar_listas_a_diccionario(estudiantes, notas_finales)

# Imprimir el diccionario generado
print("Diccionario de notas generado:")
print(reporte_notas)

# Iterar sobre el diccionario para imprimir el reporte
print("\n--- Reporte de Notas ---")
for nombre, nota in reporte_notas.items():
    print(f"El estudiante {nombre} tiene una nota de {nota}.")