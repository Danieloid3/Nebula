#creamos la variablede la nota
nota=float(input("ingresa tu nota "))
#indicamos en las variables los niveles de calificacion y en que rango aplican
if nota >10 or nota <0:
    print("no es nota valida")
elif nota >= 9:
    print("excelente")
elif nota >= 6:
    print("aprobaste")
else:
    print("reprobastre")