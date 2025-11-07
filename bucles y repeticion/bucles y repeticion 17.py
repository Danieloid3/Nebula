import random
numero=random.randint(1,10)
for i in range (3):
    while True:
        try:
            correcto=int(input("adivina el numero entre 1 y 10 "))
            
            if correcto == numero:
                print("correto acertaste")
                exit()
                break
            elif correcto < numero:
                print("sube mas")
                break
            elif correcto > numero:
                print("baja mas")
                break
        except ValueError:
            print("fallaste")
            break
else:
    print("el numero correcto era", numero)
        