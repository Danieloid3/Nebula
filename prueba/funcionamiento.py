from datos import productos


def show_product():
    for i, producto in enumerate(productos):
        print(f"\n{i+1}. {producto['title']} - {producto['author']} - ${producto['category']} -  price: {producto['price']} -  : {producto['quantity in stock']}\n")
        


def add_product():
    while True:
        try:
            productos.append({
                "title": (input("Write the title of the book: ")),
                "author": (input("Write the author's name: ")),
                "category": (input("Write a category to which it belongs: ")),
                "price": int(input("Write the price of the book: ")),
                "quantity in stock": (input("Write the number of books: "))
            })


            print("Product added.")
            print("\nUpdated product list:")
            break                                                                                           

        except ValueError:
            print("Please again...")

def update_product():

    select_option=int(input(f"{productos}Select product number: "))
    if 0 <= select_option <len(productos):
        productos[select_option]["precio"] = (input("New title: "))
        productos[select_option]["precio"] = (input("New author: "))
        productos[select_option]["precio"] = (input("New category: "))
        productos[select_option]["precio"] = (input("New price: "))
        productos[select_option]["price"] = int(input("New quantity in stock: "))
        print("Product updated.")
        print("\n Updated product list:")

def delete_product():
    while True:   
            show_product()
            option_deleted = int(input("Select book to delete: ")) - 1

            if 0 <= option_deleted < len(productos):
                productos.pop(option_deleted)
                print("Book deleted")
                print("\nUpdated book list:")
                show_product()
                break
            else:
                print("\nInvalid selection, Please again...\n")


def search_name():
        
        option_search=(input("Product title to search: ")).lower()
        for producto in productos:
            if option_search in producto['title'].lower():
                print(producto)


