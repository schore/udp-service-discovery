"""Small helper nothing special"""

def addr_to_string(ip, port, con_type = 'tcp'):
    """convert to a string int type Protocols://ip:port"""
    return con_type + '://' + ip + ':' + str(port)


