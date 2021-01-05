acum = 0
tot = 0
highest = None
lowest = None
while True:
    intex = input('enter a number: ')
    if intex == 'done':
        break
    try:
        flotex = float(intex)
    except:
        print('please enter a valid number')
        continue
    tot = tot + flotex
    acum = acum + 1
    if highest is None or highest < flotex:
        highest = flotex
    if lowest is None or lowest > flotex:
        lowest = flotex
    
print('done!', tot, acum, highest, lowest)

