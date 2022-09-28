function nearestValue(values, search) {

    var count = [];
    var sortValues = values.sort(function(a, b) {return a - b;});

    sortValues.forEach(element => {
        count.push(Math.abs(search - element));
    });
    
    return sortValues[count.indexOf(Math.min(...count))]
}