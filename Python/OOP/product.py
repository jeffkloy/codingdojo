class Product(object):
    def __init__(self, price, item, weight, brand, status):
        self.price = price
        self.item = item
        self.weight = weight
        self.brand = brand
        self.status = status
    def sell(self):
        self.status = "sold"
        return self
    def add_tax(self, tax):
        self.tax = tax
        self.price = self.price + self.tax
        return self.price
    def return_product(self, return_product):
        self.return_product = return_product
        self.status = "for sale"
        return self
    def display_info(self):
        print "Price:", self.price
        print "Item name:", self.item
        print "Weight:", self.weight
        print "Brand:", self.brand
        print "Status:", self.status