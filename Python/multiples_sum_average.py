## Multiples

for i in range(1, 1000):
    if i % 2 == 1:
        print i

for j in range(5, 1000001):
    if j % 5 == 0:
        print j

## Sum
a = [1, 2, 5, 10, 255, 3]
print sum(a)

## Average
a = [1, 2, 5, 10, 255, 3]
b = sum(a) / len(a)
print b