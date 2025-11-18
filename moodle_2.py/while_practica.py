print("1.  Agregar producto")  # Menú opción 1
print("2.  Mostrar inventario")  # Menú opción 2
print("3.  Calcular estadísticas")  # Menú opción 3
print("4. Salir")  # Menú opción 4

while True:  # Bucle principal
    opcion=(input("elige una opcion: "))  # Solicita opción

    if opcion == "1":
        print("Has entrado a la seccion de Agregar producto")  # Mensaje opción 1

    elif opcion == "2":
        print("Has entrado a la seccion de Mostrar inventario")  # Mensaje opción 2

    elif opcion == "3":
        print("Has entrado a la seccion de calcular estadistica")  # Mensaje opción 3

    elif opcion =="4":
        print("Has salido del menu. Vuelva pronto")  # Sale del programa
        break

    else: 
        print("Solo hay opciones del 1 al 4, vuelve a ingresar un numero: ")  # Manejo de errores
