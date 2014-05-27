"""
Small method for packin information for service Discovery
"""
import struct


class DiscObjectRequest(object):
    """
    Methods for Building a string sending over Network
    for request of service discovery
    """
    header = 0x43
    #format header(0x43), type(Service looking for), Port(for answer)
    formatString = "III"

    @staticmethod
    def encode(disc_type, port):
        """
        Make a data opjec for transfering over
        Networtk
        """
        return struct.pack(DiscObjectRequest.formatString,
                DiscObjectRequest.header, disc_type, port)

    @staticmethod
    def decode(packed_obj):
        """
        Get Data out of the object
        """
        temp = struct.unpack(DiscObjectRequest.formatString, packed_obj)
        if temp[0] != DiscObjectRequest.header:
            raise Exception("Wrong packed object")
        return (temp[1], temp[2])

    @staticmethod
    def get_size():
        """
        Return size of the Data Packet
        """
        return struct.calcsize(DiscObjectRequest.formatString)


if __name__ == '__main__':
    TEST = DiscObjectRequest.encode(0x10)
    print TEST
    print DiscObjectRequest.decode(TEST)
    print DiscObjectRequest.get_size()
