class Customer:
    name = ""
    lastName = ""
    age = 0

    def addCart(self):
        print("Added to " +self.name+ " " + self.lastName + "'s cart")

customer1 = Customer()
customer1.name = "Artittaya"
customer1.lastName = "Duangtawan"
customer1.age = 17
customer1.addCart()

customer2 = Customer()
customer2.name = "Norrarat"
customer2.lastName = "Phudphad"
customer2.age = 17
customer2.addCart()

customer3 = Customer()
customer3.name = "Jirakarn"
customer3.lastName = "Nukboon"
customer3.age = 17
customer3.addCart()

customer4 = Customer()
customer4.name = "Benyapa"
customer4.lastName = "Martsurok"
customer4.age = 18
customer4.addCart()