"""
Some static configurations enum....
"""
from enumeration import Enumeration

#only a dummy list at the momen
SERVICE_TYPE = Enumeration(('red', 'green', 'blue', 'servdisc'))
#only a dummy list at the momen
SERVICE_CONNECTION_TYPE = Enumeration((
    'tcp',
    'udp',
    'zmq'))


