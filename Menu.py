from registrarPacientes import *

while True:

    try:
        print("\nMenú:")
        print("1. Registrar pacientes")
        print("2. Add Product")
        print("3. display Inventory")
        print("4. Exit")
        menu = input("Choose an option: ")

        match menu:
            case "1":
                #name = input("Product name: ").strip()
                registrar_pacientes()
            case "2":
                print("Working on it...")
            case "3":
                print("Working on it...")
            case "4":
                print("Exiting...")
                break
            case _:
                print("You have entered an invalid option")


    except ValueError:
        print("You have entered an invalid number")