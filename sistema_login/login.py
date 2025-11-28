import os
import csv

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ARCHIVO_USUARIOS = os.path.join(BASE_DIR, "usuarios.csv")


def cargar_usuarios():
    usuarios = []

    with open(ARCHIVO_USUARIOS, "r", newline="") as archivo:
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
    usuarios = cargar_usuarios()

    print("\n--- LOGIN ---")
    username = input("Usuario: ")
    password = input("Contraseña: ")

    if validar_login(username, password, usuarios):
        print("\nAcceso concedido\n")
    else:
        print("\nUsuario o contraseña incorrectos")
        exit()
