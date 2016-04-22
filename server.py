import socket
import vlc
import sys

#prepare player
instance = vlc.Instance()
player = instance.media_player_new()

#start connection
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind(('', 3378))
print "Socket has been bound"
serversocket.listen(1)
while True:
    c, addr = serversocket.accept()     # Establish connection with client.
    print 'Got connection from', addr
    f = open('file_1.mp3','wb') #open in binary
    l = c.recv(1024)
    while (l):
        f.write(l)
        l = c.recv(1024)
    f.close() #close file
    c.close() #close connection socket

    print 'received the file'
    print 'start playing'
    media = instance.media_new('file_1.mp3')
    player.stop()
    player.set_media(media)
    player.play()

serversocket.close
