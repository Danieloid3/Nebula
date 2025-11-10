import math

# Función para validar que el usuario ingrese un número

def pedir_numero(mensaje):
    while True:
        valor = input(mensaje)

        # Verifica si lo ingresado puede convertirse a float
        try:
            valor = float(valor)
            return valor
        except ValueError:
            print("Entrada inválida. Solo se permiten números.\n")

# Funciones de operaciones
def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: no se puede dividir entre 0"
    return a / b

def potencia(a, b):
    return a ** b

def raiz(a):
    if a < 0:
        return "Error: no existe raíz real para números negativos"
    return math.sqrt(a)

# Menú principal
print("--- CALCULADORA AVANZADA ---")

while True:
    print("\nSeleccione una opción: "
    "\n1. Sumar"
    "\n2. Restar"
    "\n3. Multiplicar"
    "\n4. Dividir"
    "\n5. Potencia"
    "\n6. Raíz cuadrada" 
    "\n7. Salir")

    opcion = input("Opción: ")

    # Salir del programa
    if opcion == "7":
        print("Saliendo... ¡Hasta luego!")
        break

    # Opción de raíz cuadrada (solo un número)
    if opcion == "6":
        num = pedir_numero("Ingrese el número: ")
        print("Resultado:", raiz(num))
        continue

    # Para el resto de operaciones se piden dos números, con validación
    a = pedir_numero("Ingrese el primer número: ")
    b = pedir_numero("Ingrese el segundo número: ")

    if opcion == "1":
        print("Resultado:", sumar(a, b))

    elif opcion == "2":
        print("Resultado:", restar(a, b))

    elif opcion == "3":
        print("Resultado:", multiplicar(a, b))

    elif opcion == "4":
        print("Resultado:", dividir(a, b))

    elif opcion == "5":
        print("Resultado:", potencia(a, b))

    else:
        print("Opción inválida.")