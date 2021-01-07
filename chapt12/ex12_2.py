import re
fname = open('mbox.txt')
count = 0
tot = 0
for line in fname:
    line = line.rstrip()
    matc = re.findall('^New .*: ([0-9]+)',line)
    if len(matc) > 0: 
        count += 1
        tot += int(matc[0])

print(tot / count)


#print('mbox.txt had', count, 'lines that matched', usrin)