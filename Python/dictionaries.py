person = {"name": "Anna", "age": "101", "country of birth": "United States", "favourite language": "Python"}

def print_dict():
    for key, value in person.iteritems():
        print "My", key, "is", value

print_dict()