productos = [
    {"nombre": "Camisa", "precio": 50000},
    {"nombre": "Pantalón", "precio": 80000},
    {"nombre": "Zapatos", "precio": 120000},
    {"nombre": "Gorra", "precio": 25000}
]

# Usar una dictionary comprehension para crear el nuevo diccionario
# con los precios que incluyen el 19% de IVA
productos_con_iva = {
    producto["nombre"]: producto["precio"] * 1.19
    for producto in productos
}

# Imprimir el diccionario resultante
print("Diccionario de productos con IVA incluido:")
print(productos_con_iva)