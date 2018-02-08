import random

def coin_toss():
    print "Starting the program..."

    num_heads = 0
    num_tails = 0

    for x in range(1,5001):
        side = round(random.random())

        if side == 0:
            side = "head"
            num_heads += 1
        elif side == 1:
            side = "tail"
            num_tails += 1

        print "Attempt# " + str(x) + ": Throwing a coin... It's a " + str(side) + "!... Got " + str(num_heads) + " head(s) so far and " + str(num_tails) + " tail(s) so far"

    print "Ending the program, thank you!"

coin_toss()