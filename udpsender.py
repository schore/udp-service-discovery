import socket
import time
import discrequestobj

def discovery(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    discrequ = discrequestobj.DiscObject(0x43, "III")
    i = 0
    while True:
        data_stream = discrequ.encode(i, 3231)
        i = i + 1
        sock.sendto(data_stream, (ip, port))
        print "Sending test" + str(i)
        time.sleep(1)

if __name__ == '__main__':
    discovery("127.0.0.1", 5555)
