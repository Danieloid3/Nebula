numeros = input("ingresa los numeros separados por una coma ")

n1=[int(n2) for n2 in numeros.split(",")]
n3= [n4 for n4 in n1 if n4 % 2 == 0]

print("los numeros pares son", n3)
