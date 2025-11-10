# Comparador de tres números para determinar el mayor y el menor
print("Ingrese tres numero para validar el mayor y menor de los mismos")
number1 = float(input("Ingrese el primer número: "))
number2 = float(input("Ingrese el segundo número: "))
number3 = float(input("Ingrese el tercer número: "))

# Comparar los números y determinar el mayor y el menor según las condiciones
if number1 < number2 and number2 < number3:
    print(f"El numero menor es {number1} y el número mayor es {number3}")
elif number1 < number3 and number3 < number2:
    print(f"El numero menor es {number1} y el número mayor es {number2}")
elif number2 < number1 and number1 < number3:
    print(f"El numero menor es {number2} y el número mayor es {number3}")
elif number2 < number3 and number3 < number1:       
    print(f"El numero menor es {number2} y el número mayor es {number1}")
elif number3 < number1 and number1 < number2:
    print(f"El numero menor es {number3} y el número mayor es {number2}")
else:
    print(f"El numero menor es {number3} y el número mayor es {number1}")   
