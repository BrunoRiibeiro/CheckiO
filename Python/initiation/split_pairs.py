def split_pairs(a):

    lst = []
    if len(a) % 2 != 0:
        a += "_"
        
    for i in range(0, len(a), 2):
        lst.append(a[i:i+2])
        
    return lst