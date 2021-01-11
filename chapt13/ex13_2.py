import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#usrin = input('input a website URL \n')
#host = usrin.split('/')
try:
    mysock.connect(('bruh.com', 80))
except:
    print('that did not work')
    quit()

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

count = 0
word = dict()
while True:
    data = mysock.recv(512)
    data.rstrip()
    if len(data) < 1:
        break
    for w in data.decode():
        if count >= 3000:
            break
        count += 1
        word[w] = word.get(w,0) + 1

mysock.close()

print("amount of characters:", count)