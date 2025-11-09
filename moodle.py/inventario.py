#NOMBRE DEL PRODUCTO-PIDE DATOS CON INPUT
nombre=input("ingrese el nombre del producto: ")
precio=input("ingrece el precio: ")

#ISNUMERIC HACE LA VALIDACION DE QUE SEA SOLO NUMEROS
while not precio.isnumeric():
    print("--ingrese solo numeros:-- ")
    precio=input("Ingrese solo precio: ")

#LO CONVIERTO A FLOAT ES DECIR PARA QUE SE PUEDA USAR DECIMAL
precio2=float(precio)
    

#VUELVO A VALIDAR CON ISNUMERIC
cantidad = input("ingrese la cantidad: ")
while not cantidad.isnumeric():
    print("--solo numeros-- ")
    cantidad=input("ingrese la cantidad: ")

#CONVERTIR A INT PARA QUE FUNCIONEN ENTEROS SIN DECIMAL    
cantidad1=int(cantidad)
    

costo_total=int(precio2*cantidad1)
print(f"producto: {nombre} precio: {precio2} cantidad: {cantidad1} total: {costo_total}")