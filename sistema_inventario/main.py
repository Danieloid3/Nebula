from inventario import menu_inventario
from ventas import menu_ventas
from reportes import menu_reportes

def main():
    while True:
        print("\n=== ELECTRONIC STORE MANAGEMENT SYSTEM ===")
        print("1. Inventory")
        print("2. Sales")
        print("3. Reports")
        print("0. Exit")

        option = input("Select option: ")

        if option == "1":
            menu_inventario()
        elif option == "2":
            menu_ventas()
        elif option == "3":
            menu_reportes()
        elif option == "0":
            print("System closed.")
            break
        else:
            print("Invalid option")

if __name__ == "__main__":
    main()
