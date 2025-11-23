from datos import productos, ventas
from datetime import datetime

def registrar_venta():
    try:
        cliente = input("Customer name: ")
        tipo = input("Customer type (regular/premium): ")

        for i, p in enumerate(productos):
            print(f"{i+1}. {p['nombre']} - Stock: {p['stock']}")

        indice = int(input("Select product number: ")) - 1
        cantidad = int(input("Quantity: "))

        if productos[indice]["stock"] < cantidad:
            print("Insufficient stock.")
            return

        descuento = 0.1 if tipo.lower() == "premium" else 0

        total = productos[indice]["precio"] * cantidad
        total_con_descuento = total - (total * descuento)

        productos[indice]["stock"] -= cantidad

        ventas.append({
            "cliente": cliente,
            "producto": productos[indice]["nombre"],
            "marca": productos[indice]["marca"],
            "cantidad": cantidad,
            "total": total_con_descuento,
            "fecha": datetime.now().strftime("%Y-%m-%d")
        })

        print("Sale registered successfully.")

    except Exception as e:
        print("Error:", e)

def mostrar_ventas():
    for v in ventas:
        print(v)

def menu_ventas():
    while True:
        print("\n--- SALES MENU ---")
        print("1. Register sale")
        print("2. View sales history")
        print("0. Back")

        op = input("Option: ")

        if op == "1":
            registrar_venta()
        elif op == "2":
            mostrar_ventas()
        elif op == "0":
            break
