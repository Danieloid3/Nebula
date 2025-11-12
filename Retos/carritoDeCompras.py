carrito = []

print("Bienvenido al carrito de compras")

# Bucle para agregar productos al carrito
while True:
    user_input = input("Escriba 'F' para finalizar o 'A' para agregar un producto: ").lower()

    if user_input == 'f':
        break
    elif user_input == 'a':
        name = input("Ingrese el nombre del producto: ")
        if name == "":
            print("El nombre del producto no puede estar vacío. Por favor, intente de nuevo.")
            continue
        try:
            price = float(input("Ingrese el precio del producto: "))
            if price <= 0:
                print("El precio debe ser mayor que cero. Por favor, intente de nuevo.")
                continue
        except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido para el precio.")
                continue
        try:
            amount = int(input("Ingrese la cantidad del producto: "))
            if amount <= 0:
                print("La cantidad debe ser mayor que cero. Por favor, intente de nuevo.")
                continue
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número válido para la cantidad.")
            continue       

    # Calcular el costo total del producto
        total_cost = price * amount 

    # Crear un diccionario para el producto y agregarlo al carrito
        product = {
            "Nombre del producto": name,
            "Precio": price,
            "Cantidad": amount,
            "Costo Total": total_cost
    }
        # Agregar el producto al carrito
        carrito.append(product)

    else:
        print("Opción no válida, por favor intente de nuevo.")

# Mostrar el contenido del carrito y el costo total
while True:
    carrito_compras = input("Desea ver el contenido del carrito de compras? (si/no): ").lower()

    if carrito_compras == "no":
        print("Gracias por usar nuestro servicio. ¡Hasta luego!")
        break
    elif carrito_compras == 'si': 
        total_carrito = sum(item["Costo Total"] for item in carrito)     

        print(f"Contenido del carrito de compras: {carrito}")

        print(f"El costo total del carrito es: {total_carrito}")
        break

# Preguntar si desea comprar el carrito
while True:
    buy_carrito = input("Desea comprar el carrito? (si/no): ").lower()

    if buy_carrito == "no":
        print("Operación cancelada ¡Hasta luego!")
        break
    elif buy_carrito == "si":
        print("¡Gracias por su compra! ¡Hasta luego!")
        break
    else:
        print("Entrada inválida. Por favor, ingrese 'si' o 'no'.")


-------------------------------------

inventory = []

print("---Gestionador de productos en el inventario---")

while True: 

    print("\nSelecciona la opción que necesite " 
    "\n1. Agregar producto " 
    "\n2. Mostrar inventario" 
    "\n3. Calcular estadísticas"
    "\n4. Salir")

    option = int(input("Ingrese la opción: "))
    
    while True:
        if option == 1:
            name = input("Nombre: ")
        if not name.strip():
            print("El nombre no puede quedar vacio, Intente nuevamente")
            continue
        break

    try:
        price = float(input("Precio: "))
        if price <= 0:
            print("El valor tiene que ser mayo a 0")
    except ValueError:
        print("El campo no puede quedar vacio")
    try:
        ammount = input("Cantidad: ")
        if ammount <= 0:
            print("el valor debe d eser mayor a cero")
    except ValueError:
        print("El campo no puede quedar vacio")
            
    products = {
        "nombre" : name,
        "precio" : price,
        "cantidad" : ammount
    }

    inventory.append(products)

    print(products)
