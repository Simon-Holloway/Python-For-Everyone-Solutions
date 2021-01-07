fname = open('mbox-short.txt')
days = dict()
for line in fname:
    nline = line.rstrip()
    if not nline.startswith('From'): continue
    words = nline.split()
    if len(words) < 3: continue
    print(words)
    if words[2] not in days.keys():
        days[words[2]] = 1
    else:
        days[words[2]] += 1

print(days)