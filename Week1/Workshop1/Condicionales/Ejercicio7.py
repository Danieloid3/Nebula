while True:
    try:
        age = int(input("Ingresa tu edad: "))
        if age < 0 or age > 100:
            print("El edad es invalida")
            continue
        if age >= 18:
            print("Eres mayor de edad")
        else:
            print("Eres menor de edad")
    except ValueError:
        print("El numero es invalido")
    except (KeyboardInterrupt):
        print("Saliendo...")
        break