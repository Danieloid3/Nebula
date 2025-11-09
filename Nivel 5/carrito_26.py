carrito=["inicio: "]


while True:
    producto=(input("Copia salir para terminar o\n Ingresa un producto para agregarlo al carrito: "))

    if producto.lower()=="salir":
        break
    carrito.append(producto)

    print("Aqui esta tu lista de productos: ", carrito)