# Agenda de Contactos

agenda = []   # Aquí se guardarán los contactos

    # Función que valida que el usuario no deje campos vacíos.
def pedir_texto(mensaje):
    while True:
        dato = input(mensaje).strip()
        if dato == "":
            print("Este campo no puede estar vacío.")
        else:
            return dato


print("--- AGENDA DE CONTACTOS ---")

while True:
    print("\nSeleccione una opción: "
    "\n1. Agregar contacto"
    "\n2. Ver contactos"
    "\n3. Buscar contacto"
    "\n4. Editar contacto"
    "\n5. Eliminar contacto"
    "\n6. Salir")


    opcion = input("Opción: ")

    # Agregar contacto
    if opcion == "1":
        nombre = pedir_texto("Nombre: ")
        telefono = pedir_texto("Teléfono: ")
        correo = pedir_texto("Correo: ")

        contacto = {
            "nombre": nombre,
            "telefono": telefono,
            "correo": correo
        }

        agenda.append(contacto)
        print("Contacto agregado correctamente.")

   # Ver los contactos guardados
    elif opcion == "2":
        if len(agenda) == 0:
            print("La agenda está vacía.")
        else:
            print("\n--- LISTA DE CONTACTOS ---")
            for contacto in agenda:
                print(contacto)
                
    # Buscar contacto por nombre
    elif opcion == "3":
        nombre_buscar = input("Nombre a buscar: ").lower()

        encontrado = False

        for c in agenda:
            if c["nombre"].lower() == nombre_buscar:
                print("Contacto encontrado:", c)
                encontrado = True
                break

        if not encontrado:
            print("No se encontró ese contacto.")

    # Editar contacto
    elif opcion == "4":
        nombre_edit = input("Nombre del contacto a editar: ").lower()

        encontrado = False

        for c in agenda:
            if c["nombre"].lower() == nombre_edit:
                print("Contacto encontrado:", c)

                c["nombre"] = pedir_texto("Nuevo nombre: ")
                c["telefono"] = pedir_texto("Nuevo teléfono: ")
                c["correo"] = pedir_texto("Nuevo correo: ")

                print("Contacto actualizado.")
                encontrado = True
                break

        if not encontrado:
            print("No existe un contacto con ese nombre.")

    # Eliminar contacto
    elif opcion == "5":
        nombre_del = input("Nombre del contacto a eliminar: ").lower()

        eliminado = False

        for c in agenda:
            if c["nombre"].lower() == nombre_del:
                agenda.remove(c)
                print("Contacto eliminado.")
                eliminado = True
                break

        if not eliminado:
            print("No se encontró ese contacto.")

    # Salir del programa
    elif opcion == "6":
        print("Cerrando agenda... ¡Hasta luego!")
        break

    else:
        print("Opción inválida, intente nuevamente.")
