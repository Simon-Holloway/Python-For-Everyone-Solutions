fname = open('mbox-short.txt')
emails = dict()
for line in fname:
    nline = line.rstrip()
    if not nline.startswith('From:'): continue
    words = nline.split()
    if len(words) < 2: continue
    emil = words[1]
    cut = emil.find('@')
    nexword = emil[cut+1:]
    if nexword not in emails.keys():
        emails[nexword] = 1
    else:
        emails[nexword] += 1

print(emails)