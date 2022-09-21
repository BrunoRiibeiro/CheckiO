function removeAllBefore(values, b) {
    if (!(values.includes(b))) {
        return values;
    } else {
        return values.slice(values.indexOf(b));
    }
}