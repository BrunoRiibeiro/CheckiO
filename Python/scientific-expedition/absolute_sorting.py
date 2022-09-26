def checkio(values: list) -> list:
    abs_list = []
    for i in values:
            abs_list.append(abs(i))

    abs_sorted = sorted(abs_list)
    for i in values:
        a = abs(i)
        if i != abs(i):
            abs_sorted[abs_sorted.index(a)] = i

    return abs_sorted