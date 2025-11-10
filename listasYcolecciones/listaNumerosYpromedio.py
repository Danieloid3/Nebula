#Solicitar al usuario una lista de números separados por comas
numbers_list = list(map(int, input("Ingresa números separados por comas: ").split(",")))
print(numbers_list)

#Calcular el promedio de los números en la lista
average = sum(numbers_list) / len(numbers_list)

#Mostrar el promedio
print(f"El promedio de la lista es: {average}")