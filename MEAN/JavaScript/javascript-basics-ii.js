// MATHS FUNCTION
function magic_multiply(x, y) {
    if (Array.isArray(x)) {
        for (let i = 0; i < x.length; i++) {
            x[i] = x[i] * y;
        }
    } else if (typeof x === 'string' || typeof y === 'string') {
        console.log('Error: Can not multiply by string');
    } else {
        x = x * y;
    }
    return x;
}

// MATHS TESTS
let test1 = magic_multiply(5, 2);
console.log(test1);

let test2 = magic_multiply(0, 0);
console.log(test2);

let test3 = magic_multiply([1, 2, 3], 2);
console.log(test3);

let test4 = magic_multiply(7, "three");
console.log(test4);
