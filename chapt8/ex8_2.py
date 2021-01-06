fname = input('enter your file name\n')
if fname == 'na na boo boo':
    print('\nBRUH')
    quit()
try:
    kahn = open(fname)
except:
    print('enter a real name or a txt file')
    quit()

count = 0
tot = 0.0
for lyn in kahn:
    nlyn = lyn.rstrip()
    if not nlyn.startswith('X-DSPAM-Confidence:'): continue
    count = count + 1
    cut = nlyn.find(':')
    new = nlyn[cut+1:]
    tot = tot + float(new)
print('Average spam confidence:', (tot/count))