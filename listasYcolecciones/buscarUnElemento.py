#Crear una lista de carros
list_cars= ["mazda", "ford", "honda", "toyota"]

#Solicitar al usuario el nombre del carro a buscar
cars_to_find= input("Ingrese el nombre del auto que desea buscar: ").lower()

#Buscar el carro en la lista
if cars_to_find in list_cars :
    print(f"El carro {cars_to_find} se encuentra en la base de datos")
else:  
    print(f"El carro {cars_to_find} no se encuentra en la base de datos")