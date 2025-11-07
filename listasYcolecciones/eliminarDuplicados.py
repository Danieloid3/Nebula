duplicates = list(map(int, input("Ingrese varios números separados por coma: ").split(",")))

print(f"Lista con duplicados: {duplicates}")

unique_numbers = list(set(duplicates))
print(f"Lista sin duplicados: {unique_numbers}")