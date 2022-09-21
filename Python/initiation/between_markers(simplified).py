def between_markers(text: str, begin: str, end: str) -> str:

    a = text.index(begin) + len(begin)
    b = text.index(end) + len(end)
    
    return text[a:b-1]