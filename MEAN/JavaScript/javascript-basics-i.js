// BASIC 1
var x = [];
console.log(x);
x.push('coding', 'dojo', 'rocks');
x.pop();
console.log(x);

// BASIC 2
const y = [];
console.log(y);
y.push(88);
console.log(y);

// BASIC 3
let z = [9, 10, 6, 5, -1, 20, 13, 2];
console.log(z);
z.pop();
console.log(z);

// BASIC 4
let names = ['Kadie', 'Joe', 'Fritz', 'Pierre', 'Alphonso'];
for (let i = 0; i < names.length; i++) {
    if (names[i].length >= 5) {
        console.log(names[i]);
    };
};

// BASIC 5
function yell (string) {
    console.log(string.toUpperCase());
    return string.toUpperCase();
};
yell('this is easy');