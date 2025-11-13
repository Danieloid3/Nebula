
def buscarPaciente (lista, id):

    parcial = []
    for paciente in lista:
        if id.lower() in paciente['nombre'].lower() or id.lower() in paciente['diagnostico'].lower() or (id) == str(paciente['id']):
            parcial.append(paciente)
            print("Coincidencias encontradas:")
    for p in parcial:
        print(f"ID: {p['id']} | Nombre: {p['nombre']} | Edad: {p['edad']} | Género: {p['genero']} | Diagnóstico: {p['diagnostico']} | Historial Médico: {p['historial']}")
    if not parcial:
        print("No se encontró ningún paciente con coincidencias con ese ID o nombre.")