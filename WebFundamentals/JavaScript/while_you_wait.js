var daysUntilMyBirthday = 60;

while (daysUntilMyBirthday >= 30) {
    console.log(daysUntilMyBirthday + " days until my birthday. It's so far from now... what a bummer!");
    daysUntilMyBirthday--;
}
while (daysUntilMyBirthday <= 30 && daysUntilMyBirthday >= 6) {
    console.log(daysUntilMyBirthday + " days until my birthday. It's getting closer!");
    daysUntilMyBirthday--;
}
while (daysUntilMyBirthday <= 5 && daysUntilMyBirthday > 0) {
    console.log(daysUntilMyBirthday + " days until my birthday. OH MY GOD!");
    daysUntilMyBirthday--;
}
while (daysUntilMyBirthday === 0) {
    console.log("It's MY friggin' BiRtHdAy! OH YEAH!!!");
    break;
}