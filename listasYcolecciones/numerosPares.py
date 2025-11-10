#Solicitar al usuario una lista de números separados por comas
numbers = list(map(int, input("Ingresa números separados por comas: ").split(",")))

#Encontrar y mostrar los números pares en la lista
pair = []

for number in numbers:
    if number % 2 == 0:
        pair.append(number)

if pair:
    print("Números pares encontrados:", pair)
else:
    print("No se encontraron números pares.")