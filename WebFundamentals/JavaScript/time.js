var HOUR = 7;
var MINUTE = 15;
var PERIOD = "PM";

if (MINUTE < 30) {
    var timing = "just after";
    var newHour = HOUR;
}
else if (MINUTE >= 30) {
    var timing = "almost";
    var newHour = HOUR + 1;
}
else {
    var timing = "";
}

if (PERIOD == "AM") {
    var newPeriod = "in the morning";
}
else if (PERIOD == "PM") {
    var newPeriod = "in the evening";
}
else {
    var newPeriod = "";
}

console.log("It's " + timing + " " + newHour + " " + newPeriod + "!");