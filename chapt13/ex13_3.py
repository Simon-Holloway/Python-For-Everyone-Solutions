import urllib.request, urllib.parse, urllib.error
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

html = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
count = 0
freq = dict()
for line in html:
    words = line.decode().lower().split()
    for w in words:
        for i in w:
            print(i)
            count += 1
            if count >= 3000: break
            freq[i] = freq.get(i, 0) + 1

print(freq, count)