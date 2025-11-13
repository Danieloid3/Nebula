from registrarPacientes import *
from buscarPacientes import *
from actualizacioDeDatos import *
from eliminar_paciente import *
from reportes import *

while True:

    try:
        print("\nMenú:")
        print("1. Registrar pacientes")
        print("2. Actualizar pacientes")
        print("3. Buscar pacientes")
        print("4. Eliminar pacientes")
        print("5. Reportes")
        print("6. Salir")
        menu = input("Choose an option: ")

        match menu:
            case "1":

                registrar_pacientes()
            case "2":
                menu_principal(informacion_paciente)
            case "3":
                print("Buscar Pacientes")
                consulta = input("Ingrese el nombre o ID del paciente a buscar: ")
                buscarPaciente(informacion_paciente, consulta)
            case "4":
                menu_eliminar(informacion_paciente)
            case "5":
                menu_reportes(informacion_paciente)
            case "6":
                print("Saliendo del programa...")
            case _:
                print("You have entered an invalid option")


    except ValueError:
        print("You have entered an invalid number")