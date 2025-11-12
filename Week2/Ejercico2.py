lista = [1,1,1,2,2,2,3,4,4,5,1]
lista.sort()

for i in range (0, len(lista)):
    print("\n\nI:",i)
    for j in range(i+1,len(lista)):
        print("J:", j)
        if j == len(lista)-2:
            break
        elif lista[i]==lista[j]:
            del lista[i]

print(lista)



