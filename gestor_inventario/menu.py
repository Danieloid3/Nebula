def registrar_producto():
    nombre=str(input("ingresa el nombre del producto: "))
    precio=float(input("ingresa el precio: "))
    cantidad=int(input("ingresa la cantidad: "))
    
    registro.append()

def editar_producto():
    print
def eliminar_producto():
    print
def guardar_txt():
    print
def guardar_csv():
    print
def guardar_json():
    print




    while True:
        
        try:
            
            print("MENU")
            print("1.Registrar producto: ")
            print("2.Editar producto: ")
            print("3.Eliminar producto: ")
            print("4.Guardar txt: ")
            print("5.Guardar csv: ")
            print("6.Guardar json: ")
            print("7.Salir")  
            
            menu=(input("selecciona una opcion"))
            
            match menu: 
                case "1":
                    registrar_producto()
                case "2":
                    editar_producto()
                case "3":
                    eliminar_producto()
                case "4":
                    guardar_txt
                case "5":
                    guardar_csv
                case "6":
                    guardar_json
                    
            
        except ValueError:
            print()