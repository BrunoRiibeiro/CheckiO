function beginningZeros(text) {

    return text.length - text.replace(/^0+/, '').length;
}