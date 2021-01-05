acum = 0
tot = 0
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
    
print('done!', tot, acum, tot/acum)
