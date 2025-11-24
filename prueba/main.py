from fucionamiento import add_product, show_product, update_product, delete_product, search_name
from ventas import register_sale, show_sales
from reportes import inventory_performance, ventas_por_book, top_3_productos

def main():
    while True:    
        print("==Menu==")
        print("1-Register book-")
        print("2-Update book-")
        print("3-Delete book-")
        print("4-View books-")
        print("5-Search book-")
        print("6-Register sales-")
        print("7-Show sales-")
        print("8-Top 3 productos-")
        print ("9-inventory Performance-")
        print("10-Ventas por Book-")
        print("11-Exit-")

        option=(input("Select the option number: "))

        match option:
            case "1": add_product()
            case "2": update_product()
            case "3": delete_product()
            case "4": show_product()
            case "5": search_name()
            case "6": register_sale()
            case "7": show_sales()
            case "8": top_3_productos()
            case "9": inventory_performance()
            case "10": ventas_por_book()

        
            case "11":
                print("exit")
                break
            case _:
                print("invalid option")

main()

