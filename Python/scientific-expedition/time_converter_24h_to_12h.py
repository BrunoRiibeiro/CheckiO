def time_converter(time):
    dic = { 
        "13":"1",
        "14":"2",
        "15":"3",
        "16":"4",
        "17":"5",
        "18":"6",
        "19":"7",
        "20":"8",
        "21":"9",
        "22":"10",
        "23":"11",
        "00":"12",
}
    
    lst = time.split(":")
    hour = []
    if int(lst[0]) > 12 or int(lst[0]) == 0:
        hour.append(dic[lst[0]])
        hour.append(":")
        hour.append(lst[1])
    else:
        hour.append(lst[0].lstrip("0"))
        hour.append(":")
        hour.append(lst[1])
        
    if 11 < int(lst[0]):
        hour.append(" p.m.")
    else:
        hour.append(" a.m.")
        
    return "".join(hour)