arr = []
while True:
    usrin = input('enter a number: ')
    if usrin == 'done':
        break
    try:
        usrflo = float(usrin)
    except:
        print('enter a valid number')
        continue
    arr.append(usrflo)
    
print('Minimum:', min(arr))
print('Maximum:', max(arr))