fname = open('mbox-short.txt')
emails = dict()

for line in fname:
    nline = line.rstrip()
    if not nline.startswith('From'): continue
    words = nline.split()
    if len(words) < 3: continue
    if words[1] not in emails.keys():
        emails[words[1]] = emails.get(words[1],0) + 1
    else:
        emails[words[1]] += 1
    
lst = list()
for k,v in list(emails.items()):
    lst.append((v,k))
lst.sort(reverse = True)
print(lst[1])

#print(sorted([(v,k) for k,v in emails.items()], reverse = True))

