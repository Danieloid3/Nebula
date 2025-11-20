import json
import os

class CRUD:
    def crear_archivo(self, archivo, datos):
        with open(archivo, "w") as file:
            json.dump(datos, file, indent=4)
            return "Archivo JSON creado exitosamente."

    def agregar_datos(self,archivo, nueva_data):
        with open (archivo, "r") as file:
            data = json.load(file)
        data.update(nueva_data)
        with open (archivo, "w") as file:
            json.dump(data, file, indent=4)
            return "Datos agregados exitosamente al archivo JSON."

    def auto_id(self,archivo):
        with open(archivo, "r") as file:
            data = list(json.load(file))
            if len(data) == 0:
                return 1
            last_id = data[-1]["id"]
            return last_id + 1

    def create_users(self,archivo, datos):
        if not os.path.isfile(archivo):
            self.crear_archivo(archivo, datos)
        else:
            self.agregar_datos(archivo, datos)



