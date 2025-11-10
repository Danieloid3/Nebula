print("Este programa determina si un número es par o impar.")

# Solicitar al usuario que ingrese un número entero
number = int(input("Por favor, ingresa un número entero: "))

# Determinar si el número es par o impar utilizando el operador módulo
if number % 2 == 0 :
    print(f"El número {number} es par")
else :
    print(f"El número {number} es impar")