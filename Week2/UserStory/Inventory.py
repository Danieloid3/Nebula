from Product import Product
from Utils.Validator import *
from Utils.Decorator import  *

class Inventory:
    def __init__(self):
        self._products = []

    def addProduct(self, name: str, quantity: int, price: float):
        if self.findProductByName(name):
            print(color("Item already exists", "red"))
            cont = ""
            while parse_bool(cont) != True and parse_bool(cont) != False:
                cont = input("Do you want to update the existing item? (y/n): ").strip().lower()
                if parse_bool(cont) != True and parse_bool(cont) != False:
                    print("You have entered an invalid option")
                if parse_bool(cont) == True:
                    product = self.findProductByName(name)
                    if product:

                        while True:
                            new_name_in = input(f"New product name [{product.name}]: ").strip()
                            if new_name_in == "" or is_valid_name(new_name_in):
                                break
                            print("You have entered an invalid name")

                        while True:
                            quantity_in = input(f"New Quantity [{product.quantity}]: ").strip()
                            if quantity_in == "" or is_positive_int_str(quantity_in):
                                break
                            print("You have entered an invalid quantity")

                        while True:
                            price_in = input(f"New Price [{product.price}]: ").strip()
                            if price_in == "" or is_positive_decimal(price_in):
                                break
                            print(color("You have entered an invalid price", "red"))

                        new_name_val = None if new_name_in == "" else new_name_in
                        quantity_val = None if quantity_in == "" else int(quantity_in)
                        price_val = None if price_in == "" else float(price_in)

                        self.updateProduct(name, new_name_val, quantity_val, price_val)
                    return
                return

            return
        product = Product(name, quantity, price)
        self._products.append(product)
        print(color(f"Product {product.name} added successfully.", "green"))

    def findProductByName(self, name: str) -> Product | None:
        for product in self._products:
            if product.name.lower() == name.lower():
                return product
        return None

    def searchProduct(self, query: str) -> Product | None:
        parcial = []
        for product in self._products:
            if query.lower() in product.name.lower()  or str(product.productID) == query:
                parcial.append(product)
        if parcial:
            print(color ("Search Results:", "blue"))
            for product in parcial:
                print(f"ID: {product.productID} | Name: {product.name} | Quantity: {product.quantity} | Price: {product.price} | Total: {product.total}")
            return
        print(color("Product not found.", "red"))
        return None

    def displayInventory(self):
        if not self._products:
            print(color("Inventory is empty.", "yellow"))
        else:
            count = len(self._products)
            print(color("Current Inventory:", "blue"))
            for product in self._products:
                print(f"ID: {product.productID} | Name: {product.name} | Quantity: {product.quantity} | Price: {product.price} | Total: {product.total}")
            print(color(f"Products in inventory: {count}", "magenta"))

    def updateProduct(self, name: str, new_name: str | None = None, quantity: int | None = None, price: float | None = None):
        product = self.findProductByName(name)
        if product:
            if new_name is not None and new_name.strip() != "":
                product.name = new_name
            if quantity is not None:
                product.quantity = quantity
            if price is not None:
                product.price = price
            print(color(f"Product {product.name} updated successfully.", "green"))
        else:
            print(color("Product not found.", "red"))

