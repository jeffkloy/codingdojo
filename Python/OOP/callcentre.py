from datetime import datetime

class Call(object):
    unique_id = 0
    def __init__(self, name, number, reason):
        self.id = Call.unique_id
        self.name = name
        self.number = number
        self.time = datetime.now()
        self.reason = reason
        Call.unique_id += 1
    def display(self):
        print "#" * 30
        print "Unique ID:", self.id
        print "Name:", self.name
        print "Phone number:", self.number
        print "Time:", self.time
        print "Reason:", self.reason
        print "#" * 30

class CallCentre(object):
    def __init__(self):
        super(CallCentre, self).__init__()
        self.calls = []
        self.queue = len(self.calls)
    def add(self, Call):
        self.calls.append(self.calls)
    def remove(self, Call):
        self.calls.remove(self.calls)
    def info(self, Call):
        print Call.display.unique_id
        print Call.display.name
        print Call.display.number

call1 = Call("Jeff K.", "+1 415-555-1212", "Callback")
call1.display()

callcentre1 = CallCentre()
callcentre1.add(call1)
callcentre1.remove([0])
callcentre1.info()