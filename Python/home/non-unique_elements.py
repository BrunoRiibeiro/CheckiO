def checkio(data: list) -> list:

    lst = []
    for i in data:
        if data.count(i) > 1:
            lst.append(i)

    return lst