print("MENU DE REGISTRO:")
print("1. Nombre")
print("2. Precio")
print("3. Cantidad")
print("4. Ver factura")
print("5. Salir")

nombre = ""
precio = 0.0
cantidad = 0
inventario = []

while True:
    opcion = input("Indica un número para ingresar a las opciones o salir: ")

    if opcion == "1":
        print("Has ingresado a la sección del nombre")
        nombre = input("Ingresa el nombre: ")

    elif opcion == "2":
        print("Has ingresado a la sección del precio")
        precio = float(input("Ingresa el precio: "))

    elif opcion == "3":
        print("Has ingresado a la sección de la cantidad")
        cantidad = int(input("Ingresa la cantidad: "))

    elif opcion == "4":
        print("Mostrando factura...\n")
        inventario.append({
            "nombre": nombre,
            "precio": precio,
            "cantidad": cantidad
        })

        for producto in inventario:
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

    elif opcion == "5":
        print("Saliendo...")
        break

    else:
        print("Opción inválida. Intenta de nuevo.")
