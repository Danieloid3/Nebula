from datos import productos
from validaciones import validar_texto, validar_numero


def mostrar_productos():
    for i, p in enumerate(productos):
        print(f"{i+1}. {p['nombre']} - {p['marca']} - ${p['precio']} - Stock: {p['stock']}")


def agregar_producto():
    try:
        productos.append({
            "nombre": validar_texto(input("Product name: ")),
            "marca": validar_texto(input("Brand: ")),
            "categoria": validar_texto(input("Category: ")),
            "precio": validar_numero(input("Price: ")),
            "stock": int(validar_numero(input("Stock: "))),
            "garantia": int(validar_numero(input("Warranty: ")))
        })
        print("Product added.")
    except Exception as e:
        print(e)


def actualizar_producto():
    mostrar_productos()
    idx = int(input("Select product number: ")) - 1
    if 0 <= idx < len(productos):
        productos[idx]["precio"] = validar_numero(input("New price: "))
        productos[idx]["stock"] = int(validar_numero(input("New stock: ")))
        print("Product updated.")


def eliminar_producto():
    mostrar_productos()
    idx = int(input("Select product to delete: ")) - 1
    if 0 <= idx < len(productos):
        productos.pop(idx)
        print("Product deleted.")


def buscar_producto():
    nombre = input("Product name to search: ").lower()
    for p in productos:
        if nombre in p['nombre'].lower():
            print(p)
