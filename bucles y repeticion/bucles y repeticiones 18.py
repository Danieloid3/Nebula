suma=0
desde=1

while desde != 0:
    numero=int(input("ingresa un numero para sumar(pon 0 para parar) "))
    desde=int(numero)
    if desde != 0:
        suma+=desde
        print("la suma actual es", suma)