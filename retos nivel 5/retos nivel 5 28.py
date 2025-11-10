nombres=[]
edades=[]
grados=[]

print("registre el nuevo estuandte")

nombre=input("nombre: ")
edad=input("edad: ")
grado=input("grado: ")

nombres.append(nombre)
edades.append(edad)
grados.append(grado)

print(f"se grego el estudiante {nombre} con {edad} años del curso {grado}")
print(nombres, edades, grados)