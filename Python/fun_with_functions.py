## Odd/Even
def odd_even():
    for num in range(1, 2001):
        if (num % 2 == 0):
            print "Number is " + str(num) + ". This is an even number."
        elif (num % 2 == 1):
            print "Number is " + str(num) + ". This is an odd number."
odd_even()

## Multiply
def multiply(a):
    b = []
    for value in a:
        b.append(value * 5)
        print b

multiply([2,4,10,16])