"""
Implementation of a List
for Discovery/Registration of Services
"""
from enumeration import Enumeration
#only a dummy list at the momen
SERVICE_TYPE = Enumeration(('red', 'green', 'blue'))
#only a dummy list at the momen
SERVICE_CONNECTION_TYPE = Enumeration((
    'tcp',
    'udp',
    'zmq'))

class ServiceList(list):
    """
    The List itself holds Head of the List as
    a static variable
    """
    Head = list()
    def __init__(self):
        list.__init__(self)
        self.service_type = "Some stupid Type"
        self.connection_type = "Not defined"
        self.addr = 0
        ServiceList.Head.append(self)

    def print_list(self):
        """
        Print the list item
        """
        print SERVICE_TYPE.get_string(self.service_type)
        print SERVICE_CONNECTION_TYPE.get_string(self.connection_type)
        print self.addr

    @staticmethod
    def print_whole_list():
        """Print the whole list"""
        for i in ServiceList.Head:
            i.print_list()

    @staticmethod
    def find_service(serv_to_disc):
        """Returns a list of service you are looking for"""
        #checkin the input type
        if type(serv_to_disc) != int:
            if type(serv_to_disc) != str:
                raise Exception()
            serv = SERVICE_TYPE.string_to_numb(serv_to_disc)
        else:
            serv = serv_to_disc
        #iterating throug list
        ret = list()
        for i in ServiceList.Head:
            if i.service_type == serv:
                ret.append(i)
        return ret

    @staticmethod
    def add_service(service_type, connection_type, address):
        """add Service to the list"""
        if not SERVICE_TYPE.is_in_list(service_type):
            return False
        if not SERVICE_CONNECTION_TYPE.is_in_list(connection_type):
            return False
        temp = ServiceList()
        temp.service_type = SERVICE_TYPE.get_numb(service_type)
        temp.connection_type = SERVICE_CONNECTION_TYPE.get_numb(connection_type)
        temp.addr = address
        return True

    @staticmethod
    def remove_service(service_type, connection_type, address):
        """Remove Item From List"""
        ret = False
        service_type = SERVICE_TYPE.get_numb(service_type)
        connection_type = SERVICE_CONNECTION_TYPE.get_numb(connection_type)
        for i in ServiceList.Head:
            if (i.service_type == service_type and
                    i.connection_type == connection_type and
                    i.addr == address):
                ServiceList.Head.remove(i)
                ret = True
        return ret



if __name__ == "__main__":
    ServiceList.add_service("red", "tcp", 0)
    ServiceList.add_service("green", "udp", 1)
    ServiceList.add_service("blue", "zmq", 22)
    ServiceList.add_service("blue", "tcp", 22)
    ServiceList.print_whole_list()
    ServiceList.remove_service("red", "tcp", 0)
    print "Testing Remove"
    print "------------------"
    ServiceList.print_whole_list()
    print "Testing Find"
    print "------------------"
    SERV = ServiceList.find_service("blue")
    for j in range(0, 2, 1):
        print j
        SERV[j].print_list()
