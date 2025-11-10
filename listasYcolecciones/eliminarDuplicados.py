#Solicitar al usuario varios números separados por coma
duplicates = list(map(int, input("Ingrese varios números separados por coma: ").split(",")))

#Mostrar la lista con duplicados
print(f"Lista con duplicados: {duplicates}")

#Eliminar los duplicados convirtiendo la lista a un conjunto y luego de vuelta a una lista
unique_numbers = list(set(duplicates))
print(f"Lista sin duplicados: {unique_numbers}")