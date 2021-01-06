fhand = open('mbox-short.txt')
count = 0
for line in fhand:
    bline = line.rstrip()
    if not bline.startswith('From:'): continue
    words = bline.split()
    if len(words) < 2: continue
    count = count + 1
    print(words[1])
    
print(count)