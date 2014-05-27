import disc_send_object
import socket


def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    while True:
        data, addr = sock.recvfrom(
                disc_send_object.DiscObjectRequest.get_size())
        disc_type = disc_send_object.DiscObjectRequest.decode(data)
        print "received " + data +" from " + addr[0]+ " " + str(addr[1])
        print "Type" + str(disc_type)


if __name__ == '__main__':
    server(5555)
