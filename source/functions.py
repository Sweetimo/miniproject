import os
import csv
import pandas as pd


# Class that handles the project menu
class ProductMenu():

    def __init__(self, product):
        self.list = product
        

    def menu(self):

        while True:
            
            self.pdf = pd.DataFrame(self.list)
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
                self.showlist(self.pdf)
            # Add Product
            elif product_menu_selection == 2:
                while True:
                    os.system("cls")
                    
                    name = input("Please enter the names of the products you sell: \n")
                    price = input("How much does that cost: \n")
                    
                    self.list = self.addproduct(self.list, name, price)
                    product_fields = ["name", "price"]
                    
                    self.pdf = pd.DataFrame(self.list)
                    os.system("cls")
                    print(self.pdf.to_string())
                    another_product = ""
                    while another_product != "y" and another_product != "n":
                        another_product = input("Add another product: y or n:\n").lower()
                    if another_product == "n":
                        os.system("cls")
                        break
                    if another_product == "n":
                        break
                

            # Update Product
            elif product_menu_selection == 3:
                print(self.pdf.to_string())
                while True:
                    if len(self.list) <= 0:
                        print("There are no products")
                        input("Press enter to continue")
                        break
                    prod_index = input("Which product would you like to change, enter the index number: ")
                    try:
                        prod_index = int(prod_index)
                        print(list[prod_index])
                    except:
                        print("That product doesn't exit")
                        continue
                    else:
                        for keys in self.list[prod_index].keys():
                            print(self.list[prod_index][keys])
                            update = input(f"{keys} What would you like to change this to?\n")
                            if update != "":
                                self.list = self.changeproduct(self.list,prod_index,keys,update )
                        break

            # Delete Product
            elif product_menu_selection == 4:
                print(self.pdf.to_string())
                while True:
                    if len(self.list) <= 0:
                        print("There are no products")
                        input("Press enter to continue")
                        break
                    prod_index = input("Which product would you like to delete, enter the index number: ")
                    try:
                        prod_index = int(prod_index)
                        print(f"{self.list[prod_index]} has been removed")
                    except:
                        print("That product doesn't exit")
                        continue
                    else:
                        self.list = self.deleteproduct(self.list, prod_index)
                        break
                    

            elif product_menu_selection == 0:
                product_fields = ["id","name", "price"]
                with open("product.csv", "w") as prod:
                    writer = csv.DictWriter(prod, fieldnames=product_fields)
                    writer.writeheader()
                    writer.writerows(self.list)
                
                break

    def showlist(self,df):
        print(df)
        input("Press enter to return")
        os.system("cls")

    def addproduct(self,list, name, price):
        while True:
            
            product_dictionary = {}
            product_dictionary["id"] = len(list) + 1
            product_dictionary["name"] = name
            product_dictionary["price"] = price
            list.append(product_dictionary)
            self.pdf = pd.DataFrame(self.list)
            
            return list

    def changeproduct(self,list,prod_index,keys,update):
        
                list[prod_index][keys] = update
                return list

    def deleteproduct(self, list, prod_index):
        
                del list[prod_index]
                return list

