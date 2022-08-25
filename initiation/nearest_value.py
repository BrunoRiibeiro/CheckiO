def nearest_value(values: set, one: int) -> int:

    count = []

    for i in sorted(values):
        count.append(abs(one - i))
    
    return list(sorted(values))[count.index(min(count))]