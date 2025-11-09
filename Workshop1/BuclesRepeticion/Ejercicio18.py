sum = 0
num = int
while num != 0:
    num = int(input("Ingrese el número a sumar o 0 para terminar y obtener el total: "))
    if num != 0:
        sum += num
    else:
        print(f"La suma total es: {sum}")