class CourierMenu():

    def __init__(self, Courier):
        self.list = Courier
        self.cdf = pd.DataFrame(self.list)

    def menu(self):

        while True:
            courier_fields = ["name", "phone"]
            
            self.cdf = pd.DataFrame(self.list)
            print("""
Courier Menu:
0. Return to main menu.
1. Show the list of Couriers.
2. Add a Courier to the list.
3. Update a Courier.
4. Delete a Courier.
                """)
            Courier_menu_selection = input()
            try:
                int(Courier_menu_selection)

            except ValueError:
                print("That was an invalid selection")
                continue
            else:
                if int(Courier_menu_selection) > 4:
                    print("That was an invalid selection")
                    continue
                else:
                    Courier_menu_selection = int(Courier_menu_selection)
                    os.system("cls")

            # Show Courier List
            if Courier_menu_selection == 1:
                self.showlist(self.cdf)
            # Add Courier
            elif Courier_menu_selection == 2:
                while True:
                    
                    name = input("Please enter the names of the courier: \n")
                    phone ="#" + input("What is their phone number: \n")
                    
                    self.list = self.addCourier(self.list, name, phone)
                    
                    another_Courier = ""
                    while another_Courier != "y" and another_Courier != "n":
                        another_Courier = input("Add another Courier: y or n:\n").lower()
                    if another_Courier == "n":
                        os.system("cls")
                        break
                

            # Update Courier
            elif Courier_menu_selection == 3:
                print(self.cdf.to_string())
                while True:
                    if len(self.list) <= 0:
                        print("There are no Couriers")
                        input("Press enter to continue")
                        break
                    Courier_index = input("Which Courier would you like to change, enter the index number: ")
                    try:
                        Courier_index = int(Courier_index)
                        print(list[Courier_index])
                    except:
                        print("That Courier doesn't exit")
                        continue
                    else:
                        for keys in self.list[Courier_index].keys():
                            print(self.list[Courier_index][keys])
                            update = input(f"{keys} What would you like to change this to?\n")
                            if update != "":
                               self.list = self.changeCourier(self.list,Courier_index,keys,update)
                        break

            # Delete Courier
            elif Courier_menu_selection == 4:
                print(self.cdf.to_string())
                while True:
                    if len(self.list) <= 0:
                        print("There are no Couriers")
                        input("Press enter to continue")
                        break
                    Courier_index = input("Which Courier would you like to delete, enter the index number: ")
                    try:
                        Courier_index = int(Courier_index)
                        print(f"{self.list[Courier_index]} has been removed")
                    except:
                        print("That Courier doesn't exit")
                        continue
                    else:
                        self.list = self.deleteCourier(self.list, Courier_index)
                        break

            elif Courier_menu_selection == 0:
                courier_fields = ["id","name", "phone"]
                with open("courier.csv", "w") as cour:
                    writer = csv.DictWriter(cour, fieldnames=courier_fields)
                    writer.writeheader()
                    writer.writerows(self.list)
                self.cdf = pd.DataFrame(self.list)
                break

    def showlist(self, df):
        print(df)
        input("Press enter to return")
        os.system("cls")

    def addCourier(self, list, name, phone):
        while True:
            courier_dictionary = {}
            courier_dictionary["id"] = len(list) + 1
            courier_dictionary["name"] = name
            courier_dictionary["phone"] = phone
            list.append(courier_dictionary)
            
            self.cdf = pd.DataFrame(self.list)
            return list

    def changeCourier(self, list, Courier_index, keys, update):
                list[Courier_index][keys] = update
                return list

    def deleteCourier(self, list, courier_index):

                del list[courier_index]
                return list



