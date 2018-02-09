## Part I
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
print " "

## Part II
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

students = users['Students']
instructors = users['Instructors']

def print_dict(data, role): 
	print role
	for i in range(len(data)): 
		name = data[i]['first_name'] + " " + data[i]['last_name']
		print i + 1, "-", name, "-", (len(data[i]['first_name'] + data[i]['last_name']))

print_dict(students, 'Students:')
print_dict(instructors, 'Instructors:')