import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
html = urllib.request.urlopen('https://en.wikipedia.org/wiki/Peter_Badcoe', context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')

# Retrieve all of the p tags
count = 0
tags = soup('p')
for tag in tags:
    count += 1

print(count)