frutas = ["Manzana", "Pera", "Banano", "Piña"]

nueva_fruta1 = (input("ingresa una fruta: "))
frutas.append(nueva_fruta1)
print(frutas)

frutas = ["Manzana", "Pera", "Banano", "Piña"]

nueva_fruta2 = (input("elimina una fruta: "))
frutas.remove(nueva_fruta2)
print(frutas)

frutas = ["Manzana", "Pera", "Banano", "Piña"]

nueva_fruta3 = (input("Busca una fruta: "))
frutas.index(nueva_fruta3)
print(f"Aqui esta su fruta buscada; {nueva_fruta3}")

