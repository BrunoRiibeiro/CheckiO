function replaceFirst(values) {
    if(values === []) {
        return values;
    } else {
        values.push(values[0]);
        return values.slice(1);
    }
}

console.log(replaceFirst([1,2,3,4]))