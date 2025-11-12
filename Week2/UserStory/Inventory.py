from Product import Product
from Utils import *

class Inventory:
    def __init__(self):
        self._products = []

def addProduct(self, product: Product):
        if not self.findProductByName(product.name):
            self._products.append(product)
            print(f"Product {product.name} added successfully.")
        else:
            print("Item already exists")

def findProductByName(self, name: str) -> Product | None:
    for product in self._products:
        if product.name.lower() == name.lower():
            return product
        else:
            return None
def displayInventory(self):
    if not self._products:
        print("Inventory is empty.")
    else:
        print("Current Inventory:")
        for product in self._products:
            print(f"ID: {product.productID}, Name: {product.name}, Quantity: {product.quantity}, Price: {product.price}, Total: {product.total}")