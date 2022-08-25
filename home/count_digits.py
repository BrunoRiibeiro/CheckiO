def count_digits(text: str) -> int:

    acc = 0
    for i in list(text):
        if i.isdigit() == True:
            acc += 1

    return acc