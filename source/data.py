import os
import functions
import csv

product = []
orders = []
couriers = []
orders_fields = ["customer_name", "customer_address", "customer_phone", "courier", "status"]

# Opens the saved product data and adds it to be used in program
with open("product.txt", "r") as prod:
    for products in prod:
        product.append(products.strip())

with open("courier.txt", "r") as cour:
    for courier in cour:
        couriers.append(courier.strip())

# Opens the saved order data and adds it to be used in program
try:
    with open("orders.csv", "r") as ords:
        reader = csv.DictReader(ords)
        orders = list(reader)

except:
    print("No order list found")

menu = functions.ProductMenu(product)
order = functions.OrderMenu(orders, couriers)
courier = functions.CourierMenu(couriers)

# Main Loop for calling the menu
while True:
    os.system("cls")
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
with open("product.txt", "w") as prod:
    for products in menu.list:
        prod.write(f"{products} \n")

with open("courier.txt", "w") as cour:
    for couriers in courier.list:
        cour.write(f"{couriers} \n")

with open("orders.csv", "w") as ords:
    writer = csv.DictWriter(ords, fieldnames=orders_fields)
    writer.writeheader()
    writer.writerows(order.list)
