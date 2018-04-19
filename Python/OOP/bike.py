class Bike(object):
    def __init__(self, price, max_speed):
        self.price = price
        self.max = max_speed
        self.miles = 0
    def displayInfo(self):
        print self.price, self.max, self.miles
    def ride(self):
        print "Riding"
        self.miles += 10
        print "Miles:", self.miles
    def reverse(self):
        print "Reversing"
        if self.miles > 0:
            self.miles -= 5
        if self.miles <= 0:
            self.miles = 0
        print "Miles:", self.miles

bike1 = Bike(200, 25)
bike2 = Bike(400, 20)
bike3 = Bike(600, 25)

## Bike1
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

## Bike2
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

## Bike3
bike3.reverse()
bike3.reverse()
bike3.reverse()
bike3.displayInfo()