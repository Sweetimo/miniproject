import functions

couriers = []

couriers = functions.CourierMenu(couriers)

def test_couriers_deleteCourier():
    list = [{"name": "John", "phone" : "01614444444"}, {"name": "James", "phone" : "01613214444"}]
    excepted = [{"name": "John", "phone" : "01614444444"}]
    result = couriers.deleteCourier(list, 1)
    print(result)
    print("success")
    assert excepted == result

test_couriers_deleteCourier()
