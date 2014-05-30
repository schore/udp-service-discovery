"""
Small method for packin information for service Discovery
"""
import struct


class DiscObject(object):
    """
    Methods for Building a string sending over Network
    for request of service discovery
    """
    def __init__(self, header, format_string):
        self.header = header
        self.format_string = format_string

    def encode(self, disc_type, port):
        """
        Make a data opjec for transfering over
        Networtk
        """
        return struct.pack(self.format_string,
                self.header, disc_type, port)

    def decode(self, packed_obj):
        """
        Get Data out of the object
        """
        temp = struct.unpack(self.format_string, packed_obj)
        if temp[0] != self.header:
            raise Exception("Wrong packed object")
        return (temp[1], temp[2])

    def get_size(self):
        """
        Return size of the Data Packet
        """
        return struct.calcsize(self.format_string)


if __name__ == '__main__':
    DISC = DiscObject(0x43, "III")
    TEST = DISC.encode(0x10, 12)
    print TEST
    print DISC.decode(TEST)
    print DISC.get_size()
