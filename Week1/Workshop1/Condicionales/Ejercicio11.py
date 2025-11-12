add = ""
flag = True
while flag:
    try:
        grade = int(input("Grade: "))
        if grade >= 0 and grade <= 5:
            if grade >= 0 and grade <= 2.9:
                print("Reprobado")
            elif grade >= 3 and grade <= 3.9 :
                print("Aprobado")
            else:
                print("Excelente")
        while not (add == "y" or add == "n"):
            add = input("Verificar otra nota? (y/n): ").strip().lower()
            if add == "n":
                flag = False
            else:
                flag = True

    except ValueError:
        print("Ingrese un numero valido")