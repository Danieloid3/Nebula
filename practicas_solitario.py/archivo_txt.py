def archivo_new(name):
    with open(name, "w") as file:
        file.write("archivo creado")
        return f"archivo {name} creado correctamente"