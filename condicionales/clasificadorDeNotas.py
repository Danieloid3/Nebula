# Clasificador de notas de estudiantes en rango de 0 a 5
print("Clasificador de notas de estudiantes en rango de 0 a 5")
qualification = float(input("Ingrese la primer nota: "))
qualification2 = float(input("Ingrese la segunda nota: "))
qualification3 = float(input("Ingrese la tercer nota: "))
qualification4 = float(input("Ingrese la cuarta nota: "))

# Calcular el promedio de las notas
average = (qualification + qualification2 + qualification3 + qualification4) / 4

# Clasificar el promedio según los criterios establecidos
if average == 5.0 :
    print(f"Excelente el estudiante aprobó con una nota de: {average}")
elif average >= 3.0 and average <= 4.9:
    print(f"El estudiante es Aprobado con una nota de: {average}")
elif average < 3.0 and average >= 0 :
    print(f"El estudiante es Reprobado con una nota de: {average}")
else :
    print("Error: La nota ingresada no se encuentra dentro del rango permitido.")