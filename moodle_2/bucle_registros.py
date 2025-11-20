print("MENU DE REGISTRO:")  # Menú principal
print("1.Nombre.")  # Opción nombre
print("2.Precio.")  # Opción precio
print("3.Cantidad.")  # Opción cantidad
print("4.Salir.")  # Salida

nombre=""  # Guarda nombre
precio=0.0  # Guarda precio
cantidad=0  # Guarda cantidad

while True:  # Bucle principal
    pregunta=(input("Indica un numero para ingresar a las opciones o salir: "))  # Solicita opción
    inventario=[]  # Lista del inventario (reiniciada cada ciclo)

    if pregunta =="1":
        print("Has ingresado a la seccion del nombre")
        nombre=str(input("Ingresa el nombre: "))  # Guarda nombre

    elif pregunta =="2":
        print("Has ingresado a la seccion del precio")
        precio=float(input("Ingresa el precio: "))  # Guarda precio

    elif pregunta =="3":
        print("Has ingresado a la seccion del cantidad")
        cantidad=int(input("Ingresa el cantidad: "))  # Guarda cantidad  

    else:
        print("Has salido del menu de registro. Suerte.")  # Fin
        break

    producto={"Nombre": nombre, "Precio": precio, "Cantidad": cantidad}  # Crea producto
    inventario.append(producto)  # Lo agrega al inventario

    print(producto)  # Muestra producto
