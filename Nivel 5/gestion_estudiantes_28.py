seccion=(input("Ingresa tu grupo estudiantil: "))

hamilton=["Salva","Gabriela","Mateo","Natasha","Jose"]
tesla=["Mariana","Victor","Randolph","Hannan","Ronald","Alex"]

if seccion.lower()== "hamilton":
    print("Ingresaste a la base de datos estudiantil de hamilton: ", hamilton)

elif seccion.lower()== "tesla":
        print("Ingresaste a la base de datos estudiantil de tesla: ", tesla)

else:
    print("No existe ese clan")    

promedio1 = len(hamilton) 


promedio2 = len(tesla) 

saber_promedio=(input("Ingresa (promedio1) si quieres saber el promedio de hamilton \n ingresa (promedio2) si quieres saber el promedio de tesla: "))

if saber_promedio.lower()=="promedio1":
        print("Esta es la cantidad de estudiante que hay en el clan hamilton: ",promedio1)

elif saber_promedio.lower()== "promedio2":
    print("Esta es la cantidad de estudiante que hay en el clan tesla: ",promedio2)

cantidad=(input("Quieres saber la cantidad de estudiantes que hay en los dos clanesdi (si): "))   

promedio3=(promedio1)+(promedio2)

print(f"Hay en total entre los dos clanes {promedio3} estudiantes." )

