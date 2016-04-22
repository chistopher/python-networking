import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 3378))
print "Socket has been bound"
serversocket.listen(1)
(clientsocket, address) = serversocket.accept()
print "Connection has been accepted"
    #ct = client_thread(clientsocket)
    #ct.run()
