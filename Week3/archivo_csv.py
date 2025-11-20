import csv

def crear_csv(nombre, encabezados):
    with open(nombre, "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(encabezados)
        return "Archivo CSV creado exitosamente."

#crear_csv("archivo_csv.csv", ["Usuario", "Tipo de Usuario"])

def leer_csv(nombre):
    try:
        with open(nombre, "r") as file:
            reader = csv.reader(file)
            for row in reader:
                print(row)
            return
    except FileNotFoundError:
        return "El archivo CSV no existe."

def agregar_fila_csv(nombre, fila):
    try:
        with open(nombre, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(fila)
            return "Fila agregada exitosamente al archivo CSV."
    except FileNotFoundError:
        return "El archivo CSV no existe."

#agregar_fila_csv("archivo_csv.csv", ["Dani", "Administrador"])
print(leer_csv("archivo_csv.csv"))