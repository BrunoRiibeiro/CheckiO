function betweenMarkers(line, left, right) {
    
    var start = line.indexOf(left) + left.length;
    var stop = line.indexOf(right) + right.length;

    return line.slice(start, stop - 1);
}