def goes_after(word: str, first: str, second: str) -> bool:
    try:
        return 1 + word.index(first) == word.index(second)
    except:
        return False