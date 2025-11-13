

def eliminar_user_id(informacion_paciente):
    id_eliminar = input("Ingresa el ID del usuario que quieres eliminar: ").strip()
   

    for usuario in informacion_paciente:
        if (usuario["id"]) == int(id_eliminar):

            confirmar=""
            while confirmar != "aceptar" and confirmar != "cancelar":
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
        else:
            print("No se encontró ningún usuario con ese ID.")




def eliminar_user_name(informacion_paciente):
    nombre_eliminar = input("Ingresa el nombre del usuario que quieres eliminar: ").strip().lower()
    

    for usuario1 in informacion_paciente:
        if usuario1["nombre"].strip().lower()==  nombre_eliminar: 

            confirmar1=""
            while confirmar1 != "aceptar" and confirmar1 != "cancelar":
                confirmar1=input(f"Deseas eliminar el usuario? Aceptar/Cancelar: {usuario1 ['nombre']}? ").lower()
                if confirmar1 == "aceptar":
                    informacion_paciente.remove(usuario1)
                    print(f"Has aceptado, el usuario {usuario1["nombre"]} ha sido eliminado.")
                    print("Lista actualizada de informacion_paciente:", informacion_paciente)
                elif confirmar1 == "cancelar":
                    print("Has cancelado, el usuario no ha sido eliminado.")
                else:
                    print("Ingresa el valor correcto.")
                    continue
                return 
            break  
        
    print("No se encontró ningún usuario con ese nombre.")




              


    
def menu_eliminar(informacion_paciente):
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
            eliminar_user_id(informacion_paciente)

        elif eleccion == 2:
            eliminar_user_name(informacion_paciente)
            

        else:
            print("Has salido del menu")
            break           

