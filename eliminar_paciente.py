informacion_paciente = [
    {"id": "1", "nombre": "Salvador"},
    {"id": "2", "nombre": "Maria"},
    {"id": "3", "nombre": "Carlos"}
]

def eliminar_user_id():
    id_eliminar = input("Ingresa el ID del usuario que quieres eliminar: ").strip()
   

    for usuario in informacion_paciente:
        if usuario["id"] == id_eliminar: 
            confirmacion = input(f"Deseas eliminar el usuario? Aceptar/Cancelar: {usuario ['nombre']}? ").lower()
            confirmar=""
            while confirmar != "Aceptar" and confirmar != "Cancelar":
                confirmar=input(f"Deseas eliminar el usuario? Aceptar/Cancelar: {usuario ['nombre']}? ").lower()
                if confirmar == "aceptar":
                    informacion_paciente.remove(usuario)
                    print(f"Has aceptado, el usuario {usuario["nombre"]} ha sido eliminado.")
                    print("Lista actualizada de informacion_paciente:", informacion_paciente)
                elif confirmar == "cancelar":
                    print("Has cancelado, el usuario no ha sido eliminado.")
                else:
                    print("Ingresa el valor correcto.")
                    continue
                return 
            break 
    
    print("No se encontró ningún usuario con ese ID.")




def eliminar_user_name():
    nombre_eliminar = input("Ingresa el nombre del usuario que quieres eliminar: ").strip().lower()
    

    for usuario1 in informacion_paciente:
        if usuario1["nombre"].strip().lower()==  nombre_eliminar: 
            confirmacion1 = input(f"Deseas eliminar el usuario? Aceptar/Cancelar: {usuario1 ['nombre']}? ").lower()
            confirmar1=""
            while confirmar1 != "Aceptar" and confirmar1 != "Cancelar":
                confirmar=input(f"Deseas eliminar el usuario? Aceptar/Cancelar: {usuario1 ['nombre']}? ").lower()
                if confirmar == "aceptar":
                    informacion_paciente.remove(usuario1)
                    print(f"Has aceptado, el usuario {usuario1["nombre"]} ha sido eliminado.")
                    print("Lista actualizada de informacion_paciente:", informacion_paciente)
                elif confirmar == "cancelar":
                    print("Has cancelado, el usuario no ha sido eliminado.")
                else:
                    print("Ingresa el valor correcto.")
                    continue
                return 
            break  
        
    print("No se encontró ningún usuario con ese nombre.")




              


    
def menu_eliminar():
    while True:
        print("""Menu Eleccion A Cual Eliminar (Eliminar por ID/Eliminar por nombre)
              1.Eliminar por ID
              2.Eliminar por nombre
              3.Salir""")
        try:
            eleccion = int(input("Selecciona una opcion: "))
        except ValueError:
                print("Ingresa unicamente un numero de la lista")
                continue

        if eleccion == 1:
            eliminar_user_id()

        elif eleccion == 2:
            eliminar_user_name()
            

        else:
            print("Has salido del menu")
            break           

menu_eliminar()