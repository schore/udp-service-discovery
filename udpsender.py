import socket
import time
import discrequestobj
import staticenumerations
import zmq
import servicelist

servlist = servicelist.ServiceList()
def discovery(ip, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    discrequ = discrequestobj.DiscObject(0x43, "III")
    serv = staticenumerations.SERVICE_TYPE.get_numb('servdisc')
    ctx = zmq.Context()
    zmq_sock = ctx.socket(zmq.REP)
    while True:
        aport = zmq_sock.bind_to_random_port("tcp://*")
        data_stream = discrequ.encode(serv, aport)
        sock.sendto(data_stream, (ip, port))
        print "Sending test" + str(aport)
        rxob = zmq_sock.recv_pyobj()
        zmq_sock.send("rx ok")
        print rxob
        print type(rxob)
        import ipdb; ipdb.set_trace() # BREAKPOINT
        time.sleep(1)

if __name__ == '__main__':
    discovery("127.0.0.1", 5555)
