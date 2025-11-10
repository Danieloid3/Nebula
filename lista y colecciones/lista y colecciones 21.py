lista=["pera","uva","maracuya","sandia"]
buscar=input("que fruta quieres buscar? ")

if buscar in lista:
    print(f"la fruta {buscar} si esta en la lista")
else:
    print(f"la fruta {buscar} no esta en la lista")