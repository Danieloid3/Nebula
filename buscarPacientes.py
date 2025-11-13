


def buscarPaciente (id):
    encontrado = None
    for paciente in informacion_paciente:
        if paciente['id'] == id:
            encontrado = paciente
            break
    if encontrado:
        print("Paciente encontrado")
        print(f"Nombre: {encontrado['nombre']}")
        print(f"Edad: {encontrado['edad']}")
        print(f"Género: {encontrado['género']}")
        print(f"Diagnóstico: {encontrado['diagnóstico']}")
        print(f"Historial Médico: {encontrado["historial"]}")