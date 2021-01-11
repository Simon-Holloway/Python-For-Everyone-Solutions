from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl


ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


html = urlopen('http://py4e-data.dr-chuck.net/comments_1121985.html', context=ctx)
soup = BeautifulSoup(html, "html.parser")


count = 0
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
    print('Contents:', tag.contents[0])
    bruh = int(tag.contents[0])
    count += bruh
    
print(count)
