import random # importa el módulo para poder utilizar sus funciones

print("¡Bienvenido al juego de adivina el número!")
print("Estoy pensando en un número entre 1 y 10.")      

guess = int(input("Adivina el número: "))

random_number = random.randint(1,10) #usa la función randint del módulo random para generar un número aleatorio entre 1 y 10

#Compara el número ingresado por el usuario con el número aleatorio generado
if guess == random_number:
    print(f"El número que seleccionaste es: {guess} y el número elegido es: {random_number}, ¡GANASTE!")
else:
    print(f"El número que seleccionaste es: {guess} y el número elegido es: {random_number}, ¡PERDISTE!")
