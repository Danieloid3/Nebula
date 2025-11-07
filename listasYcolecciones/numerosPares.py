numbers = list(map(int, input("Ingresa números separados por comas: ").split(",")))
pair = []

for number in numbers:
    if number % 2 == 0:
        pair.append(number)

if pair:
    print("Números pares encontrados:", pair)
else:
    print("No se encontraron números pares.")