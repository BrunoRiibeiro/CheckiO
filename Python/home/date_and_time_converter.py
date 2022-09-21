def date_time(time: str) -> str:
    
    months = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December",
    }
    
    date = str(time.split()[0]).split('.')
    day = date[0]
    month = date[1]
    tempo = str(time.split()[1]).split(':')
    hour = tempo[0]

    if hour == "00":
        hour = '0'

    else:
        hour = tempo[0].lstrip('0')

    minutes = tempo[1]

    if minutes == "00":
        minutes = '0'

    else:
        minutes = tempo[1].lstrip('0')
        
        
    min_is_plural = ""
    if minutes == '1':
        min_is_plural = "minute"

    else:
        min_is_plural = "minutes"  
        
    hr_is_plural = ""
    if hour == '1':
        hr_is_plural = "hour"

    else:
        hr_is_plural = "hours"

    result = day.lstrip("0"), months[month], date[-1], "year", hour, hr_is_plural, minutes, min_is_plural
    return " ".join(result)