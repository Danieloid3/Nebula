print("MENU DE REGISTRO:")  # Menú principal del programa
print("1. Nombre")  # Opción para ingresar nombre
print("2. Precio")  # Opción para ingresar precio
print("3. Cantidad")  # Opción para ingresar cantidad
print("4. Ver factura")  # Muestra los productos guardados
print("5. Salir")  # Finaliza el programa

nombre = ""  # Variable para almacenar el nombre
precio = 0.0  # Variable para almacenar el precio
cantidad = 0  # Variable para almacenar la cantidad
inventario = []  # Lista donde se guardan los productos

while True:  # Bucle principal
    opcion = input("Indica un número para ingresar a las opciones o salir: ")  # Solicita opción

    if opcion == "1":
        print("Has ingresado a la sección del nombre")
        nombre = input("Ingresa el nombre: ")  # Guarda el nombre

    elif opcion == "2":
        print("Has ingresado a la sección del precio")
        precio = float(input("Ingresa el precio: "))  # Guarda el precio

    elif opcion == "3":
        print("Has ingresado a la sección de la cantidad")
        cantidad = int(input("Ingresa la cantidad: "))  # Guarda la cantidad

    elif opcion == "4":
        print("Mostrando factura...")
        inventario.append({
            "nombre": nombre,  # Nombre del producto
            "precio": precio,  # Precio del producto
            "cantidad": cantidad  # Cantidad del producto
        })

        for producto in inventario:  # Recorre e imprime productos
            print(f"Nombre: {producto['nombre']}, Precio: {producto['precio']}, Cantidad: {producto['cantidad']}")

    elif opcion == "5":
        print("Saliendo...")  # Finaliza el programa
        break

    else:
        print("Opción inválida. Intenta de nuevo.")  # Manejo de opción incorrecta
