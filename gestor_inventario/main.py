from archivo_txt import crear_archivo
from archivo_csv import crear_csv, agregar_line
from archivo_json import guardar_json, leer_json
from menu import *

print(crear_archivo("mi_archivo.txt"))

crear_csv("miarchivo.csv", ["nombre:", "precio:", "cantidad:"])
agregar_line("miarchivo.csv", ["manzana:", "1500", "10"])

guardar_json
leer_json
