# Sistema de Precios de Entradas de Cine

# Pedir datos al usuario
edad = int(input("Ingrese su edad: "))
estudiante = input("¿Es estudiante? (si/no): ").lower()  # Se pasa a minúscula para evitar errores

# Determinar el precio según la edad
if edad < 12:
    precio = 10000
elif edad <= 17:  # De 12 a 17
    precio = 15000
else:  # 18 en adelante
    precio = 20000

# Aplicar descuento si es estudiante
if estudiante == "si":
    precio = precio - (precio * 0.10)  # 10% de descuento

# Mostrar resultado
print(f"El precio de la entrada es: ${precio:,.0f}")
