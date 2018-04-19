// MATH 1
let a = [-1, 0, 1, 2];

function zero_negativity() {
    for (let i = 0; i < a.length; i++) {
        if (a[i] < 0) {
            console.log('false');
            return false;
        } else {
            console.log('true');
            return true;
        }
    }
}

zero_negativity();

// MATH 2
let b = 4;

function is_even() {
    if (b % 2 == 0) {
        console.log('true');
        return true;
    } else {
        console.log('false');
        return false;
    }
}

is_even();

// MATH 3
// function how_many_even(c) {
//     let d = 0;
//     for (let i = 0; i < c.length; i++) {
//         if (is_even(c[i])) {
//             d += 1;
//         }
//     }
//     return d;
// }

// how_many_even([1,2,3,4,5,6,7]);

// MATH 4
function create_dummy_array(n) {
    for (let i = 0; i < n.length; i++) {
        n.push(Math.floor(Math.random() * 10));
    }
    console.log(n);
    return n;
}

create_dummy_array(1,2,3,4);