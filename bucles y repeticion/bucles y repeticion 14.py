#pedimos hast que numero queremos sumar
numero=int(input("introduce el numero hasta donde quieres sumar "))
#declaramos la variable y el valor
suma=0
#declaramos el rango sumando uno para conincidir con lo ingresado con el usuario
for i in range (1, numero+1):
    #declaramos el valor de suma y sumamos junto con el rango de i
    suma +=i
    #imprimimos el resultado
    print(suma)
