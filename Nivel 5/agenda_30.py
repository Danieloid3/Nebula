# Agenda de contactos muy sencilla

agenda = []  # Lista vacía

# Agregar contactos
nombre1 = input("Ingresa el nombre del primer contacto: ")
telefono1 = input("Ingresa su teléfono: ")

nombre2 = input("Ingresa el nombre del segundo contacto: ")
telefono2 = input("Ingresa su teléfono: ")

# Crear diccionarios
contacto1 = {"nombre": nombre1, "telefono": telefono1}
contacto2 = {"nombre": nombre2, "telefono": telefono2}

# Agregarlos a la lista
agenda.append(contacto1)
agenda.append(contacto2)

# Mostrar todos los contactos
print("\n📒 Lista de contactos:")
for c in agenda:
    print(f"Nombre: {c['nombre']} - Teléfono: {c['telefono']}")
