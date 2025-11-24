from datos import ventas


def top_3_productos():
    conteo = {}
    for v in ventas:
        conteo[v['title']] = conteo.get(v['title'], 0) + v['quantity in stock']
    top = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
    print(top)


def ventas_por_book():
    marcas = {}
    for v in ventas:
        marcas[v['marca']] = marcas.get(v['marca'], 0) + v['neto']
    print(marcas)


def inventory_performance():
    totales = sum(v['neto'] for v in ventas)
    print(f"Total revenue: {totales}")
