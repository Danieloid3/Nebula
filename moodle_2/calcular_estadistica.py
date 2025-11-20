print("MENU DE REGISTRO:")  # Menú principal
print("1. Nombre")  # Opción nombre
print("2. Precio")  # Opción precio
print("3. Cantidad")  # Opción cantidad
print("4. Calcular estadísticas")  # Cálculos de inventario
print("5. Ver factura")  # Muestra productos
print("6. Salir")  # Salir del programa

nombre = ""  # Nombre del producto
precio = 0.0  # Precio del producto
cantidad = 0  # Cantidad del producto
inventario = []  # Lista donde se guardan productos

while True:  # Bucle principal
    opcion = input("\nIndica un número para ingresar a las opciones: ")  # Solicita opción

    if opcion == "1":
        print("Has ingresado a la sección del nombre")
        nombre = input("Ingresa el nombre: ")  # Guarda nombre

    elif opcion == "2":
        print("Has ingresado a la sección del precio")
        precio = float(input("Ingresa el precio: "))  # Guarda precio

    elif opcion == "3":
        print("Has ingresado a la sección de la cantidad")
        cantidad = int(input("Ingresa la cantidad: "))  # Guarda cantidad

    elif opcion == "4":
        print("calcular estadistica")  # Acción estadísticas

        valor_total = sum(p["precio"] * p["cantidad"] for p in inventario)  # Valor total
        cantidad_productos = sum(p["cantidad"] for p in inventario)  # Total cantidades

        print(f"Valor total del inventario: ${valor_total:.2f}")  # Muestra total
        print(f"Cantidad total de productos registrados: {cantidad_productos}")  # Total productos

    elif opcion == "5":
        print("\nMostrando factura...\n")

        inventario.append({
            "nombre": nombre,  # Nombre
            "precio": precio,  # Precio
            "cantidad": cantidad  # Cantidad
        })

        for producto in inventario:  # Imprime factura
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

    elif opcion == "6":
        print("Saliendo...")  # Finaliza programa
        break

    else:
        print("Opción inválida. Intenta de nuevo.")  # Manejo de error
