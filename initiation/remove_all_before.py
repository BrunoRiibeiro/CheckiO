from typing import Iterable

def remove_all_before(items: list, border: int) -> Iterable:

    if border not in items:
        return items
        
    else:
        list = items.index(border)
        return items[list:]