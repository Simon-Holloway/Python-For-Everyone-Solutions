import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    mysock.connect(('data.pr4e.org', 80))
except:
    print('that did not work')
    quit()

cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()