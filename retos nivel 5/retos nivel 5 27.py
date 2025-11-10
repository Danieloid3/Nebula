clave=2846
saldo=1000000

intentos=0

while intentos <3:
    c1=int(input("ingresa tu clave "))
    if clave == c1:
        print("bienvenido")
        break
    else:
        intentos+=1
        print("incorrecto intenta otra vez")
else:
    print("numeros de intentos superados")

saldo2=int(input("cuanto saldo quieres retirar? "))
if saldo2 > saldo:
    print("saldo insuficiente")
else:
    print("tu saldo restanta es", saldo-saldo2)
