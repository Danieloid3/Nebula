notas = list(map(float, input("Ingrese las calificaciones separadas por coma y al finalizar presiona enter: ").split(","))) 
print(f"Notas ingresadas: {notas}") 


for nota in notas: 
    if nota < 0 or nota > 5:
         print(f"La calificación {nota} no es válida, ingrese una calificación entre 0 y 5") 

if all(nota >= 0 and nota <= 5 for nota in notas) : 
    average_notas = sum(notas) / len(notas) 

    if average_notas < 3:
        print(f"El promedio de las calificaciones es: {average_notas}, ¡REPROBASTE!")
    else:
        print(f"El promedio de las calificaciones es: {average_notas}, ¡APROBASTE!")