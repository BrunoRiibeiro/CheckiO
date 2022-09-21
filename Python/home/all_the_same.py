from typing import List, Any

def all_the_same(elements: List[Any]) -> bool:

    if elements == []:
        return True

    acc = elements[0]
    value = None

    for i in elements:
        if i != acc:
            value = i
    
    if value == None:
        return True
    
    else:
        return False