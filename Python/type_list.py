##l = ['magical unicorns',19,'hello',98.98,'world']
##l = [2,3,1,7,4,12]
##l = ['magical','unicorns']

sum = 0
m = ""

for item in l:
    if type(item) == str:
        m += item
    elif type(item) == int or type(item) == float:
        sum += item
    else:
        continue
print m
print "Sum:", sum

if sum == 0:
    print "The list you entered is of string type"
elif all(isinstance(item, (int, long)) for item in l):
    print "The list you entered is of integer type"
else:
    print "The list you entered is of mixed type"