# Class that handles the order menu
class OrderMenu():

    def __init__(self, order, courier, product):
        self.list = order
        self.clist = courier
        self.plist = product
        self.pdf = pd.DataFrame(self.plist)
        self.cdf = pd.DataFrame(self.clist)
        self.df = pd.DataFrame(self.list)

    def menu(self):
        while True:
            
            self.df = pd.DataFrame(self.list)
            self.pdf = pd.DataFrame(self.plist)
            self.cdf = pd.DataFrame(self.clist)
            print("""
Orders Menu:
0. Return to main menu.
1. Show the list of Orders.
2. Add an Order.
3. Update order status.
4. Update order contents.
5. Delete an order.
                """)
            menu_selection = input()
            try:
                int(menu_selection)

            except ValueError:
                print("That was an invalid selection")
                continue
            else:
                if int(menu_selection) > 5:
                    print("That was an invalid selection")
                    continue
                else:
                    menu_selection = int(menu_selection)
                    os.system("cls")

            # Show Order List
            if menu_selection == 1:
                self.showlist()
            # Add Order
            elif menu_selection == 2:
                while True:
                    productlist= []
                    os.system("cls")
                    name = input("Please enter the name of the customer: \n")
                    address = input("Please enter the customers address: \n")
                    phone = "#" + input("Please enter the customers phone number: \n")
                    print(self.cdf.to_string())
                    cour = input("Please enter the index number for the courier to use: \n")
                    
                    print(self.pdf.to_string())    
                    
                    while True:
                        product_index= input("Please enter the products in this order by index: \n")
                        try:
                            productlist.append(int(product_index))
                        except:
                            print("That was an invalid selction")
                            continue    
                        else:
                            another_product = ""
                            while another_product != "y" and another_product != "n":   
                                another_product = input("Add another product: y or n:\n").lower()
                            if another_product == "n":                                        
                                break

                    self.list = self.addorder(self.list,name, address, phone, cour, productlist)
                    another_order = ""
                    while another_order != "y" and another_order != "n":
                        another_order = input("Add another order: y or n:\n").lower()
                    if another_order == "n":
                        os.system("cls")
                        break
                        

            # Update Update order status
            elif menu_selection == 3:
                while True:
                    status_list = ["Preparing", "Out of the Oven", "On it's way", "Delivered"]
                    if len(self.list) <= 0:
                        print("There are no orders")
                        input("Press enter to continue")
                        break
                    print(self.df.to_string())
                    orders_index = input("Which order would you like to change, enter the index number: ")
                    try:
                        orders_index = int(orders_index)
                        print(self.list[orders_index])
                    except:
                        print("That order doesn't exit")
                        continue
                    else:
                        while True:
                            for i in range(len(status_list)):
                                print(f"{i}: {status_list[i]}")
                            status_index = input("What would you like to change status to, enter the index number: ")
                            try:
                                status_index = int(status_index)
                                print(self.list[orders_index])
                            except:
                                print("That was an invalid selection")
                                continue
                            else:
                                self.list = self.changeorder(self.list,orders_index,status_index)
                                break
                        break

            # Update Customer Information
            elif menu_selection == 4:
                
                print(self.df.to_string())
                while True:
                    if len(self.list) <= 0:
                        print("There are no orders")
                        input("Press enter to continue")
                        break
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
                                    self.list = self.updateorder(self.list, orders_index, keys, update)
                        orders_fields = ["customer_name", "customer_address", "customer_phone", "courier", "status", "product"]
                        self.df = pd.DataFrame(self.list)
                        break

            # Delete Order
            elif menu_selection == 5:
                print(self.df.to_string())
                while True:
                    if len(self.list) <= 0:
                        print("There are no Orders")
                        input("Press enter to continue")
                        break
                    prod_index = input("Which order would you like to delete, enter the index number: ")
                    try:
                        prod_index = int(prod_index)
                        
                    except:
                        print("That order doesn't exit")
                        continue
                    else:
                        input(f"{self.list[prod_index]} has been removed")
                        self.list = self.deleteorder(self.list, prod_index)
                        break

            elif menu_selection == 0:
                orders_fields = ["customer_name", "customer_address", "customer_phone", "courier", "status", "product"]
                with open("orders.csv", "w") as ords:
                    writer = csv.DictWriter(ords, fieldnames=orders_fields)
                    writer.writeheader()
                    writer.writerows(self.list)
                break

    def showlist(self):
        status_list = ["preparing", "Out of the Oven", "On it's way", "Delivered"]        
        while True:
            print("""
Orders Menu:
0. Return to main menu.
1. Show all orders.
2. Show orders by courier.
3. Show orders by status.
                """)
            menu_selection = input()
            try:
                int(menu_selection)

            except ValueError:
                print("That was an invalid selection")
                continue
            else:
                if int(menu_selection) > 3:
                    print("That was an invalid selection")
                    continue
                else:
                    menu_selection = int(menu_selection)
                    os.system("cls")
                if menu_selection == 1:
                    print(self.df)
                    input("Press enter to return")
                    os.system("cls")
                    return
                elif menu_selection ==2:
                    templist = []
                    print(self.cdf.to_string)
                    Courier_index = input("Which Courier would you like to see orders for, enter the index number: ")
                    try:
                        Courier_index = int(Courier_index)                        
                    except:
                        print("That Courier doesn't exit")
                        continue
                    else:
                        for i in range(len(self.list)):
                            if self.list[i]["courier"] == str(Courier_index):
                                templist.append(self.list[i])
                        print(pd.DataFrame(templist))
                        input("Press enter to return")
                        os.system("cls")
                        return
                elif menu_selection == 3:
                    templist = []
                    for i in range(len(status_list)):
                        print(f"{i}: {status_list[i]}")
                    status_index = input("Which status would you like to see orders for, enter the index number: ")
                    try:
                        status_index = int(status_index)                        
                    except:
                        print("That Courier doesn't exit")
                        continue
                    else:
                        for i in range(len(self.list)):
                            if self.list[i]["status"] == status_list[status_index]:
                                templist.append(self.list[i])
                        print(pd.DataFrame(templist).to_string())
                        input("Press enter to return")
                        os.system("cls")
                        return
                elif menu_selection == 0:
                    return
                        

        

    def addorder(self,list,cname,caddress,cphone,cour,cproduct):
        while True:
            order_dictionary = {}
            
            order_dictionary["customer_name"] = cname
            order_dictionary["customer_address"] = caddress
            order_dictionary["customer_phone"] = "#" + cphone
            order_dictionary["courier"] = cour
            order_dictionary["status"] = "preparing"
            order_dictionary["product"] = (', '.join(str(x) for x in cproduct))        
                       
            list.append(order_dictionary)
            
            return list

    def changeorder(self,list,orders_index, status_index):
            status_list = ["Preparing", "Out of the Oven", "On it's way", "Delivered"]
            list[orders_index]["status"] = status_list[status_index]
            
            return list

    def updateorder(self, list, orders_index, keys, update):        
                list[orders_index][keys] = update
                return list

    def deleteorder(self, list, prod_index):
       
                del list[prod_index]
                return list


# Function to call the main menu
def mainmenu():
    while True:
        print("""
Main Menu:
1. Product Menu
2. Courier Menu
3. Orders


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