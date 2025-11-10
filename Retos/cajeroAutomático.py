# Base de datos simulada de usuarios
usuarios = {
    "juan": {
        "password": "1234",
        "saldo": 500
    },
    "ana": {
        "password": "abcd",
        "saldo": 1000
    }
}

print("=== Cajero Automático ===")

# Verificar si el usuario existe
usuario = input("Ingrese su usuario: ").lower()

if usuario not in usuarios:
    print("El usuario no existe en el sistema.")
else:

# Verificar contraseña
    intentos = 3
    while intentos > 0:
        password = input("Ingrese su contraseña: ")

        if password == usuarios[usuario]["password"]:
            print("\nAcceso concedido.\n")
            break
        else:
            intentos -= 1
            print(f"Contraseña incorrecta. Intentos restantes: {intentos}")

    if intentos == 0:
        print("Demasiados intentos fallidos. Operación cancelada.")
    else:
        
        # Menú principal del cajero
        while True:
            print("\nSeleccione una opción: \n1. Consultar saldo\n2. Retirar dinero\n3. Depositar dinero\n4. Salir")

            opcion = input("Opción: ")

            # Consultar saldo
            if opcion == "1":
                print(f"Su saldo actual es: {usuarios[usuario]['saldo']}")

            # Retirar
            elif opcion == "2":
                try:
                    monto = float(input("Monto a retirar: "))
                    if monto <= 0:
                        print("El monto debe ser mayor que 0.")
                    elif monto > usuarios[usuario]["saldo"]:
                        print("Fondos insuficientes.")
                    else:
                        usuarios[usuario]["saldo"] -= monto
                        print(f"Retiro exitoso. Nuevo saldo: {usuarios[usuario]['saldo']}")
                except ValueError:
                    print("Debe ingresar un número válido.")

            # Depositar
            elif opcion == "3":
                try:
                    monto = float(input("Monto a depositar: "))
                    if monto <= 0:
                        print("El monto debe ser mayor que 0.")
                    else:
                        usuarios[usuario]["saldo"] += monto
                        print(f"Depósito exitoso. Nuevo saldo: {usuarios[usuario]['saldo']}")
                except ValueError:
                    print("Debe ingresar un número válido.")

            # Salir
            elif opcion == "4":
                print("Gracias por usar el cajero. ¡Hasta luego!")
                break

            else:
                print("Opción inválida. Intente de nuevo.")
