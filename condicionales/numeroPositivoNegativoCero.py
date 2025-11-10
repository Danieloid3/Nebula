print("Este programa determina si un número es positivo, negativo o cero.")

# Solicitar al usuario que ingrese un número
number = int(input("Ingrese un número: "))

# Determinar si el número es positivo, negativo o cero
if number > 0 :
    print(f"{number} es un número positivo.")
elif number < 0 :
    print(f"{number} es un número negativo.")
else :
    print("El número es cero.")