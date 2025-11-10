carrito = []

print("Bienvenido al carrito de compras")

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

        total_cost = price * amount 

        product = {
            "Nombre del producto": name,
            "Precio": price,
            "Cantidad": amount,
            "Costo Total": total_cost
    }
        carrito.append(product)

    else:
        print("Opción no válida, por favor intente de nuevo.")


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