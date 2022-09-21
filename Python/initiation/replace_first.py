from typing import Iterable

def replace_first(items: list) -> Iterable:

    if items == []:
        return items

    else:
        items.append(items[0])
        items.pop(0) 
        return items