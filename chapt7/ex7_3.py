def lettercount(string, letter):
    count = 0
    for lets in string:
        if lets == letter:
            count = count + 1
    print(count)
    
lettercount('blahblahblahb','b')