fruits = ["manzana", "banana", "naranja", "fresa"]
print(f"Tienes las siguientes frutas disponibles: {fruits}")

add = input("Ingresa una nueva fruta: ")

fruits.append(add)

print(f"Lista de frutas actualizada: {fruits}")

remove = input("Ingresa una fruta que deseas eliminar: ")

if remove in fruits :
    fruits.remove(remove)
    print(f"Lista de frutas actualizada: {fruits}")
else:
    print(f"La fruta {remove} no se encuentra en la lista.")