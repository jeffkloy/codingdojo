var newArray = numbersOnly([1, "apple", -3, "orange", 0.5]);

function numbersOnly(newArray) {
    var numArray = [];

    for (var i = 0; i < newArray.length; i++) {
        if (typeof (newArray[i]) === 'number') {
            numArray.push(newArray[i]);
        }
    }
    console.log(numArray);
    
    return numArray;
}