import random 

numero_secreto= random.randint(1,5)

adivina=int

while adivina != numero_secreto: 
    adivina=int(input("Adivina el numero del 1 al 5: "))
    if  adivina != numero_secreto:
        print("no es el numero secreto, intentalo de nuevo: ")

    else:
        print(f"adivinaste el numero: {numero_secreto}")