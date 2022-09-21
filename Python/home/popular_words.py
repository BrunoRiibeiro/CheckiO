def popular_words(text: str, words: list) -> dict:

    lst = []
    
    for i in words:
        lst.append(text.lower().split().count(i))

    dic1 = {
            
        words[0]: lst[0],
        words[1]: lst[1],
        words[2]: lst[2],
}
    if len(lst) == 3:
        return dic1


    dic2 = {
        
        words[0]: lst[0],
        words[1]: lst[1],
        words[2]: lst[2],
        words[3]: lst[3],
}
    if len(lst) == 4:
        return dic2


    dic3 = {
        words[0]: lst[0],
        words[1]: lst[1],
        words[2]: lst[2],
        words[3]: lst[3],
        words[4]: lst[4],
}   
    if len(lst) == 5:
        return dic3