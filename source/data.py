import os
import functions
import csv

product = []
orders = []
couriers = []
orders_fields = ["customer_name", "customer_address", "customer_phone", "courier", "status", "product"]
product_fields = ["name", "price"]
courier_fields = ["name", "phone"]


# Opens the saved product data and adds it to be used in program
try:
    with open("product.csv", "r") as prod:
        reader = csv.DictReader(prod)
        product = list(reader)

except:
    print("No product list found")

try:
    with open("courier.csv", "r") as cour:
        reader = csv.DictReader(cour)
        couriers = list(reader)

except:
    print("No courier list found")

# Opens the saved order data and adds it to be used in program
try:
    with open("orders.csv", "r") as ords:
        reader = csv.DictReader(ords)
        orders = list(reader)

except:
    print("No order list found")




# Main Loop for calling the menu
while True:
    os.system("cls")
    menu = functions.ProductMenu(product)
    courier = functions.CourierMenu(couriers)
    order = functions.OrderMenu(orders, courier.list, menu.list)
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

with open("product.csv", "w") as prod:
    writer = csv.DictWriter(prod, fieldnames=product_fields)
    writer.writeheader()
    writer.writerows(menu.list)

with open("courier.csv", "w") as cour:
    writer = csv.DictWriter(cour, fieldnames=courier_fields)
    writer.writeheader()
    writer.writerows(courier.list)

with open("orders.csv", "w") as ords:
    writer = csv.DictWriter(ords, fieldnames=orders_fields)
    writer.writeheader()
    writer.writerows(order.list)
