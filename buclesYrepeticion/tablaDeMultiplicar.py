multiplicar= int(input("Que tabla de multiplicar desea conocer: "))

# Realizar la tabla de multiplicar que el usuario solicite en un rango del 1 al 10
for number in range (1,10 + 1) :
    total = multiplicar * number
    print(f"{multiplicar} x {number} = {total}")