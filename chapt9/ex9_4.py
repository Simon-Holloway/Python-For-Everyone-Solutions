fname = open('romeo.txt')
alph = []
for line in fname:
    word = line.split()
    for i in range(len(word)):
        if word[i] in alph: continue
        alph.append(word[i])
    

alph.sort()
print(alph)