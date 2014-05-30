import discrequestobj
import socket


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    discrequest = discrequestobj.DiscObject(0x43, "III")
    while True:
        data, addr = sock.recvfrom(
                discrequest.get_size())
        disc_type = discrequest.decode(data)
        print "received " + data +" from " + addr[0]+ " " + str(addr[1])
        print "Type" + str(disc_type)


if __name__ == '__main__':
    server(5555)
