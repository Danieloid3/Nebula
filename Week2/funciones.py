# def saludar(nombre, edad):
#     print(f"Hola, {nombre}, tu edad es {edad}!")
#
# saludar(input("Introduce tu nombre: "), input("Introduce tu edad: "))

# def multiplicar(a,b):
#     return a*b
#
# multiplicacion = multiplicar(int(input("ingrese un numero: ")), int(input("ingrese otro numero: ")))
#
# print(multiplicacion)

def parimpar(a,b):
    if a%2==0 and b%2==0:
        return f"{a} Es par y {b} Es par"
    elif a%2==0 and b%2!=0:
        return f"{a} Es par y {b} Es impar"
    elif a%2!=0 and b%2==0:
        return f"{a} Es impar y {b} Es par"
    else:
        return f"{a} Es impar y {b} Es impar"


par= parimpar(int(input("Ingrese un numero: ")), int(input("Ingrese otro numero: ")))
print(par)

print ("Fin del programa")

