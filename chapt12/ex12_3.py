import re
fname = open('act.txt')
tot = 0
for line in fname:
    line = line.rstrip()
    #matc = re.findall('[^A-Za-z\?.! \(\),-:+\'>].* ([0-9]*)',line)
    matc = re.findall('([0-9]+)',line)
    if len(matc) > 0:
        for i in matc:
            print(i)
            tot += int(i)

print(tot)
