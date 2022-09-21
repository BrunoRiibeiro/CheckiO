def between_markers(text: str, begin: str, end: str) -> str:

    try:
        start = text.index(begin) + len(begin)
    
    except ValueError:
        start = 0
        
    try:
        stop = text.index(end)
    
    except ValueError:
        stop = None
    
    return text[start:stop]