def checkio(array: list[int]) -> int:

    if len(array) == 0:
        return 0
        
    return sum(array[0::2]) * array[-1]