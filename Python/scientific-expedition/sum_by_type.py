from typing import Tuple

def sum_by_types(items: list) -> Tuple[str, int]:
    inte = 0
    strg = ""
    for i in items:
        try:
            inte += i
        except:
            strg += i
    
    return (strg, inte)

print(sum_by_types(["1", 2, 3]))