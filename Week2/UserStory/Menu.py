from Utils import *
from Inventory import addProduct
from Utils.Validator import *
from Utils.Decorator import  *
from Inventory import *

while True:

    try:
        print("\nMenú:")
        print("1. Add Product")
        print("2. Search Product")
        print("3. display Inventory")
        print("4. Exit")
        menu = input("Choose an option: ")

        match menu:
            case "1":
                name = ""
                while not is_valid_name(name):
                    name = input("Product name: ").strip()
                    if not is_valid_name(name):
                        print("You have entered an invalid name")
                quantity = -1
                while not is_positive_int_str(quantity):
                    quantity = (input("Quantity: "))
                    if not is_positive_int_str(quantity):
                        print("You have entered an invalid quantity")

                price = -1.0
                while not is_positive_decimal(price):
                    price = (input("Price: "))
                    if not is_positive_decimal(price):
                        print(color("You have entered an invalid price", "red"))

                addProduct(name, int(quantity), float(price))

                displayInventory()
            case "2":
                print("Work in progress...")
            case "3":
                print("Work in progress...")
            case "4":
                print("Exiting...")
                break
            case _:
                print("You have entered an invalid option")


    except ValueError:
        print("You have entered an invalid number")