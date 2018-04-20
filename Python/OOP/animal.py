class Animal(object):
    def __init__(self, name, health):
        self.name = name
        self.health = health
    def walk(self):
        self.health -= 1
    def run(self):
        self.health -= 5
    def display(self):
        print "Health -", self.health

class Dog(Animal):
    def __init__(self):
        self.health = 150
    def pet(self):
        self.health += 5

class Dragon(Animal):
    def __init__(self):
        self.health = 170
    def fly(self):
        self.health -= 10
    def display_health(self):
        print "Health -", self.health
        print "I am a Dragon"

dog1 = Dog()

print "Dog:"
dog1.walk() ## 150 - 1 = 149
dog1.walk() ## 149 - 1 = 148
dog1.walk() ## 148 - 1 = 147
dog1.run() ## 147 - 5 = 142
dog1.run() ## 142 - 5 = 137
dog1.pet() ## 137 + 5 = 142
dog1.display() ## 142

print "Dragon:"
dragon1 = Dragon()
dragon1.display_health() ## "I am a Dragon"