from datos import ventas

def top_3_productos():
    contador = {}

    for v in ventas:
        contador[v["producto"]] = contador.get(v["producto"], 0) + v["cantidad"]

    top = sorted(contador.items(), key=lambda x: x[1], reverse=True)[:3]
    print("Top 3 Products:")
    for p in top:
        print(p)

def ventas_por_marca():
    marcas = {}

    for v in ventas:
        marcas[v["marca"]] = marcas.get(v["marca"], 0) + v["total"]

    print("Sales by Brand:")
    for m, total in marcas.items():
        print(m, "=>", total)

def menu_reportes():
    while True:
        print("\n--- REPORTS MENU ---")
        print("1. Top 3 best sellers")
        print("2. Sales by brand")
        print("0. Back")

        op = input("Option: ")

        if op == "1":
            top_3_productos()
        elif op == "2":
            ventas_por_marca()
        elif op == "0":
            break
