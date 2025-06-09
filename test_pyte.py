class test_shop:
    product = "Laptop"  # Class variable


    def constmer(self,brand,price,warranty):
        self.brand=brand
        self.price = price
        self.warranty=warranty
        #printing entered values or inputs
        print(f"Brand : {self.brand}")
        print(f"Price : {self.price}")
        print(f"Warranty : {self.warranty}")

#crete a child class calling the parent class
class shop_child(test_shop): # inheritance

    def test_brand_assignment(self):
        valid_brands = ['HP', 'DELL', 'LENOVO', 'ACER']

        brand = input("Enter Laptop Brand Searching for : ").upper()

        if brand in valid_brands:
            print("Laptop Brand is available")
        else:
            print("Laptop Brand is not available")
            return
        price = input("Enter price range you want (₹): ")
        warranty = input("Enter warranty detail in years : ")
        obj = test_shop()
        print(obj.product)
        obj.constmer(brand, price, warranty)
        assert True

def test_run():
    obj = shop_child()
    obj.test_brand_assignment()






