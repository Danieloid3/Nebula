numbers_list = list(map(int, input("Ingresa números separados por comas: ").split(",")))
print(numbers_list)

average = sum(numbers_list) / len(numbers_list)

print(f"El promedio de la lista es: {average}")