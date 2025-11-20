def crear_archivo(nombre):
    with open (nombre, "w") as file:
        file.write("archivo 2 creado")
        return f"archivo creado {nombre} correctamente"
    

