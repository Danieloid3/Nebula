

frutas = ["mango", "pera", "limón"]

def agregaFrutas():
    flag = True
    while flag == True:
        add = ""
        frutas.append(input("Ingrese la fruta: "))
        while not (add == "y" or add == "n"):
            add = input("Deseas agregar otra fruta? (y/n): ").strip().lower()
            if add == "n":
                flag = False
            else:
                flag = True

    print(frutas)

def eliminaFrutas():
    flag = True
    while flag == True:
        add = ""
        fruta = (input("Ingrese la fruta: "))
        if fruta in frutas:
            frutas.remove(fruta)
            while not (add == "y" or add == "n"):
                add = input("Deseas eliminar otra fruta? (y/n): ").strip().lower()
                if add == "n":
                    flag = False
                else:
                    flag = True
        else:
            print("La fruta ingresada no se encuentra en la lista")
    print(frutas)

while True:
    try:
        print("----MENÚ----")
        print("1. Agregar frutas")
        print("2. ELiminar frutas")
        print("3. Ver lista")
        print("4. Salir")

        opcion= input("Escoge una opción: ")

        match opcion:
            case "1":
                agregaFrutas()
            case "2":
                eliminaFrutas()
            case "3":
                print(frutas)
            case "4":
                print("Saliendo...")
                break

    except ValueError:
        print("Valor invalido")


