def sumar(a, b):  # función para sumar
    return a + b

def restar(a, b):  # función para restar
    return a - b

def multiplicar(a, b):  # función para multiplicar
    return a * b

def dividir(a, b):  # función para dividir
    if b != 0:  # evita dividir entre cero
        return a / b
    else:
        return "Error: no se puede dividir entre 0"

print("📘 Calculadora avanzada")  # título del programa
print("Operaciones disponibles:")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")
print("5. Salir")

while True:  # bucle que mantiene la calculadora activa
    opcion = input("\nElige una opción (1-5): ")

    if opcion == "5":  # si elige salir
        print("Saliendo de la calculadora...")
        break  # rompe el bucle

    num1 = float(input("Ingresa el primer número: "))  # pide el primer número
    num2 = float(input("Ingresa el segundo número: "))  # pide el segundo número

    # según la opción elegida, hace la operación
    if opcion == "1":
        resultado = sumar(num1, num2)
    elif opcion == "2":
        resultado = restar(num1, num2)
    elif opcion == "3":
        resultado = multiplicar(num1, num2)
    elif opcion == "4":
        resultado = dividir(num1, num2)
    else:
        print("❌ Opción inválida, intenta de nuevo.")
        continue  # vuelve al menú

    print(f"✅ El resultado es: {resultado}")  # muestra el resultado
