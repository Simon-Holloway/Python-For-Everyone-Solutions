import re
usrin = input('enter a regular expression:')
fname = open('mbox.txt')
count = 0
for line in fname:
    line = line.rstrip()
    matc = re.findall(usrin,line)
    if len(matc) > 0: count += 1

print('mbox.txt had', count, 'lines that matched', usrin)
    