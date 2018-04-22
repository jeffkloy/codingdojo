class Call(object):
    def __init__(self, unique_id, name, number, time, reason):
        self.id = unique_id
        self.name = name
        self.number = number
        self.time = time
        self.reason = reason
    def display(self):
        print "Unique ID:", self.id, "Name:", self.name, "Phone number:", self.number, "Time:", self.time, "Reason:", self.reason

class CallCentre(Call):
    def __init__(self, calls, queue):
        super(CallCentre, self).__init__()
        self.calls = []
        self.queue = len(self.calls)
    def add(self):
        self.calls.append()
    def remove(self):
        self.calls.pop()
    def info(self):
        print "Name:", self.name, "Phone number:", self.number, "Queue length:", self.calls

call1 = Call(1, "Jeff", 14157452146, 201804211927, "Callback")
call1.display()

callcentre1 = CallCentre(0, 0)
callcentre1.add()
print callcentre1
callcentre1.remove()
print callcentre1.info()
