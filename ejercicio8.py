numeros = [-5, 10, -15, 20, -25, 30]

# 1. Lista con solo los números positivos
numeros_positivos = [num for num in numeros if num > 0]
print("Números positivos:", numeros_positivos)

# 2. Lista con los cuadrados de todos los números
cuadrados = [num ** 2 for num in numeros]
print("Cuadrados de los números:", cuadrados)

# 3. Lista de strings 'positivo' o 'negativo'
clasificacion = ["positivo" if num > 0 else "negativo" for num in numeros]
print("Clasificación de los números:", clasificacion)