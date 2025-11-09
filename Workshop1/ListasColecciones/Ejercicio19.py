frutas = []
add = ""
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