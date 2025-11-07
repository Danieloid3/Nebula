#declaramos la variable y pedimos el valor al usuario
numero=int(input("ingresa el numero "))
#ponemos el rango de hasta donde queremos que se haga la tabla
for i in range (1,11):
    #multiplicamos lo ingresado por el usuario y multiplicado por el rango e imprimimos el resultado
    total= numero*i
    print(f"{numero} x {i} = {total}")