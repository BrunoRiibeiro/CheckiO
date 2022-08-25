def end_zeros(num: int) -> int:

    a = str(num)

    return len(a) - len(a.rstrip("0"))