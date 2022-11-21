import os
import functions
import csv







try:
    with open("orders.csv", "r") as ords:
        reader = csv.DictReader(ords)
        orders = list(reader)
   

except:
    print("No order list found")




# Main Loop for calling the menu
while True:
    os.system("cls")
    menu = functions.ProductMenu()
    courier = functions.CourierMenu()
    order = functions.OrderMenu()
    match functions.mainmenu():        
        case 1:
            os.system("cls")
            menu.menu()
        case 2:
            os.system("cls")
            courier.menu()
        case 3:
            os.system("cls")
            order.menu()
        case 0:
            break
        case _:
            input("I didn't get that, press enter to continue")
            continue




