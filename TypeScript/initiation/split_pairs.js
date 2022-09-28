function splitPairs(text) {

    if (text.length % 2 != 0) {
        text += "_";
    }
    
    var lst = [];
    for (let i = 0; i <= text.length-2; i += 2) {
        lst.push(text[i] + text[i+1]);
    }

    return lst;
}