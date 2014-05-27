import socket
import time
import disc_send_object

def discovery(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    i = 0
    while True:
        data_stream = disc_send_object.DiscObjectRequest.encode(i)
        i = i + 1
        sock.sendto(data_stream, (ip, port))
        print "Sending test" + str(i)
        time.sleep(1)

if __name__ == '__main__':
    discovery("127.0.0.1", 5555)
