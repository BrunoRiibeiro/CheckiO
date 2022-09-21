def split_list(items: list) -> list:

    first = len(items) // 2
    
    if len(items) % 2 != 0:
        list = [items[:first+1], items[first+1:]]
        
    else:
        list = [items[:first], items[first:]]
        
    return list