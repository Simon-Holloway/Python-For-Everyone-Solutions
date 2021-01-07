fname = open('mbox-short.txt')
emails = dict()
highest = None
name = None
for line in fname:
    nline = line.rstrip()
    if not nline.startswith('From'): continue
    words = nline.split()
    if len(words) < 3: continue
    if words[1] not in emails.keys():
        emails[words[1]] = emails.get(words[1],0) + 1
    else:
        emails[words[1]] += 1
    
for i in emails:
    if highest == None or emails[i] > highest:
        highest = emails[i]
        name = i


print(name, highest)
