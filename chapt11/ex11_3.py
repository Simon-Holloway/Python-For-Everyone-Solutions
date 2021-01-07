import string
fhand = open('mbox.txt')
count = dict()
for line in fhand:
    line1 = line.translate(str.maketrans('', '', string.punctuation))
    line2 = line1.translate(str.maketrans('', '', string.digits))
    line3 = line2.lower()
    words = line3.split() 
    for word in words:
        for let in word:
            count[let] = count.get(let,0) + 1
        


# Sort the dictionary by value
lst = list()
for key, val in list(count.items()):
    lst.append((val, key))

lst.sort(reverse=True)
for k,v in lst:
    print(k,v)

