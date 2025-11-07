#creamos las variables de los numeros y los signos
n1=float(input("ingrese el primer numero "))
signo=input("ingrese la operacion ")
n2=float(input("ingrese el segundo numero "))
#condicionamos que en la variable signo solo acepte los signos de operaciones basicos y en el mismo print realizamos la operacion
if signo == "+":
    print("el resultado de la suma es", n1+n2)
elif signo =="-":
    print("el resultado de la resta es", n1-n2)
elif signo == "*":
    print("el resultado de la multiplicaion es", n1*n2)
elif signo == "/":
    print("el resultado de la division es", n1/n2)
else:
    print("la operacion ingresada no es valida intenta otra vez")
