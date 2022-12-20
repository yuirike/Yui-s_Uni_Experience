import math
def work(hours, days, teen=False):
    per_day = round((hours/days),2)
    if teen == True: 
        max_days = 25
    else: 
        max_days = 20   
    percentage = hours/42
    vacation_day = math.ceil(percentage*max_days)
    return {"per_day":per_day, "vacation_days":vacation_day}
    

assert work(42, 5) == {"per_day": 8.4, "vacation_days": 20}
assert work(42, 5, True) == {"per_day": 8.4, "vacation_days": 25}
assert work(34, 5) == {"per_day": 6.8, "vacation_days": 17}
assert work(16.55, 4, True) == {"per_day": 4.14, "vacation_days": 10}

