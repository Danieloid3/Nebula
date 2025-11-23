from datos import ventas


def top_3_productos():
    conteo = {}
    for v in ventas:
        conteo[v['producto']] = conteo.get(v['producto'], 0) + v['cantidad']
    top = sorted(conteo.items(), key=lambda x: x[1], reverse=True)[:3]
    print(top)


def ventas_por_marca():
    marcas = {}
    for v in ventas:
        marcas[v['marca']] = marcas.get(v['marca'], 0) + v['neto']
    print(marcas)


def rendimiento_inventario():
    totales = sum(v['neto'] for v in ventas)
    print(f"Total revenue: {totales}")
