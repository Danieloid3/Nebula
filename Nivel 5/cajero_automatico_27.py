nombre=(input("Ingresa tu nombre: "))
contraseña=(input("Ingresa tu contraseña: "))

if contraseña=="1234":
    print("contraseña correcta")

    cuenta=(input("Ingresa tu tipo de cuenta ahorro/corriente: "))

    lista=["10.000","20.000","30.000","40.000","50.000"]
    print(lista)

    retiro=(input("ingresa el monto que quieres retirar: "))
    
    confirmar=(input("Confirmar retiro: "))
    if confirmar.lower()=="confirmar retiro":
        print("Se ha confirmado correctamente tu retiro",retiro)
    else:
        print("Cancelaste retiro")    

else:
    print("contraseña incorrecta")
    

