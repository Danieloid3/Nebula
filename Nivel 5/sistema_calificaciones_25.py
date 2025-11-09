nombre=(input("ingresa tu nombre: "))

lista=([1.0,2.0,3.0,5.0,5.0])

print(f"Aqui estan en tus notas {nombre}: {lista}")

promedio=(input("Vuelve a ingresar tu nombre para saber tu promedio: "))

promedio1= sum(lista)/ len(lista)

print(f"Tu promedio es: {promedio1}")


if promedio1 >= 3.0:
    print("Ganaste la materia, has pasado el año. ¡Felicidades!")

else:
    print("Perdiste el año.")    