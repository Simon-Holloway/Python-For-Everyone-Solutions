try:
    hr = float(input('hours worked\n'))
    rt = float(input('work rate\n'))
except:
    print('Error: not a number')
    quit()

py = hr * rt
if hr > 40:
    extra = (hr - 40.0) * ( rt * 1.5)
    tot = py + extra
    print('Pay: \n', tot)
else:
    print('pay:', py)