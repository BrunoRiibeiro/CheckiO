def correct_sentence(text: str) -> str:

    text = text[0].upper() + text[1:]
    
    if text[-1] != '.':
        text += '.'
        
    return text