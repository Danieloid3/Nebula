import csv
import os 

class CRUD:

    def crear_archivo (self, archivo):
        if not os.path.exists(archivo):
            with open(archivo, "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow(["id", "producto", "precio", "cantidad"])

    def crear_id (self, archivo):
        with open (archivo, "r") as file:
            filas = list(csv.reader(file))

            if len(filas) ==1:
                return 1
            
            ultimo_id=(filas[-1][0])
            return ultimo_id + 1
        
    def crear(self, archivo, producto, precio, cantidad):
        id_nuevo = self.obtener_nuevo_id(archivo)
        with open (archivo, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow ([id_nuevo, producto, precio, cantidad ])
        return id_nuevo    
    

    def listar (self, archivo):
        with open (archivo, "r") as file:
            reader=csv.reader(file)
            next(reader)
            return (list(reader))