import socket
import time
import discrequestobj
import staticenumerations
import zmq
import servicelist

def discovery(ip, port, ty):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    discrequ = discrequestobj.DiscObject(0x43, "III")
    serv = staticenumerations.SERVICE_TYPE.get_numb(ty)
    ctx = zmq.Context()
    zmq_sock = ctx.socket(zmq.REP)
    aport = zmq_sock.bind_to_random_port("tcp://*")
    data_stream = discrequ.encode(serv, aport)
    sock.sendto(data_stream, (ip, port))
    rxob = zmq_sock.recv_pyobj()
    zmq_sock.send("rx ok")
    return rxob

if __name__ == '__main__':
    rx = discovery("127.0.0.1", 5555, 'servdisc')
    for i in rx:
        i.print_list()
    rx = discovery("127.0.0.1", 5555, 'red')
    for i in rx:
        i.print_list()
