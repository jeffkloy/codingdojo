class Car(object):
    def __init__(self, price, speed, fuel, mileage):
        self.price = price
        self.speed = speed
        self.fuel = fuel
        self.mileage = mileage
        if self.price > 10000:
            self.price *= 1.15
        if self.price <= 9999:
            self.price *= 1.12
    def display_all(self):
        print "Price:", self.price
        print "Speed:", self.speed
        print "Fuel:", self.fuel
        print "Mileage:", self.mileage

car1 = Car(2000, 35, "Full", "15mpg")
car2 = Car(2000, 5, "Not Full", "105mpg")
car3 = Car(2000, 15, "Kind of Full", "95mpg")
car4 = Car(2000, 25, "Full", "25mpg")
car5 = Car(2000, 45, "Empty", "25mpg")
car6 = Car(20000000, 35, "Empty", "15mpg")

print "Car 1:", car1.display_all()
print "Car 2:", car2.display_all()
print "Car 3:", car3.display_all()
print "Car 4:", car4.display_all()
print "Car 5:", car5.display_all()
print "Car 6:", car6.display_all()