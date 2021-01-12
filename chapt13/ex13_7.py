import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

url =  'http://py4e-data.dr-chuck.net/known_by_Talha.html'
count = int(input('Enter count \n'))
enpos = int(input('Enter position \n'))
i = 0


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


while i < count:
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    pos = 0
    for tag in tags:
        ntag = tag.get('href', None)
        pos += 1
        if pos == enpos:
            url=ntag
            print(ntag)
            break
    i += 1