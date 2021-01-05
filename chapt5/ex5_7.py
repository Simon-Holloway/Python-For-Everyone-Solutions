def computegrade(score):
    if scr > 1.0 or scr < 0.0:
        return("Outta range")
    elif scr >= .9:
        return('Grade A!')
    elif scr >= .8:
        return('Grade B!')
    elif scr >= .7:
        return('Grade C!')
    elif scr >= .6:
        return('Grade D!')
    else:
        return('Grade F!')


try:
    scr = float(input("enter score between 0.0 and 1.0\n"))
except:
    print("\nPut in a score")
    quit()
    
print(computegrade(scr))
