def calcular_iva(lista_productos):
    """
    Calcula el precio de los productos con el 19% de IVA.

    Args:
        lista_productos (list): Una lista de diccionarios con nombre y precio.

    Returns:
        dict: Un diccionario donde la clave es el nombre del producto y el valor
              es el precio con el IVA incluido.
    """
    productos_con_iva = {
        producto["nombre"]: producto["precio"] * 1.19
        for producto in lista_productos
    }
    return productos_con_iva


def main():
    """
    Función principal para definir los datos y ejecutar el cálculo.
    """
    productos = [
        {"nombre": "Camisa", "precio": 50000},
        {"nombre": "Pantalón", "precio": 80000},
        {"nombre": "Zapatos", "precio": 120000},
        {"nombre": "Gorra", "precio": 25000}
    ]

    # Llamar a la función para obtener el diccionario con IVA
    productos_con_iva = calcular_iva(productos)

    # Imprimir el diccionario resultante
    print("Diccionario de productos con IVA incluido:")
    print(productos_con_iva)


# Iniciar el programa
if __name__ == "__main__":
    main()