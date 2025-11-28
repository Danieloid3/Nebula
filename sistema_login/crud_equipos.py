equipos = []

def listar_equipos():
    if not equipos:
        print("No hay equipos registrados. \n ")
        return


    print("\n--- Lista de Equipos ---")
    for i, equipo in enumerate(equipos):
        print(f"{i+1}. {equipo['nombre']} - {equipo['entrenador']} - {equipo['trofeos']}\n")

def crear_equipos():
    while True:
        try:
            nombre = input("Ingresa nombre del equipo: ")
            entrenador = input("Ingresa el nombre del entrenador: ")
            trofeos = int(input("Ingresa los trofeos ganados: "))

            equipos.append({
                "nombre": nombre,
                "entrenador": entrenador,
                "trofeos": trofeos
            })
            print("\n Equipo creado correctamente \n ")
            break
        except ValueError:
            print("No se puede saltar las opciones, intentalo de nuevo...\n ")
            

def actualizar_equipos():
    if not equipos:
        print("No hay equipos registrados. \n")
        return

    listar_equipos()
    select_option=int(input(f"\n Selecciona el equipo a actualizar: ")) -1
    if 0 <= select_option <len(equipos):
        equipos[select_option]["nombre"] = (input("Nuevo nombre: "))
        equipos[select_option]["entrenador"] = (input("Nuevo entrenador: "))
        equipos[select_option]["trofeos"] = int(input("Nueva cantidad de trofeos: "))
        print("\n Lista actualizada:")

    else:
        print("opcion invalida")

def eliminar_equipo():
    if not equipos:
        print("No hay equipos registrados. \n")
        return

    while True:   
            listar_equipos()
            option_deleted = int(input("Selecciona el equipo a eliminar: ")) - 1

            if 0 <= option_deleted < len(equipos):
                equipos.pop(option_deleted)
                print("Equipo eliminado")
                print("\n Lista de equipos actualizada")
                listar_equipos()
                break
            else:
                print("\n Selección no válida, por favor ingrese otra vez la eleccion \n")
