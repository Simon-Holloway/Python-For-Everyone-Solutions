try:
    scr = float(input("enter score between 0.0 and 1.0\n"))
except:
    print("bad score")
    
if scr > 1.0 or scr < 0.0:
    print("Outta range")
elif scr >= .9:
    print('Grade A!')
elif scr >= .8:
    print('Grade B!')
elif scr >= .7:
    print('Grade C!')
elif scr >= .6:
    print('Grade D!')
else:
    print('Grade F!')