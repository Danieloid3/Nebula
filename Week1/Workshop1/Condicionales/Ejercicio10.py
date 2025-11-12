while True:
    try:
        print("----MENÚ----")
        print("1. Additon")
        print("2. Substraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Exit")
        option = input("Choose an option: ")

        match option:
            case "1":
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                addition = num1 + num2
                print("El resultado es: ", addition)
            case "2":
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                substraction = num1 - num2
                print("El resultado es: ", substraction)
            case "3":
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                multiplication = num1 * num2
                print("El resultado es: ", multiplication)
            case "4":
                num1 = int(input("Ingrese el primer numero: "))
                num2 = int(input("Ingrese el segundo numero: "))
                division = num1 / num2
                print("El resultado es: ", division)
            case "5":
                print("Exiting...")
                break
            case _:
                print("You have entered an invalid option")
    except ValueError:
        print("Invalid number")
        continue