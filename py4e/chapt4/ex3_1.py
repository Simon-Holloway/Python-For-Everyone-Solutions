hr = float(input('hours worked\n'))
rt = float(input('work rate\n'))
py = hr * rt
if hr > 40:
    extra = (hr - 40.0) * ( rt * .5)
    tot = py + extra
    print('Pay: \n', tot)
else:
    print('pay:', py)