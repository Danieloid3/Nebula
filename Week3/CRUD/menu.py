from CRUD import CRUD

crud = CRUD()
archivo = "registros.json"

while True:
    #try:
    print("----MENU-----")
    print("1. Agregar Datos")
    print("2. Listar Datos")
    print("3. Salir")
    option = input("Seleccione una opcion: ")
    match option:
        case "1":
            nombre = input("Ingrese nombre: ")
            edad = input("Ingrese edad: ")
            crud.create_users(archivo,{"nombre": nombre, "edad": edad})

    #except(ValueError):
        #print("Error")









