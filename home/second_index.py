def second_index(text: str, symbol: str) -> int:

    if text.find(symbol, text.find(symbol) + 1) == -1:
        return None
    
    else:
        return text.find(symbol, text.find(symbol) + 1)