informacion_paciente = [] #En esta lista se estará almacenando los datos obtencontador_idos del diccionario pacientes
contador_id = 0 #Contador para manejar los id y evitar que hayan repeticiones

while True:
    print("\n---Ingrese los datos del paciente---\n")

    historial =[] #Lista que va a almacenar los datos obtenidos en el valor diagnostico 

    contador_id += 1 # Va aumentando de 1 en 1 sin generar repeticiones en el id 
    
    while True:
        #Solicitar al usuario los datos correspondientes
        nombre = input("Nombre: ")
        if not nombre.replace(" ", "").isalpha(): #si el nombre está vacio o contiene algo
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

    nuevo_paciente = input("Desea ingresar otro paciente? si/no").lower()
    if nuevo_paciente == "si":
        continue
    elif nuevo_paciente == "no":
        print("Gracias por usar nuestro servicio. ¡Hasta luego!")
        break
    
#print(f"\nHistoria Clínica del paciente\n {informacion_paciente}") #Para visualizar todo el contenido almacenado en la lista
    