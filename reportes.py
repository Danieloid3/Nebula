
from collections import Counter




def reportes(opcion, informacion_paciente):
    if opcion == 1:
        for datos in informacion_paciente:
                print(
                    f"ID: {datos['id']} | Nombre: {datos['nombre']} | Edad: {datos['edad']} Genero: {datos['genero']} Diagnóstico: {datos['diagnostico']} Historial: {datos['historial']}")
    elif opcion == 2:
        print("\n---Pacientes mayores de 60 años---\n")
        for datos in informacion_paciente:
            if datos["edad"] > 60:
                print(
                    f"ID: {datos['id']} | Nombre: {datos['nombre']} | Edad: {datos['edad']} Genero: {datos['genero']} Diagnóstico: {datos['diagnostico']} Historial: {datos['historial']}")
    elif opcion == 3:
        diagnóstico_frecuente = [cuenta['diagnostico'].lower() for cuenta in informacion_paciente]

        contador = Counter(diagnóstico_frecuente)
        print("---Diagnósticos frecuentes---")

        for diagnostico, cantidad in contador.items():
            print(f"{diagnostico} : {cantidad}")

        mas_comun = contador.most_common(1)
        print(f"Diagnóstico más comun: {mas_comun[0][0]} con {mas_comun[0][1]} paciente(s)")
    elif opcion == 4:
        cantidad = len(informacion_paciente)
        print(f"Hay un total de {cantidad} pacientes")
    elif opcion == 5:
        print("Saliendo del menú de reportes...")
        return

def menu_reportes(informacion_paciente):
    while True:
        try:

            print("\nSeleccione el número según la opción que necesite\n"
                  "\n1. Ver todos los pacientes registrados\n"
                  "2. Pacientes mayores de 60 años\n"
                  "3. Diagnósticos más frecuentes\n"
                  "4. Cantidad total de pacientes\n"
                  "5. Salir\n")
            opcion = int(input("Ingrese la opción: "))
            reportes(opcion, informacion_paciente)
            if opcion == 5:
                break
        except ValueError:
            print("Ingrese un número valido")