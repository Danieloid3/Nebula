con_duplicados=[1,1,2,2,3,3,5,4,6,7,7,8]
sin_duplicados=[]

for i in con_duplicados:
    if i not in sin_duplicados:
        sin_duplicados.append(i)

print(f"lista sin duplicados: {sin_duplicados}")        
