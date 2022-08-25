def beginning_zeros(number: str) -> int:

    return len(str(number)) - len(str(number).lstrip("0"))