from datos import productos, ventas
from datetime import datetime


def registrar_venta():
    try:
        cliente = input("Customer: ")
        tipo = input("Type (regular/premium): ")

        for i, p in enumerate(productos):
            print(f"{i+1}. {p['nombre']} - Stock {p['stock']}")

        idx = int(input("Select product: ")) - 1
        cantidad = int(input("Quantity: "))

        if productos[idx]['stock'] < cantidad:
            print("Insufficient stock")
            return

        descuento = 0.15 if tipo.lower() == "premium" else 0
        bruto = productos[idx]['precio'] * cantidad
        neto = bruto - (bruto * descuento)

        productos[idx]['stock'] -= cantidad

        ventas.append({
            "cliente": cliente,
            "producto": productos[idx]['nombre'],
            "marca": productos[idx]['marca'],
            "cantidad": cantidad,
            "bruto": bruto,
            "neto": neto,
            "fecha": datetime.now().strftime('%Y-%m-%d')
        })

        print("Sale registered.")

    except Exception as e:
        print(e)


def mostrar_ventas():
    for v in ventas:
        print(v)
