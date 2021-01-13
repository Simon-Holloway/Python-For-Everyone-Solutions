import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

j = 0
sumr = 0

while True:
    url = 'http://py4e-data.dr-chuck.net/comments_1121987.xml'
    uh = urllib.request.urlopen(url, context=ctx)

    data = uh.read()
    print('Retrieved', len(data), 'characters')
    tree = ET.fromstring(data)
    
    results2 = tree.findall('comments/comment')
    for i in results2:
        counttex = (results2[j].find('count').text)
        sumr += int(counttex)
        j += 1
        
    print(sumr)
    break