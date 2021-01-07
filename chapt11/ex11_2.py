fname = open('mbox-short.txt')
days = dict()
for line in fname:
    nline = line.rstrip()
    if not nline.startswith('From'): continue
    words = nline.split()
    if len(words) < 6: continue
    newwrds = words[5]
    upto = newwrds.find(':')
    betwrds = newwrds[:upto]
    days[betwrds] = days.get(betwrds, 0) + 1

lst = list()
for k,v in days.items():
    lst.append((k,v))
lst.sort()
for k,v in lst:
    print(k,v)