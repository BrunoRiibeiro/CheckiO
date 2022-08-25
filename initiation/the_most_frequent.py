def most_frequent(data: list) -> str:
    
    mostF = ""
    acc = 0
    for i in data:
        if data.count(i) > acc:
            acc = data.count(i)
            mostF = i

    return mostF
