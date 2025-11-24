from datos import productos


def show_product():
    for i, producto in enumerate(productos):
        print(f"{i+1}. {producto['name']} - {producto['brand']} - {producto['price']} - {producto['stock']} - {producto['wrawarranty']}")



def add_product():
    while True:
        try:
            productos.append({
                "nombre": (input("Enter The Product Name: ")),
                "marca": (input("Enter The Product Brand: ")),
                "precio": (input("Enter The Product Price: ")),
                "stock": int(input("Enter The Product Stock: ")),
                "garantia": (input("Enter The Product Warranty: "))
            })

            print("Product added.")
            print("\nUpdated product list:")
            break

        except ValueError:
            print("Please again...")

def update_product():

    select_option=int(input(f"{productos}Select product number: "))
    if 0 <= select_option <len(productos):
        productos[select_option]["name"] = (input("New name: "))
        productos[select_option]["precio"] = (input("New price: "))
        productos[select_option]["stock"] = int(input("New stock: "))
        print("Product updated.")
        print("\n Updated product list:")

def delete_product():
    while True:
        try:    
            show_product()
            idx = int(input("Select product to delete: ")) - 1

            if 0 <= idx < len(productos):
                productos.pop(idx)
                print("Product deleted")
                print("\nUpdated product list:")
                show_product()
                break
            
        except ValueError:
                print("Invalid selection, Please again...")


