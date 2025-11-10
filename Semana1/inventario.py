#Solicitar datos al usuario.

#Verificar que el nombre no esté vacío
while True: 
    nombre = input("Ingrese el nombre del producto: ")
    if nombre:
        break
    print("El nombre del producto no puede estar vacío. Por favor, intente de nuevo.")

#Verificar que el precio y la cantidad sean números válidos, 
while True:
    try:
        precio = float(input("Ingrese el precio del producto: "))
        break
    except ValueError: #Permite manejar el error en caso de que el usuario ingrese un valor no numérico
        print("Por favor, ingrese un valor numérico para el precio")

while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break
    except ValueError: #Permite manejar el error en caso de que el usuario ingrese un valor no entero
        print("Por favor, ingrese un valor entero para la cantidad")

#Calcular el costo total del producto (precio * cantidad) y mostrar toda la información obtenida
costo_total = precio * cantidad
print(f"el Costo total de {nombre} es: {costo_total}")
print(f"Nombre del producto: {nombre} | Precio unitario: {precio} | Cantidad: {cantidad} | Costo total calculado: {costo_total} ")          


#El algoritmo solicita al usuario el nombre, precio y cantidad de un producto, 
#para posteriormente calcular el costo total del mismo, y a su vez mostrar toda la información obtenida en consola.