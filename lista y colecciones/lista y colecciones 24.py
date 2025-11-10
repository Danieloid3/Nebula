numeros=input("dime los numeros separados por comas ")
numero=[int(n1) for n1 in numeros.split (",")]

duplicados=[]

for n2 in numero:
    if n2 not in duplicados:
        duplicados.append(n2)


print(duplicados)

