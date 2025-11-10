#Crear una lista de frutas
fruits = ["manzana", "banana", "naranja", "fresa"]
print(f"Tienes las siguientes frutas disponibles: {fruits}")

#Agregar una fruta a la lista
add = input("Ingresa una nueva fruta: ")
fruits.append(add)

#Mostrar la lista actualizada
print(f"Lista de frutas actualizada: {fruits}")

#Eliminar una fruta de la lista
remove = input("Ingresa una fruta que deseas eliminar: ")

#Verificar si la fruta está en la lista antes de eliminar
if remove in fruits :
    fruits.remove(remove)
    print(f"Lista de frutas actualizada: {fruits}")
else:
    print(f"La fruta {remove} no se encuentra en la lista.")