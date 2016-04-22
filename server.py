import socket
import vlc
p = vlc.MediaPlayer('D:\Musik\Trap\TNGHT - Goooo.mp3')
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 3378))
print "Socket has been bound"
serversocket.listen(1)
while True:
    c, addr = serversocket.accept()     # Establish connection with client.
    print 'Got connection from', addr
    c.close()
    print 'start playing'
    p.stop() #stop the old playing
    p.play()
