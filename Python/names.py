students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
]

def print_list():
    for name in students:
        print name["first_name"], name["last_name"]

print_list()

users = {
'Students': [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'},
    {'first_name' : 'Mark', 'last_name' : 'Guillen'},
    {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ],
'Instructors': [
    {'first_name' : 'Michael', 'last_name' : 'Choi'},
    {'first_name' : 'Martin', 'last_name' : 'Puryear'}
    ]
}

def print_dict():
    print "\nStudents:"
    i = 0
    for key, data in users.items():
        for value in data:
            student = " "
            name = value["first_name"], value["last_name"]
            full_name = student.join(name)
            print i + 1, "-", full_name, "-", len(full_name)
            i += 1

print_dict()