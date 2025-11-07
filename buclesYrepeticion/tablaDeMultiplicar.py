multiplicar= int(input("Que tabla de multiplicar desea conocer: "))

for number in range (1,10 + 1) :
    total = multiplicar * number
    print(f"{multiplicar} x {number} = {total}")