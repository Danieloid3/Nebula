print("---Conversor de Celsius a Fahrenheit---")

# Solicitar al usuario que ingrese la temperatura en grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

#Formula para convertir grados Celsius a Fahrenheit °F = °C × (9/5) + 32
fahrenheit = celsius * (9/5) + 32

# Mostrar el resultado al usuario
print(f"La temperatura en grados Fahrenheit es: {fahrenheit} °F")