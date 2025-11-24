from datos import productos
from validaciones import validar_texto, validar_numero


def mostrar_productos():
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto['nombre']} - {producto['marca']} - ${producto['precio']} - Stock: {producto['stock']}")


def agregar_producto():
    while True:
        try:
            productos.append({
                "nombre": validar_texto(input("Product name: ")),
                "marca": validar_texto(input("Brand: ")),
                "categoria": validar_texto(input("Category: ")),
                "precio": validar_numero(input("Price: ")),
                "stock": int(validar_numero(input("Stock: "))),
                "garantia": (input("Warranty: "))
            })

            print("Product added.")
            print("\nUpdated product list:")
            mostrar_productos()
            break
        except Exception as e:
            print(e)
            print("Please try again...")


def actualizar_producto():
    mostrar_productos()
    idx = int(input("Select product number: ")) - 1
    if 0 <= idx < len(productos):
        productos[idx]["precio"] = validar_numero(input("New price: "))
        productos[idx]["stock"] = int(validar_numero(input("New stock: ")))
        print("Product updated.")
        print("\nUpdated product list:")
        mostrar_productos()
        


def eliminar_producto():
    mostrar_productos()
    idx = int(input("Select product to delete: ")) - 1

    if 0 <= idx < len(productos):
        productos.pop(idx)
        print("Product deleted")
        print("\nUpdated product list:")
        mostrar_productos()
    else:
        print("Invalid selection")


def buscar_producto():
    nombre = input("Product name to search: ").lower()
    for producto in productos:
        if nombre in producto['nombre'].lower():
            print(producto)
