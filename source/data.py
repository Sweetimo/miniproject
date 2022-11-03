import os
import functions
import csv

product = []
orders = []
orders_fields = ["customer_name", "customer_address", "customer_phone", "status"]

# Opens the saved product data and adds it to be used in program
with open("e:\MiniProject\miniproject\source\product.txt", "r") as prod:
    for products in prod:
        product.append(products.strip())

# Opens the saved order data and adds it to be used in program
try:
    with open("e:\MiniProject\miniproject\source\orders.csv", "r") as ords:
        reader = csv.DictReader(ords)
        orders = list(reader)

except:
    print("No order list found")

menu = functions.ProductMenu(product)
order = functions.OrderMenu(orders)

# Main Loop for calling the menu
while True:
    os.system("cls")
    match functions.mainmenu():
        case 1:
            os.system("cls")
            menu.menu()
        case 2:
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

with open("e:\MiniProject\miniproject\source\orders.csv", "w") as ords:
    writer = csv.DictWriter(ords, fieldnames=orders_fields)
    writer.writeheader()
    writer.writerows(order.list)
