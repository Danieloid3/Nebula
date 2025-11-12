import random

rango1 = int(input("Ingrese el rango inferior para adivinar: "))
rango2 = int(input("Ingrese el rango superior para adivinar: "))

num = random.randint(rango1, rango2)
adivina = int
while adivina != num:
    adivina = int(input(f"Adivina el número entre el rango {rango1}, {rango2}!!!: "))
    if adivina >= rango1 and adivina <= rango2:
        if adivina == num:
            print(f"Has adivinado, el número correcto es {num} ")
        elif adivina > num:
            print(f"Es un número más pequeño")
        else:
            print(f"Es un número más grande")
    else:
        print("Ese número está fuera del rango")