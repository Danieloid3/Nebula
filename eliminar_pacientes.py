def eliminar_user():

    eliminar_user=(input("Ingresa el ID del usuario que quiere eliminar: "))

    confirmacion=(input("Deseas eliminar el usuario? Copie aceptar o cancelar: ")).lower()
    
    if confirmacion == "aceptar":
        print(f"Has aceptado, el usuario a sido eliminado {eliminar_user}")
        
    else:
        print("Has cancelado, el usuario no ha sido eliminado")
        
eliminar_user()


