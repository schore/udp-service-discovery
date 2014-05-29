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
        print self.service_type
        print self.connection_type
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
            if type(serv_to_disc != str):
                raise Exception()
            serv = SERVICE_TYPE.string_to_numb(serv_to_disc)
        else:
            serv = serv_to_disc
        #iterating throug list
        ret = list()
        for i in ServiceList.Head:
            if i.connection_type == serv:
                ret.append(i)
        return ret



if __name__ == "__main__":
    TA = ServiceList()
    TA.print_list()
    TA.service_type = "No Idea"
    TA.addr = 1
    TB = ServiceList()
    TB.service_type = "Fuck"
    TB.connection_type = "Not Supported"
    TB.addr = 2
    TC = ServiceList()
    TC.connection_type = "fuck"
    TC.addr = 3
    print len(ServiceList.Head)

    ServiceList.find_service(1)
    print "Printing whole list"
    ServiceList.print_whole_list()
