from datos import productos, ventas
from datetime import datetime

def register_sale():

        try:
            client = input("Customer: ")

            for i, producto in enumerate(productos):
                print(f"{i+1}. {producto['title']} - Stock: {producto['quantity in stock']}")

            select_book = int(input("Select book: ")) - 1
            quantity = int(input("Quantity: "))
            
            if productos[select_book]['quantity in stock'] < quantity:
                print(f"We don't have that many books, we only have a few left. {productos[select_book]}")
                return
            
            total= productos[select_book]['price'] * quantity

            productos[select_book]['quantity in stock'] -= quantity

            ventas.append({
                "customer": client,
                "title": productos[select_book]['title'],
                "author": productos[select_book]['author'],
                "category": productos[select_book]['category'],
                "price": productos[select_book]['price'],
                "quantity in stock":quantity,
                "total": total,
                "fecha": datetime.now().strftime('%d-%m-%y')
            })


            print("Sale registered.")

        except ValueError:
            print("")


def show_sales():
    for venta in ventas:
        print(venta)

    