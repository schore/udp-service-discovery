"""Server for Service Discovery"""
import thread
import zmq
import socket
import discrequestobj
import servicelist
import time
from helper import addr_to_string

def service_sender(ip, port, service_type=None):
    print "start"
    if service_type == None:
        return
    regserv = servicelist.ServiceList.find_service(service_type)
    ctx = zmq.Context.instance()
    s = ctx.socket(zmq.REQ)
    s.connect(addr_to_string(ip, port))
    s.send_pyobj(regserv)
    print "___________________"
    print ip
    print port
    print service_type
    print "-------------------"

def servicedisc(port=5555):
    """Main servicedisc function"""
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('', port))
    discrequest = discrequestobj.DiscObject(0x43, "III")
    while True:
        data, addr = sock.recvfrom(
                discrequest.get_size())
        disc_type = discrequest.decode(data)
        thread.start_new_thread(service_sender,
                (addr[0], disc_type[1], disc_type[0]))

def service_disc_server(port):
    print "start discovery server"
    ctx = zmq.Context.instance()
    sock = ctx.socket(zmq.REP)
    sock.bind("tcp://*:"+str(port))
    addr = str(port)
    servicelist.ServiceList.add_service('servdisc', 'tcp', ('ip', port))
    while True:
        print "server running"
        time.sleep(10)


if __name__ == "__main__":
    servicelist.ServiceList.add_service('red', 'tcp', 0)
    servicelist.ServiceList.add_service('red', 'tcp', 1)
    servicelist.ServiceList.add_service('red', 'tcp', 2)
    servicelist.ServiceList.add_service('red', 'tcp', 3)
    thread.start_new_thread(service_disc_server, (10000,))
    servicedisc()
#    thread.start_new_thread(my_thread, ("Test different thread",))
#    thread.start_new_thread(my_thread, ("Third thread",))
#    print "test"
#    time.sleep(20)
