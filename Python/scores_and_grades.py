import random

def grade(score):
    if 90 < score < 100:
        print "Score: " + str(score) + "; Your grade is: A."
    elif 80 < score < 89:
        print "Score: " + str(score) + "; Your grade is: B."
    elif 70 < score < 79:
        print "Score: " + str(score) + "; Your grade is: C."
    elif 60 < score < 69:
        print "Score: " + str(score) + "; Your grade is: D."

print "Scores and Grades"

for x in range(0,10):
    score = random.randint(60,100)
    grade(score)

print "End of the program. Bye!"