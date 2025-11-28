import os
import csv

#BASE_DIR es la brújula de tu programa: le dice desde dónde debe buscar los archivos.
#__file__ - Es una variable especial que significa:Ruta del archivo actual que se está ejecutando.
#os.path.abspath(__file__) - Convierte esa ruta en una ruta completa y clara para el sistema.
#os.path.dirname(...) - Ahora le quita el nombre del archivo y deja solo la carpeta.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
archivo_user = os.path.join(BASE_DIR, "usuarios.csv")


def cargar_usuarios():
    usuarios = []

#csv.DictReader te permite leer un CSV y trabajar con datos por su nombre, no por su posición.
    with open(archivo_user, "r", newline="") as archivo:
        lector = csv.DictReader(archivo)
        for fila in lector:
            usuarios.append(fila)

    return usuarios


def validar_login(username, password, usuarios):
    for user in usuarios:
        if user["username"] == username and user["password"] == password:
            return True
    return False


def login_user():
    while True:
        

            usuarios = cargar_usuarios()

            print("\n--- LOGIN ---")
            username = input("Usuario: ")
            password = input("Contraseña: ")

            if validar_login(username, password, usuarios):
                print("\nAcceso concedido\n")
                break
            else:
                print("\nUsuario o contraseña incorrectos. Vuelve a intentarlo.")
                
