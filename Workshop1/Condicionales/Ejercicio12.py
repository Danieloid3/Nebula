num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))
num3 = int(input("Ingrese el tercer número: "))

nums = [num1, num2, num3]
mayor = 0
menor = num1
for n in nums:
    if n > mayor:
        mayor = n

for n in nums:
    if n < menor:
        menor = n

print(menor, mayor)

