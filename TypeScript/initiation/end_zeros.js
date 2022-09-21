function endZeros(value) {
    
    return String(value).length - String(value).replace(/0+$/, '').length;
}