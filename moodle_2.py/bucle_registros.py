print("MENU DE REGISTRO:")
print("1.Nombre.")
print("2.Precio.")
print("3.Cantidad.")
print("4.Salir.")

nombre=""
precio=0.0
cantidad=0


while True:
    pregunta=(input("Indica un numero para ingresar a las opciones o salir: "))
    inventario=[]

    if pregunta =="1":
        print("Has ingresado a la seccion del nombre")
        nombre=str(input("Ingresa el nombre: "))

    elif pregunta =="2":
        print("Has ingresado a la seccion del precio")
        precio=float(input("Ingresa el precio: "))

    elif pregunta =="3":
        print("Has ingresado a la seccion del cantidad")
        cantidad=int(input("Ingresa el cantidad: "))   

    else:
        print("Has salido del menu de registro. Suerte.")
        break


    producto={"Nombre": nombre, "Precio": precio, "Cantidad": cantidad} 
    inventario.append(producto)

    print(producto)

        