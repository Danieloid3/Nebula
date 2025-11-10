while True:
    
        producto=str(input("que producto quieres agregar al carrito? "))
        if producto.isalpha():
         break
        else:
             print("no es valido lo ingresado intenta nuevamente")

while True:
    try:
            precio=float(input("que precio tiene el producto? "))
            break
    except ValueError: str
    print("eso no es un valor valido para el precio intenta nuevamente")

while True:
     try:
          cantidad=int(input("cuantas unidades de producto estas llevando? "))
          break
     except ValueError: str
     print("eso no es un valor valido para la unidad intenta nuevamente")

costo_total=float(precio*cantidad)

print(f"su producto {producto} tiene un valor unitario de {precio} y al solicitar {cantidad} de unidades tienen un costo de {costo_total}")