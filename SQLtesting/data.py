import os
import functions
import csv


orders = []

orders_fields = ["customer_name", "customer_address", "customer_phone", "courier", "status", "product"]




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
    order = functions.OrderMenu(orders)
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

# Saves the product and order data to a file


with open("orders.csv", "w") as ords:
    writer = csv.DictWriter(ords, fieldnames=orders_fields)
    writer.writeheader()
    writer.writerows(order.list)
