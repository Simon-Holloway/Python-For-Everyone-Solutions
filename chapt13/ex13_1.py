import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
usrin = input('input a website URL \n')
host = usrin.split()
try:
    mysock.connect((host[0], 80))
except:
    print('that did not work')
    quit()

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()