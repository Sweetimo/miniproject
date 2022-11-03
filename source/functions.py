import os
import csv
import pandas as pd


# Class that handles the project menu
class ProductMenu():

    def __init__(self, product):
        self.list = product

    def menu(self):

        while True:
            with open("e:\MiniProject\miniproject\source\product.txt", "w") as prod:
                for products in self.list:
                    prod.write(f"{products} \n")
            print("""
Product Menu:
0. Return to main menu.
1. Show the list of products.
2. Add a product to the list.
3. Update a Product.
4. Delete a Product.
                """)
            product_menu_selection = input()
            try:
                int(product_menu_selection)

            except ValueError:
                print("That was an invalid selection")
                continue
            else:
                if int(product_menu_selection) > 4:
                    print("That was an invalid selection")
                    continue
                else:
                    product_menu_selection = int(product_menu_selection)
                    os.system("cls")

            # Show Product List
            if product_menu_selection == 1:
                self.showlist()
            # Add Product
            elif product_menu_selection == 2:
                self.addproduct()

            # Update Product
            elif product_menu_selection == 3:
                self.changeproduct()

            # Delete Product
            elif product_menu_selection == 4:
                self.deleteproduct()

            elif product_menu_selection == 0:
                break

    def showlist(self):
        for i in range(len(self.list)):
            print(f"{i}: {self.list[i]}")
        input("Press enter to return")
        os.system("cls")

    def addproduct(self):
        while True:
            os.system("cls")
            self.list.append(input("Please enter the names of the products you sell: \n"))
            os.system("cls")
            print(self.list)
            another_product = ""
            while another_product != "y" and another_product != "n":
                another_product = input("Add another product: y or n:\n").lower()
            if another_product == "n":
                os.system("cls")
                return list

    def changeproduct(self):
        for i in range(len(self.list)):
            print(f"{i}: {self.list[i]}")
        while True:
            if len(self.list) <= 0:
                print("There are no products")
                input("Press enter to continue")
                return self.list
            prod_index = input("Which product would you like to change, enter the index number: ")
            try:
                prod_index = int(prod_index)
                print(list[prod_index])
            except:
                print("That product doesn't exit")
                continue
            else:
                list[prod_index] = input("What would you like to change this to?: ")
                return list

    def deleteproduct(self):
        for i in range(len(self.list)):
            print(f"{i}: {self.list[i]}")
        while True:
            if len(self.list) <= 0:
                print("There are no products")
                input("Press enter to continue")
                return self.list
            prod_index = input("Which product would you like to delete, enter the index number: ")
            try:
                prod_index = int(prod_index)
                print(f"{self.list[prod_index]} has been removed")
            except:
                print("That product doesn't exit")
                continue
            else:
                del self.list[prod_index]
                return self.list


# Class that handles the order menu
class OrderMenu():

    def __init__(self, order):
        self.list = order
        self.df = pd.read_csv("e:\MiniProject\miniproject\source\orders.csv")

    def menu(self):
        while True:
            orders_fields = ["customer_name", "customer_address", "customer_phone", "status"]
            with open("e:\MiniProject\miniproject\source\orders.csv", "w") as ords:
                writer = csv.DictWriter(ords, fieldnames=orders_fields)
                writer.writeheader()
                writer.writerows(self.list)
            self.df = pd.read_csv("e:\MiniProject\miniproject\source\orders.csv")
            print("""
Orders Menu:
0. Return to main menu.
1. Show the list of Orders.
2. Add an Order.
3. Update order status.
4. Update order contents.
5. Delete an order.
                """)
            product_menu_selection = input()
            try:
                int(product_menu_selection)

            except ValueError:
                print("That was an invalid selection")
                continue
            else:
                if int(product_menu_selection) > 5:
                    print("That was an invalid selection")
                    continue
                else:
                    product_menu_selection = int(product_menu_selection)
                    os.system("cls")

            # Show Order List
            if product_menu_selection == 1:
                self.showlist()
            # Add Order
            elif product_menu_selection == 2:
                self.addorder()

            # Update Update order status
            elif product_menu_selection == 3:
                self.changeorder()

            # Update Customer Information
            elif product_menu_selection == 4:
                self.updateorder()

            # Delete Order
            elif product_menu_selection == 5:
                self.deleteorder()

            elif product_menu_selection == 0:
                break

    def showlist(self):
        print(self.df.to_string())
        input("Press enter to return")
        os.system("cls")

    def addorder(self):
        while True:
            order_dictionary = {}
            os.system("cls")
            order_dictionary["customer_name"] = input("Please enter the name of the customer: \n")
            order_dictionary["customer_address"] = input("Please enter the customers address: \n")
            order_dictionary["customer_phone"] = input("Please enter the customers phone number: \n")
            order_dictionary["status"] = "preparing"
            self.list.append(order_dictionary)
            os.system("cls")
            self.df = pd.read_csv("e:\MiniProject\miniproject\source\orders.csv")
            print(self.df.to_string())
            another_product = ""
            while another_product != "y" and another_product != "n":
                another_product = input("Add another order: y or n:\n").lower()
            if another_product == "n":
                os.system("cls")
                return list

    def changeorder(self):
        print(self.df.to_string())
        while True:
            if len(self.list) <= 0:
                print("There are no orders")
                input("Press enter to continue")
                return self.list
            orders_index = input("Which order would you like to change, enter the index number: ")
            try:
                orders_index = int(orders_index)
                print(self.list[orders_index])
            except:
                print("That order doesn't exit")
                continue
            else:
                self.list[orders_index]["status"] = input("What would you like to change this to?: ")
                return list

    def updateorder(self):
        print(self.df.to_string())
        while True:
            if len(self.list) <= 0:
                print("There are no products")
                input("Press enter to continue")
                return self.list
            orders_index = input("Which order details would you like to change, enter the index number: ")
            try:
                orders_index = int(orders_index)
                print(self.list[orders_index])
            except:
                print("That order doesn't exit")
                continue
            else:
                for keys in self.list[orders_index].keys():
                    if keys != "status":
                        print(self.list[orders_index][keys])
                        update = input(f"{keys} What would you like to change this to?\n")
                        if update != "":
                            self.list[orders_index][keys] = update

                return list

    def deleteorder(self):
        print(self.df.to_string())
        while True:
            if len(self.list) <= 0:
                print("There are no products")
                input("Press enter to continue")
                return self.list
            prod_index = input("Which product would you like to delete, enter the index number: ")
            try:
                prod_index = int(prod_index)
                print(f"{self.list[prod_index]} has been removed")
            except:
                print("That product doesn't exit")
                continue
            else:
                del self.list[prod_index]
                return self.list


# Function to call the main menu
def mainmenu():
    while True:
        print("""
Main Menu:
1. Product Menu
2. Orders


0. Exit
            """)
        menu_selection = input()
        try:
            int(menu_selection)
        except ValueError:
            print("That was an invalid selection")
            continue
        else:
            return int(menu_selection)

class Orders():

    def __init__(self, name, address, phone_no, order, order_status):
        pass