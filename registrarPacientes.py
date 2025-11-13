informacion_paciente = [{"id": 1, "nombre": "Ana",    "edad": 30,  "genero": "f", "diagnostico": "Gripe",        "historial": ["Gripe"]},
    {"id": 2, "nombre": "Dani",   "edad": 45,  "genero": "m", "diagnostico": "Asma",         "historial": ["Asma", "Resfriado"]},
    {"id": 3, "nombre": "Damian",  "edad": 70,  "genero": "f", "diagnostico": "Asma", "historial": ["Hipertension"]},
    {"id": 4, "nombre": "Carlos", "edad": 5,   "genero": "m", "diagnostico": "Varicela",     "historial": ["Varicela"]},
    {"id": 5, "nombre": "Sofia",  "edad": 29,  "genero": "f", "diagnostico": "Alergia",      "historial": ["Rinitis", "Alergia"]},
    {"id": 6, "nombre": "Miguel", "edad": 120, "genero": "m", "diagnostico": "Diabetes",     "historial": ["Diabetes", "Hipertension"]},
    {"id": 7, "nombre": "Pablo",  "edad": 0,   "genero": "m", "diagnostico": "Prematuro",    "historial": ["Prematuro"]},
    {"id": 8, "nombre": "Ines",   "edad": 18,  "genero": "f", "diagnostico": "Resfriado",    "historial": ["Resfriado"]},
]  # En esta lista se estará almacenando los datos obtencontador_idos del diccionario pacientes


def registrar_pacientes():
    contador_id = informacion_paciente[-1]["id"] if informacion_paciente else 0#Contador para manejar los id y evitar que hayan repeticiones
    flag = True
    while flag == True:
        print("\n---Ingrese los datos del paciente---\n")

        historial =[] #Lista que va a almacenar los datos obtenidos en el valor diagnostico

        contador_id += 1 # Va aumentando de 1 en 1 sin generar repeticiones en el id

        while True:
            #Solicitar al usuario los datos correspondientes
            nombre = input("Nombre: ")
            if not nombre.strip().isalpha(): #si el nombre está vacio o contiene algo
                #que no sean letras muestra el error
                print("El usuario sólo debe contener letras y no puede estar vacío")
                continue
            break

        while True:
            try:
                edad = int(input("Edad: "))
                if edad < 0 or edad > 120: # verifica que la edad esté entre 0 y 120
                    print("Ingrese una edad entre 0 y 120 años")
                    continue
                else:
                    break
            except ValueError:
                print("Ingrese un valor válido.")
                continue

        while True:
            try:
                genero = input("Ingrese su género: (M/F)").lower()

                if genero == "f" or genero == "m":
                    break
                else:
                    print("Seleccione M para masculino ó F para femenino")
            except ValueError:
                print("Opción no váida")
                continue

        while True:
            diagnostico = input("Diagnóstico: ")
            if not diagnostico.replace(" ", "").isalpha(): #si el nombre está vacio o contiene algo
                #que no sean letras muestra el error
                print("El campo sólo debe contener letras y no puede estar vacío")
                continue
            break

        historial.append(diagnostico) #Agregar a historial lo obtenido en el valor diagnostico

        #Diccionario que me permite organizar la información relacionada a un paciente
        pacientes = {
            "id" : contador_id,
            "nombre" : nombre,
            "edad" : edad,
            "genero" : genero,
            "diagnostico" : diagnostico,
            "historial" : historial
        }

        informacion_paciente.append(pacientes)
        nuevo_paciente = ""

        while not nuevo_paciente == "si" and not nuevo_paciente == "no":
            nuevo_paciente = input("Desea ingresar otro paciente? si/no").lower()
            if nuevo_paciente == "si":
                continue
            elif nuevo_paciente == "no":
                flag = False
                print("Gracias por usar nuestro servicio. ¡Hasta luego!")



    for datos in informacion_paciente:
        print(
            f"ID: {datos['id']} | Nombre: {datos['nombre']} | Edad: {datos['edad']} Genero: {datos['genero']} Diagnóstico: {datos['diagnostico']} Historial: {datos['historial']}")
    