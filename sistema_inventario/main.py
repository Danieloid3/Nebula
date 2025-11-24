from inventario import mostrar_productos, agregar_producto, actualizar_producto, eliminar_producto, buscar_producto
from ventas import registrar_venta, mostrar_ventas
from reportes import top_3_productos, ventas_por_marca, rendimiento_inventario


def main():
    while True:
        print("=== Menu ===")
        print("1. Show products")
        print("2. Add product")
        print("3. Update product")
        print("4. Delete product")
        print("5. Search product")
        print("6. Register sale")
        print("7. Show sales")
        print("8. Top 3 products")
        print("9. Sales by brand")
        print("10. Inventory performance")
        print("0. Exit")

        option = input("Select option: ")

        match option:
            case "1": mostrar_productos()
            case "2": agregar_producto()
            case "3": actualizar_producto()
            case "4": eliminar_producto()
            case "5": buscar_producto()
            case "6": registrar_venta()
            case "7": mostrar_ventas()
            case "8": top_3_productos()
            case "9": ventas_por_marca()
            case "10": rendimiento_inventario()
            case "0":
                print("Goodbye")
                break
            case _:
                print("Invalid option")


main()

