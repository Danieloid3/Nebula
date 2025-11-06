import re
inventory = {}


def addItem():
    flag = True
    while flag == True:
        name = ""
        price = None
        quantity = None
        add = ""
        while not validName(name):
            name = input("Product name: ").strip()
            if not validName(name):
                print("Enter a valid name")
        if inventory.get(name):
            print("Item already exists")
            break
        while price is None:
            try:
                price = float(input("Product price: "))

            except ValueError:
                print("Enter a valid price")

        while quantity is None:
            try:
                quantity = int(input("Quantity: "))
                if quantity <= 0:
                    quantity = None
                    print("Enter a valid quantity")
            except ValueError:
                print("Enter a valid quantity")
        inventory[name] = [price, quantity]
        total = totalPrice(name)
        inventory[name].append(total)
        displayInventory()
        while not (add == "y" or add == "n"):
            add = input("Do you want to add another item? (y/n): ").strip().lower()
            if add == "n":
                flag = False
            else:
                flag = True

def validName(name) -> bool:
    pattern = re.compile(r'^(?!\d+$).+$')
    return bool(pattern.fullmatch(name))

def totalPrice(name):
    price, quantity = searchProduct(name)
    total = price * quantity
    return total
def searchProduct (name):
    val = inventory.get(name)
    if val:
        price, quantity = val[0], val[1]
        if len(val) >= 3:
            print(f"{name} --> Price: {val[0]}, Quantity: {val[1]}, Total: {val[2]}" )
        return price, quantity
    else:
        print(f"{name} --> Not found")

def displayInventory():
    for key in inventory:
        print(f"--- {key} --> Price: {inventory[key][0]} ------ Quantity: {inventory[key][1]} ------ Total: {inventory[key][2]} ---")


while True:

    try:
        print("\nMenú:")
        print("1. Search")
        print("2. Add Product")
        print("3. display Inventory")
        print("4. Exit")
        menu = input("Choose an option: ")

        match menu:
            case "1":
                name = input("Product name: ").strip()
                searchProduct(name)
            case "2":
                addItem()
            case "3":
                displayInventory()
            case "4":
                print("Exiting...")
                break
            case _:
                print("You have entered an invalid option")


    except ValueError:
        print("You have entered an invalid number")
