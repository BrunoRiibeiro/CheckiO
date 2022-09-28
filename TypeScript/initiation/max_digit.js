function maxDigit(value) {

    return Math.max(...String(value).split("").map(n => Number(n)));
}

console.log(maxDigit(1000))