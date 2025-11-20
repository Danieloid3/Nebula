import json

def crear_archivo(nombre, data):
    with open (nombre, "w") as file:
        json.dump(data, file, indent=4)
        return "Archivo JSON creado exitosamente."

def agregar_datos(nombre, nueva_data):
    with open (nombre, "r") as file:
        data = json.load(file)
    data.update(nueva_data)
    with open (nombre, "w") as file:
        json.dump(data, file, indent=4)
        return "Datos agregados exitosamente al archivo JSON."


#print(crear_archivo("archivo_json.json", {"Usuario": "Emma", "Tipo de Usuario": "Coder"}))
print(agregar_datos("archivo_json.json", {"Edad": 30, "Ciudad": "Madrid"}))