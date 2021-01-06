fname = input('enter your file name\n')
try:
    kahn = open(fname)
except:
    print('enter a real name or a txt file')
    quit()
    
for lyn in kahn:
    nlyn = lyn.rstrip()
    print(nlyn.upper())