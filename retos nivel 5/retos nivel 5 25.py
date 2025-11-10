notas=input("dime las notas separadas por una coma ")
n2=[int(n1) for n1 in notas.split(",")]

promedio=sum(n2)/ len(n2)

print("tu promedio es", promedio)

if promedio >10 or promedio < 0:
    print("el promedio no es valido")
elif promedio >= 9:
    print("excelente")
elif promedio >=6:
    print("aprobaste")
else:
    ("reprobaste")
