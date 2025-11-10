print("---Bienvenido a la calculadora básica---")

# Solicitar al usuario los números y la operación a realizar
number1 = float(input("Ingresa un número: "))
operation = input("Elige la operación que deseas realizar: + , - , * , / ")
number2 = float(input("Ingresa otro número: "))

# Realizar las operaciones
resultado_sumar = number1 + number2
resultado_restar = number1 - number2
resultado_multiplicar = number1 * number2
resultado_dividir = number1 / number2

# Mostrar el resultado según la operación elegida
if operation == "+" :
    print(f"La suma de {number1} + {number2} es: {resultado_sumar}")
elif operation == "-" :
    print(f"La resta de {number1} - {number2} es: {resultado_restar}")
elif operation == "*" :
    print(f"La multiplicación de {number1} * {number2} es: {resultado_multiplicar}")
elif operation == "/" :
    if number2 != 0 :
        print(f"La división de {number1} / {number2} es: {resultado_dividir}")
    else :
        print("Error: No se puede dividir entre cero.")
else :
    print("Operación no válida. Por favor, elige una de las siguientes: + , - , * , /")     






