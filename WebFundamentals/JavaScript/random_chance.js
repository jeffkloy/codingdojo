// This assignment could be entirely incorrect as I didn't really understand the prompt.

function randomChance (quarters) {
    if (quarters > 1) {
        var q = Math.random(quarters) * 100;
        q = Math.floor(q);
        var total = quarters + q;
        console.log("You started with " + quarters + " and won " + q + ", with a total of " + total + ".");
    } else {
        console.log("You have no money.");
    }
}