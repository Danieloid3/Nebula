suma_total = 0

# Bucle para sumar números hasta que se ingrese 0
while True:
    suma = float(input("Ingrese un numero para sumar (Presiona 0 para terminar): "))
    suma_total += suma
    
    if suma == 0:
        print(f"la suma de los datos ingresados es: {suma_total}")
        break   