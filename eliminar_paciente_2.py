informacion_paciente = [
    {"id": "1", "nombre": "Salvador"},
    {"id": "2", "nombre": "María"},
    {"id": "3", "nombre": "Carlos"}
]

def eliminar_user():
    id_eliminar = input("Ingresa el ID del usuario que quieres eliminar: ")
    nombre_eliminar = input("Ingresa el ID del usuario que quieres eliminar: ")

    for usuario in informacion_paciente:
        if usuario["id"] == id_eliminar or usuario["nombre"].lower() == nombre_eliminar:
            confirmacion = input(f"Deseas eliminar el usuario? Copie aceptar o cancelar: {usuario ['nombre']}? ").lower()
            
            if confirmacion == "aceptar":
                informacion_paciente.remove(usuario)
                print(f"Has aceptado, el usuario {usuario["nombre"]} ha sido eliminado.")
            else:
                print("Has cancelado, el usuario no ha sido eliminado.")
            return  
    
    print("No se encontró ningún usuario con ese ID.")

eliminar_user()
print("Lista actualizada de informacion_paciente:", informacion_paciente)
