def crear_archivo(name_archivo, encabezado):
    with open (name_archivo, "w") as file:
        file.write(encabezado)
        
def agregar_line_txt(name_archivo, datos):
    with open(name_archivo, "a") as file:
        file.write(datos)
            
       