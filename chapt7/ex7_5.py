str = 'X-DSPAM-Confidence: 0.8475'
other = str.find(':')
newstr = str[18+1:]
x = newstr.strip()
y = float(x)
print(y)