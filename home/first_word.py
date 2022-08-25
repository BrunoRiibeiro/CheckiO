def first_word(text: str) -> str:

    lst = text.replace(","," ").replace("."," ").split()
    
    return lst[0]