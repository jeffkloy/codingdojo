class MathDojo(object):
    def __init__(self):
        self.result = 0
    def add(self, *args):
        for i in args:
            if type(i) == list or type(i) == tuple:
                for j in i:
                    self.result += j
            else:
                self.result += i
        return self
    def subtract(self, *args):
        return self

md = MathDojo()
print md.add(2).add(2,5).subtract(3,2).result