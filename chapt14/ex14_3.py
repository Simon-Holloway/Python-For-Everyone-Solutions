import urllib.request, urllib.parse, urllib.error
import json

sumr = 0
url = 'http://py4e-data.dr-chuck.net/comments_1121988.json'
uh = urllib.request.urlopen(url)
data = uh.read()
js = json.loads(data)
com = js['comments']
for i in com:
    for k,v in i.items():
        if type(v) == str: continue
        sumr += int(v)
  
print(sumr)