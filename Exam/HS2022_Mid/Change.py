def change(pennies):
    res = [0,0,0,0,0]
    if pennies >= 100:
        add = pennies//100
        res[0] = add
        pennies %= 100
    if pennies >= 25:
        add = pennies//25
        res[1] = add
        pennies %=25
    if pennies >= 10:
        add = pennies//10
        res[2] = add
        pennies %=10
    if pennies >= 5:
        add = pennies//5
        res[3] = add
        pennies %= 5
    if pennies < 5:
        res[4] = pennies
    return tuple(res)

print(change(3))


#their solution
def change(pennies):
    dollars = pennies//100
    pennies %= 100
    quarters = pennies//25
    pennies %= 25
    dimes = pennies//10
    pennies %= 10
    nickel = pennies//5
    pennies %= 5
    return (dollars, quarters, dimes, nickel, pennies)
print(change(3))


