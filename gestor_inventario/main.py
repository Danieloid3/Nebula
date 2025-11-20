from archivo_txt import crear_archivo, agregar_line_txt
from archivo_csv import crear_csv, agregar_line
from archivo_json import guardar_json, leer_json

inventario = leer_json("inventario.json")


def registrar_producto():
    nombre = input("Ingresa el nombre del producto: ")
    precio = float(input("Ingresa el precio: "))
    cantidad = int(input("Ingresa la cantidad: "))

    producto = {"nombre": nombre, "precio": precio, "cantidad": cantidad}
    inventario.append(producto)
    print("Producto registrado.")


def editar_producto():
    nombre_buscar = input("Ingresa el nombre del producto a buscar: ")
    for p in inventario:
        if p["nombre"] == nombre_buscar:
            print("Producto encontrado.")
            p["nombre"] = input("Nuevo nombre: ")
            p["precio"] = float(input("Nuevo precio: "))
            p["cantidad"] = int(input("Nueva cantidad: "))
            print("Producto editado.")
            return
    print("Producto no encontrado.")


def eliminar_producto():
    nombre_buscar = input("Nombre del producto a eliminar: ")
    for p in inventario:
        if p["nombre"] == nombre_buscar:
            inventario.remove(p)
            print("Producto eliminado.")
            return
    print("Producto no encontrado.")


def guardar_txt():
    crear_archivo("inventario.txt")
    for p in inventario:
        linea = f"{p['nombre']}, {p['precio']}, {p['cantidad']}\n"
        agregar_line_txt("inventario.txt", linea)
    print("TXT guardado.")


def guardar_csv_menu():
    crear_csv("inventario.csv", ["nombre", "precio", "cantidad"])
    for p in inventario:
        agregar_line("inventario.csv", [p["nombre"], p["precio"], p["cantidad"]])
    print("CSV guardado.")


def guardar_json_menu():
    guardar_json("inventario.json", inventario)
    print("JSON guardado.")


while True:
    print("\nMENU")
    print("1. Registrar producto")
    print("2. Editar producto")
    print("3. Eliminar producto")
    print("4. Guardar TXT")
    print("5. Guardar CSV")
    print("6. Guardar JSON")
    print("7. Salir")

    opcion = input("Selecciona una opción: ")

    match opcion:
        case "1":
            registrar_producto()
        case "2":
            editar_producto()
        case "3":
            eliminar_producto()
        case "4":
            guardar_txt()
        case "5":
            guardar_csv_menu()
        case "6":
            guardar_json_menu()
        case "7":
            break
        case _:
            print("Opción inválida.")
