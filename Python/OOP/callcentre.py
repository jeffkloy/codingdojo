from datetime import datetime

class Call(object):
    def __init__(self, unique_id, name, number, reason):
        self.id = unique_id
        self.name = name
        self.number = number
        self.time = datetime.now()
        self.reason = reason
    def display(self):
        print "Unique ID:", self.id, "Name:", self.name, "Phone number:", self.number, "Time:", self.time, "Reason:", self.reason

class CallCentre(object):
    def __init__(self):
        super(CallCentre, self).__init__()
        self.calls = []
        self.queue = len(self.calls)
    def add(self, call):
        self.calls.append(self.calls)
    def remove(self, call):
        self.calls.remove(self.calls)
    def info(self):
        for call in self.calls:
            call.display()

call1 = Call(1, "Jeff K.", "+1 415-555-1212", "Callback")
call1.display()

callcentre1 = CallCentre()
callcentre1.add(1)
callcentre1.remove(call1)
print callcentre1.info()