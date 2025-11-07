num1=float(input("Ingresa el primer numero para calcular: "))
num2=float(input("Ingresa el segundo numero para calcular: "))

operacion=(input("--Ingresa la operación-- +|-|*|/:  "))

if operacion == "+":
    resultado=num1+num2
    print(f"El resultado de la suma es: {resultado}")

elif  operacion == "-":
    resultado=num1-num2
    print(f"El resultado de la resta es: {resultado}")   

elif operacion == "*":
    resultado=num1*num2
    print(f"El resultado de la multiplicacion es: {resultado}")    

elif operacion == "/":
    
    if num2 ==0:
        print("Error: No se puede dividir entre cero. ")  
    else:
        resultado=num1/num2
        print(f"El resultado de la multiplicacion es: {resultado}")      
    
   
