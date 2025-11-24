from fucionamiento import add_product, show_product, update_product, delete_product

def main():
    while True:    
        print("==Menu==")
        print("1-Register-")
        print("2-Update-")
        print("3-Delete-")
        print("4-View-")
        print("5-Exit-")

        option=(input("Select the option number: "))

        match option:
            case "1": add_product()
            case "2": update_product()
            case "3": delete_product()
            case "4": show_product()

        
            case "5":
                print("exit")
                break

main()

