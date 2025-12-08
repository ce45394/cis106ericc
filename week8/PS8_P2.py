class Car:
    def __init__(self, make, model, sticker_price):
        self.make = make
        self.model = model
        self.sticker_price = sticker_price

    def discount_price(self):
        return self.sticker_price * 0.90


# Derived Sport class
class Sport(Car):
    def __init__(self, make, model, sticker_price):
        super().__init__(make, model, sticker_price)
        self.total_price = self.discount_price()

    def SportWheels(self, option):
        if option == "Y":
            self.total_price += 1000

    def SportEngine(self, option):
        if option == "Y":
            self.total_price += 3000

    def SportInterior(self, option):
        if option == "Y":
            self.total_price += 2000

    def pricewithoptions(self):
        print("Car:", self.make, self.model)
        print("Final Price with Options: $", self.total_price)


# Test the Sport class
sport_car = Sport("1972 Ford", "Maverick", 40000)

sport_car.SportWheels("Y")
sport_car.SportEngine("Y")
sport_car.SportInterior("N")

sport_car.pricewithoptions()
