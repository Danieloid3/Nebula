from crud import CRUD 

crud= CRUD()
archivo = "datos.csv"
crud.crear_archivo(archivo)

while True:
        
    print("Menu")
    print("1.Registrar Productos")
    print("2.Editar")
    print("3.Eliminar")
    print("4.Salir")

    menu=(input("Ingresa la opcion: "))


    match menu:
        case "1":
            nombre=(())
            edad=(())

            id_creado = crud.crear()
            print()