n1=input("ingresa la lista de numeros separados por una coma ")

n2=[float(num) for num in n1.split(",")]

promedio= sum(n2)/ len(n2)

print("el promedio es", promedio)
