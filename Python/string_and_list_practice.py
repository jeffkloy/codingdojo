words = "It's thanksgiving day. It's my birthday,too!"
print words.find('day')
new_words = words.replace("day","month")
print new_words

x = [2,54,-2,7,12,98]
print min(x)
print max(x)

x = ["hello",2,54,-2,7,12,98,"world"]
new_x = x[0] + ', ' + x[-1]
print new_x

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
y = x[:len(x)/2]
z = x[len(x)/2:]
x.insert(0, y)
print x
