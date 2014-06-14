import zmq
import discrequestobj
import servicelist
import staticenumerations

STATIC_ID = "Service_Discovery"
def generate_object_to_process(command, service_type, connection_type, address):
    return (STATIC_ID, command, service_type, connection_type, address)

def process_input(input):
    #check type of input an return if it does not match
    if type(input) != tuple:
        return
    if len(input) != 5:
        return
    if input[0] != STATIC_ID:
        return
    if not staticenumerations.SERVICE_CONNECTION_COMMAND.is_in_list(input[1]):
        return
    if not staticenumerations.SERVICE_TYPE.is_in_list(input[2]):
        return
    if not staticenumerations.SERVICE_CONNECTION_TYPE.is_in_list(input[3]):
        return

    #check passed execute command
    command = staticenumerations.SERVICE_TYPE.get_numb(input[1])
    def switch(command):
        if command == staticenumerations.SERVICE_CONNECTION_COMMAND.get_numb('add'):
            servicelist.ServiceList.add_service(
                    input[2],
                    input[3],
                    input[4])
            return
        if command == staticenumerations.SERVICE_CONNECTION_COMMAND.get_numb('del'):
            print 'Remove'
            return
        print "Default Reached"

    switch(command)
    print "test"

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
    testob = generate_object_to_process(
            staticenumerations.SERVICE_CONNECTION_COMMAND.get_numb('add'),
            staticenumerations.SERVICE_TYPE.get_numb('red'),
            staticenumerations.SERVICE_CONNECTION_TYPE.get_numb('tcp'),
            "my Object"
            )
    process_input(testob)
    servicelist.ServiceList.print_whole_list()
    print "Test"
