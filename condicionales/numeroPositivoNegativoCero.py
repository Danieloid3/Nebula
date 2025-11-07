print("Este programa determina si un número es positivo, negativo o cero.")

number = int(input("Ingrese un número: "))

if number > 0 :
    print(f"{number} es un número positivo.")
elif number < 0 :
    print(f"{number} es un número negativo.")
else :
    print("El número es cero.")