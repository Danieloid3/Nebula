

def mostrar_datos(usuario):
    print('DATOS DEL PACIENTE')
    print(f"Nombre: {usuario.get('nombre')}")
    print(f"Edad: {usuario.get('edad')}")
    print(f"Genero: {usuario.get('genero')}")
    print(f"Diagnostico: {usuario.get('diagnostico')}")
    historial = ', '.join(usuario.get('historial', []))
    print(f"Historial: {historial}")

def modificar_nombre(usuario):
    while True:
        try:
            nuevo_nombre = input('Ingresa el nuevo nombre: ').strip()
            if not nuevo_nombre.isalpha():
                raise ValueError()
            confirmar = ''
            while confirmar not in ('si', 'no'):
                print(f"Nombre anterior: {usuario['nombre']}")
                confirmar = input(f"¿Deseas cambiarlo por '{nuevo_nombre}'? (si/no): ").lower().strip()
                if confirmar == 'si':
                    usuario['nombre'] = nuevo_nombre
                    print('Nombre actualizado con exito.')
                elif confirmar == 'no':
                    print('Cambio cancelado.')
                else:
                    print("Responde solo con 'si' o 'no'.")
                    continue
                break
            break
        except ValueError:
            print('Valor no valido para nombre.')

def modificar_edad(usuario):
    while True:
        try:
            nueva_edad = input('Ingresa la nueva edad: ').strip()
            if not nueva_edad.isdigit():
                raise ValueError()
            confirmar = ''
            while confirmar not in ('si', 'no'):
                print(f"Edad anterior: {usuario['edad']}")
                confirmar = input(f"¿Deseas cambiarla por '{nueva_edad}'? (si/no): ").lower().strip()
                if confirmar == 'si':
                    usuario['edad'] = int(nueva_edad)
                    print('Edad actualizada con exito.')
                elif confirmar == 'no':
                    print('Cambio cancelado.')
                else:
                    print("Responde solo con 'si' o 'no'.")
                    continue
                break
            break
        except ValueError:
            print('Valor no valido para edad.')

def modificar_genero(usuario):
    while True:
        try:
            nuevo_genero = input('Ingresa el nuevo genero: ').strip()
            if not nuevo_genero.isalpha():
                raise ValueError()
            confirmar = ''
            while confirmar not in ('si', 'no'):
                print(f"Genero anterior: {usuario['genero']}")
                confirmar = input(f"¿Deseas cambiarlo por '{nuevo_genero}'? (si/no): ").lower().strip()
                if confirmar == 'si':
                    usuario['genero'] = nuevo_genero
                    print('Genero actualizado con exito.')
                elif confirmar == 'no':
                    print('Cambio cancelado.')
                else:
                    print("Responde solo con 'si' o 'no'.")
                    continue
                break
            break
        except ValueError:
            print('Valor no valido para genero.')

def modificar_diagnostico(usuario):
    while True:
        try:
            nuevo_diag = input('Ingresa el nuevo diagnostico: ').strip()
            if not nuevo_diag.isalpha():
                raise ValueError()
            confirmar = ''
            while confirmar not in ('si', 'no'):
                print(f"Diagnostico anterior: {usuario['diagnostico']}")
                confirmar = input(f"¿Deseas cambiarlo por '{nuevo_diag}'? (si/no): ").lower().strip()
                if confirmar == 'si':
                    usuario['diagnostico'] = nuevo_diag
                    print('Diagnostico actualizado con exito.')
                elif confirmar == 'no':
                    print('Cambio cancelado.')
                else:
                    print("Responde solo con 'si' o 'no'.")
                    continue
                break
            break
        except ValueError:
            print('Valor no valido para diagnostico.')

def agregar_historial(usuario):
    nuevo_evento = input('Agrega un nuevo evento al historial (deja vacio para cancelar): ').strip()
    if nuevo_evento == '':
        print('No se agrego nada al historial.')
    else:
        usuario['historial'].append(nuevo_evento)
        print(f"Se agrego '{nuevo_evento}' al historial.")

def menu_usuario(usuario):
    while True:
        print("""
MENU DE MODIFICACION DE PACIENTES
1. Mostrar datos del paciente
2. Modificar nombre
3. Modificar edad
4. Modificar genero
5. Modificar diagnostico
6. Agregar nuevo evento al historial
7. Volver al menu principal
""")
        try:
            opcion = int(input('Selecciona una opcion: ').strip())
        except ValueError:
            print('Ingresa un numero valido.')
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
            print('Opcion no valida, intenta de nuevo.')

def menu_principal(pacientes):
    while True:
        print("""
SISTEMA DE GESTION DE PACIENTES
1. Mostrar todos los pacientes
2. Seleccionar paciente por ID
3. Salir
""")
        try:
            opcion = int(input('Selecciona una opcion: ').strip())
        except ValueError:
            print('Ingresa un numero valido.')
            continue

        if opcion == 1:
            for datos in pacientes:
                historial = ', '.join(datos.get('historial', []))
                print(
                    f"ID: {datos.get('id')} | "
                    f"Nombre: {datos.get('nombre')} | "
                    f"Edad: {datos.get('edad')} | "
                    f"Genero: {datos.get('genero')} | "
                    f"Diagnostico: {datos.get('diagnostico')} | "
                    f"Historial: {historial}"
                )
        elif opcion == 2:
            try:
                id_buscar = int(input('Ingresa el ID del paciente que deseas modificar: ').strip())
                paciente = next((p for p in pacientes if p.get('id') == id_buscar), None)
                if paciente:
                    menu_usuario(paciente)
                else:
                    print('ID no encontrado.')
            except ValueError:
                print('ID invalido.')
        elif opcion == 3:
            print('Saliendo del sistema, feliz dia.')
            break
        else:
            print('Opcion no valida, intenta de nuevo.')



