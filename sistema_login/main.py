from login import login_user
from crud_equipos import crear_equipos, listar_equipos, actualizar_equipos

def main():
    while True:
        print ("--1.Crear equipos--")
        print ("--2.Listar equipos--")
        print ("--3.Actualizar equipos existentes--")
        print ("--4.Eliminar equipos--")
        print ("--0.Salir--")
        
        option=(input("Ingrese una opcion: "))

        match option:
            case "1":
                print("\n-- Ingresaste a la seccion de crear un equipo --")
                crear_equipos()
            case "2":
                print("\n-- Ingresaste a la lista de equipos --")
                listar_equipos()
            case "3":
                print("\n-- Ingresaste a la seccion de actualizar equipos --")
                actualizar_equipos()
            case "4":
                print
            case "0":
                print
                break    
            case _:
                print

main()
login_user()