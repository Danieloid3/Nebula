pacientes = {
    1: {
        "nombre": "sergio",
        "edad": 21,
        "genero": "masculino",
        "diagnostico": "tuberculosis",
        "historial": ["consulta general", "recoger medicina"]
    },
    2: {
        "nombre": "camila",
        "edad": 25,
        "genero": "femenino",
        "diagnostico": "asma",
        "historial": ["control medico", "examen respiratorio"]
    }
}

def mostrar_datos(usuario):
    print("DATOS DEL PACIENTE")
    for clave, valor in usuario.items():
        print(f"{clave.capitalize()}: {valor}")
def modificar_nombre(usuario):
    while True:
        try:
            nuevo_nombre = input("Ingresa el nuevo nombre: ")
            if not nuevo_nombre.isalpha():
                raise ValueError()
            print(f"Nombre anterior: {usuario['nombre']}")
            confirmar = input(f"¿Deseas cambiarlo por '{nuevo_nombre}'? (si/no): ").lower()
            if confirmar == "si":
                usuario["nombre"] = nuevo_nombre
                print("Nombre actualizado con exito.")
            elif confirmar == "no":
                print("Cambio cancelado.")
            else:
                print("Responde solo con 'si' o 'no'.")
                continue
            break
        except ValueError:
            print("Valor no válido para nombre.")

def modificar_edad(usuario):
    while True:
        try:
            nueva_edad = input("Ingresa la nueva edad: ")
            if not nueva_edad.isdigit():
                raise ValueError()
            print(f"Edad anterior: {usuario['edad']}")
            confirmar = input(f"¿Deseas cambiarla por '{nueva_edad}'? (si/no): ").lower()
            if confirmar == "si":
                usuario["edad"] = int(nueva_edad)
                print("Edad actualizada con exito.")
            elif confirmar == "no":
                print("Cambio cancelado.")
            else:
                print("Responde solo con 'si' o 'no'.")
                continue
            break
        except ValueError:
            print("Valor no válido para edad.")

def modificar_genero(usuario):
    while True:
        try:
            nuevo_genero = input("Ingresa el nuevo género: ")
            if not nuevo_genero.isalpha():
                raise ValueError()
            print(f"Genero anterior: {usuario['genero']}")
            confirmar = input(f"¿Deseas cambiarlo por '{nuevo_genero}'? (si/no): ").lower()
            if confirmar == "si":
                usuario["genero"] = nuevo_genero
                print("Genero actualizado con éxito.")
            elif confirmar == "no":
                print("Cambio cancelado.")
            else:
                print("Responde solo con 'si' o 'no'.")
                continue
            break
        except ValueError:
            print("Valor no válido para genero.")

def modificar_diagnostico(usuario):
    while True:
        try:
            nuevo_diag = input("Ingresa el nuevo diagnostico: ")
            if not nuevo_diag.isalpha():
                raise ValueError()
            print(f"Diagnostico anterior: {usuario['diagnostico']}")
            confirmar = input(f"¿Deseas cambiarlo por '{nuevo_diag}'? (si/no): ").lower()
            if confirmar == "si":
                usuario["diagnostico"] = nuevo_diag
                print("Diagnostico actualizado con exito.")
            elif confirmar == "no":
                print("Cambio cancelado.")
            else:
                print("Responde solo con 'si' o 'no'.")
                continue
            break
        except ValueError:
            print("Valor no valido para diagnostico.")

def agregar_historial(usuario):
    nuevo_evento = input("Agrega un nuevo evento al historial (deja vacio para cancelar): ")
    if nuevo_evento.strip() == "":
        print("No se agrego nada al historial.")
    else:
        usuario["historial"].append(nuevo_evento)
        print(f"Se agrego '{nuevo_evento}' al historial.")

def menu_usuario(usuario):
    while True:
        print("""
MENU DE MODIFICACION DE PACIENTES
1. Mostrar datos del paciente
2. Modificar nombre
3. Modificar edad
4. Modificar género
5. Modificar diagnóstico
6. Agregar nuevo evento al historial
7. Volver al menú principal
""")
        try:
            opcion = int(input("Selecciona una opcion: "))
        except ValueError:
            print("Ingresa un numero valido.")
            continue

        if opcion == 1:
            mostrar_datos(usuario)
        elif opcion == 2:
            modificar_nombre(usuario)
        elif opcion == 3:
            modificar_edad(usuario)
        elif opcion == 4:
            modificar_genero(usuario)
        elif opcion == 5:
            modificar_diagnostico(usuario)
        elif opcion == 6:
            agregar_historial(usuario)
        elif opcion == 7:
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

def menu_principal():
    while True:
        print("""
SISTEMA DE GESTION DE PACIENTES
1. Mostrar todos los pacientes
2. Seleccionar paciente por ID
3. Salir
""")
        try:
            opcion = int(input("Selecciona una opcion: "))
        except ValueError:
            print("Ingresa un numero valido.")
            continue

        if opcion == 1:
            for id_paciente, datos in pacientes.items():
                print(f"ID: {id_paciente} | Nombre: {datos['nombre']} | Edad: {datos['edad']}")
        elif opcion == 2:
            try:
                id_buscar = int(input("Ingresa el ID del paciente que deseas modificar: "))
                if id_buscar in pacientes:
                    menu_usuario(pacientes[id_buscar])
                else:
                    print("ID no encontrado.")
            except ValueError:
                print("ID invalido.")
        elif opcion == 3:
            print("Saliendo del sistemas, feliz dia")
            break
        else:
            print("Opcion no valida, intenta de nuevo.")

menu_principal()
