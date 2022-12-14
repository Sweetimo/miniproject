import functions
import unittest

couriers = []
product = []
order = []
courier = functions.CourierMenu(couriers)
products = functions.ProductMenu(product)
orders = functions.OrderMenu(order, couriers, product)

class Test_Test_MiniProject(unittest.TestCase):

    def test_products_addproduct(self):
        name = "fanta"
        price = "1.99"
        list = [{"name": "Curry", "price" : "4.50"}, {"name": "cola", "price" : "1.99"}]
        excepted = [{"name": "Curry", "price" : "4.50"}, {"name": "cola", "price" : "1.99"}, {"name": "fanta", "price" : "1.99"}]
        result = products.addproduct(list, name, price)
        print(result)
        print("success")
        assert excepted == result

    

    def test_products_changeproduct(self):
        key = "name"
        update = "Soup"
        list = [{"name": "Curry", "price" : "4.50"}, {"name": "cola", "price" : "1.99"}]
        excepted = [{"name": "Soup", "price" : "4.50"}, {"name": "cola", "price" : "1.99"}]
        result = products.changeproduct(list,0,key,update)
        print("success")
        print(result)
        assert excepted == result

    

    def test_products_deleteproduct(self):

        list = [{"name": "Curry", "price" : "4.50"}, {"name": "cola", "price" : "1.99"}]
        excepted = [{"name": "cola", "price" : "1.99"}]
        result = products.deleteproduct(list,0)
        print("success")
        print(result)
        assert excepted == result

    

    def test_courier_addCourier(self):
        name = "fisher"
        phone = "19909990999"
        list = [{"name": "John", "phone" : "01614444444"}, {"name": "James", "phone" : "01613214444"}]
        excepted = [{"name": "John", "phone" : "01614444444"}, {"name": "James", "phone" : "01613214444"}, {"name": "fisher", "phone" : "19909990999"}]
        result = courier.addCourier(list, name, phone)
        print(result)
        print("success")
        assert excepted == result

    

    def test_courier_changeCourier(self):
        key = "name"
        update = "Sol"
        list = [{"name": "John", "phone" : "01614444444"}, {"name": "James", "phone" : "01613214444"}]
        excepted = [{"name": "Sol", "phone" : "01614444444"}, {"name": "James", "phone" : "01613214444"}]
        result = courier.changeCourier(list,0,key,update)
        print("success")
        print(result)
        assert excepted == result

   

    def test_couriers_deleteCourier(self):
        list = [{"name": "John", "phone" : "01614444444"}, {"name": "James", "phone" : "01613214444"}]
        excepted = [{"name": "John", "phone" : "01614444444"}]
        result = courier.deleteCourier(list, 1)
        print(result)
        print("success")
        assert excepted == result

    

    def test_orders_addorder(self):
        list =[] 
        name = "fisher"
        phone = "19909990999"
        address = "19 Maple street"
        courier = 1
        product = [1,2]
        expected = [{"customer_name" : "fisher", "customer_address":"19 Maple street", "customer_phone" : "#19909990999", "courier" : 1, "status": "preparing","product" : "1, 2" }]
        result = orders.addorder(list, name, address, phone, courier, product)
        print(result)
        print("success")
        assert expected == result
    
    def test_orders_changeorder(self):
        list = [{"customer_name" : "fisher", "customer_address":"19 Maple street", "customer_phone" : "#19909990999", "courier" : 1, "status": "preparing","product" : "1, 2" }]
        expected = [{"customer_name" : "fisher", "customer_address":"19 Maple street", "customer_phone" : "#19909990999", "courier" : 1, "status": "Delivered","product" : "1, 2" }]
        result = orders.changeorder(list,0,3)
        print(result)
        print("success")
        assert expected == result

    

    def test_orders_updateorder(self):
        key = "customer_name"
        update = "Sol"
        list = [{"customer_name" : "fisher", "customer_address":"19 Maple street", "customer_phone" : "#19909990999", "courier" : 1, "status": "preparing","product" : "1, 2" }]
        expected = [{"customer_name" : "Sol", "customer_address":"19 Maple street", "customer_phone" : "#19909990999", "courier" : 1, "status": "preparing","product" : "1, 2" }]
        result = orders.updateorder(list, 0, key , update)
        print("success")
        print(result)
        assert expected == result
    
        
    def test_orders_deleteorder(self):
        list = [{"customer_name" : "fisher", "customer_address":"19 Maple street", "customer_phone" : "#19909990999", "courier" : 1, "status": "preparing","product" : "1, 2" }]
        expected = []
        result = orders.deleteorder(list, 0)
        print("success")
        print(result)
        assert expected == result
    
