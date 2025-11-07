numero=0

while True:
  numero_ingresado=int(input("ingresar un numero: "))

  if numero_ingresado ==0:
    print(f"Resultado_final: {numero}")
    break
  numero= numero+numero_ingresado    