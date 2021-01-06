fname = open('words.txt')

newkey = dict()
for lines in fname:
    words = lines.split()
    for wo in words:
        newkey[wo] = 1
print('of' in newkey)
print(newkey)