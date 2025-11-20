def crear_archivo(nombre_archivo):
    with open(nombre_archivo, "w") as file:
        file.write("Hola, este es un archivo de texto.\n")
        return "Archivo creado exitosamente."

def leer_archivo(nombre):
    try:
        with open (nombre, "r") as file:
            return file.read()
    except FileNotFoundError:
        return "El archivo no existe."

def agregar_texto(nombre, texto):
    try:
        with open(nombre, "a") as file:
            file.write(texto + "\n")
            return "Texto agregado exitosamente."
    except FileNotFoundError:
        return "El archivo no existe."

crear_archivo("archivo_txt")