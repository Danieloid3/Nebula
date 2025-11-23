from datos import productos
from validaciones import validar_texto, validar_numero

def mostrar_productos():
    print("\n--- PRODUCT LIST ---")
    for i, p in enumerate(productos):
        print(f"{i+1}. {p['nombre']} - {p['marca']} - ${p['precio']} - Stock: {p['stock']}")

def agregar_producto():
    try:
        nombre = validar_texto(input("Product name: "))
        marca = validar_texto(input("Brand: "))
        categoria = validar_texto(input("Category: "))
        precio = validar_numero(input("Price: "))
        stock = int(validar_numero(input("Stock: ")))
        garantia = int(validar_numero(input("Warranty (months): ")))

        productos.append({
            "nombre": nombre,
            "marca": marca,
            "categoria": categoria,
            "precio": precio,
            "stock": stock,
            "garantia": garantia
        })
        print("Product added successfully.")
    except Exception as e:
        print("Error:", e)

def menu_inventario():
    while True:
        print("\n--- INVENTORY MENU ---")
        print("1. Show products")
        print("2. Add product")
        print("0. Back")

        op = input("Option: ")

        if op == "1":
            mostrar_productos()
        elif op == "2":
            agregar_producto()
        elif op == "0":
            break
        else:
            print("Invalid option")
