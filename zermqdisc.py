"""Server for Service Discovery"""
import thread
import zmq
import socket
import discrequestobj
import servicelist
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
    print "leave"
 
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


if __name__ == "__main__":
    servicedisc()
#    thread.start_new_thread(my_thread, ("Test different thread",))
#    thread.start_new_thread(my_thread, ("Third thread",))
#    print "test"
#    time.sleep(20)
