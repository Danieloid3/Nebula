#Mini base de datos para gestión de estudiantes

# Esta lista almacenará a los estudiantes.
estudiantes = []


print("\n--- SISTEMA DE GESTIÓN DE ESTUDIANTES ---")

while True:
    # Menú principal
    print("\nSeleccione una opción: \n1. Agregar estudiante\n2. Ver lista de estudiantes\n3. Buscar estudiante por nombre\n4. Eliminar estudiante\n5. Salir")

    opcion = input("Opción: ")

    #Agregar estudiante
    if opcion == "1":
        nombre = input("Nombre del estudiante: ")
        edad = input("Edad del estudiante: ")
        carrera = input("Carrera del estudiante: ")

        # Crea un diccionario con los datos del estudiante
        estudiante = {
            "nombre": nombre,
            "edad": edad,
            "carrera": carrera
        }

        # Se añade a la lista de estudiantes
        estudiantes.append(estudiante)

        print("Estudiante agregado con éxito.")

    #Ver lista de estudiantes
    elif opcion == "2":
        if len(estudiantes) == 0:
            print("No hay estudiantes registrados.")
        else:
            print("\nLista de estudiantes:")
            for student in estudiantes:
                print(student)   # muestra cada diccionario

    #Buscar estudiante por nombre
    elif opcion == "3":
        nombre_buscar = input("Ingrese el nombre del estudiante a buscar: ")

        encontrado = False

        for student in estudiantes:
            if student["nombre"].lower() == nombre_buscar.lower():
                print("Estudiante encontrado:", student)
                encontrado = True
                break

        if not encontrado:
            print("No se encontró un estudiante con ese nombre.")

    #Eliminar estudiante
    elif opcion == "4":
        nombre_eliminar = input("Nombre del estudiante a eliminar: ")

        eliminado = False

        for student in estudiantes:
            if student["nombre"].lower() == nombre_eliminar.lower():
                estudiantes.remove(student)
                print("Estudiante eliminado.")
                eliminado = True
                break

        if not eliminado:
            print("No se encontró ese estudiante.")

    #Salir del sistema
    elif opcion == "5":
        print("Saliendo del sistema... ¡Hasta luego!")
        break

    else:
        print("Opción inválida. Intente de nuevo.")
