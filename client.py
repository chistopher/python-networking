import socket
s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.2.107', 3378))
