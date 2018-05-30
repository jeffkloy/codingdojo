let students = [
    {name: 'Remy', cohort: 'Jan'},
    {name: 'Genevieve', cohort: 'March'},
    {name: 'Chuck', cohort: 'Jan'},
    {name: 'Osmund', cohort: 'June'},
    {name: 'Nikki', cohort: 'June'},
    {name: 'Boris', cohort: 'June'}
];

for (const student of students) {
    console.log(`Name: ${student.name}, Cohort: ${student.cohort}`);
};

let users = {
    employees: [
        {'first_name':  'Miguel', 'last_name' : 'Jones'},
        {'first_name' : 'Ernie', 'last_name' : 'Bertson'},
        {'first_name' : 'Nora', 'last_name' : 'Lu'},
        {'first_name' : 'Sally', 'last_name' : 'Barkyoumb'}
    ],
    managers: [
        {'first_name' : 'Lillian', 'last_name' : 'Chambers'},
        {'first_name' : 'Gordon', 'last_name' : 'Poe'}
    ]
};

for (const people in users) {
    console.log(people.toUpperCase() + ":");
    for (let i = 0; i < users[people].length; i++) {
        const number = i + 1;
        const fname = users[people][i].first_name;
        const lname = users[people][i].last_name;
        const length = fname.length + lname.length;
        console.log(`${number} - ${lname}, ${fname} - ${length}`);
    }
};
