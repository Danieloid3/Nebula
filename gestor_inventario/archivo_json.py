import json

def guardar_json(nombre_archivo, datos):
    with open(nombre_archivo, "w") as file:
        json.dump(datos, file)

def leer_json(nombre_archivo):
    try:
        with open(nombre_archivo, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return[]
    