nombres=[]
telefonos=[]
correos=[]

print("registre el nuevo estuandte")

nombre=input("nombre: ")
telefono=input("telefono: ")
correo=input("correo: ")

nombres.append(nombre)
telefonos.append(telefono)
correos.append(correo)

print(f"se grego el contacto {nombre} con el telefono {telefono} y el correo {correo}")
print(nombres, telefonos, correos)
