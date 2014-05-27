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
    #forma header(0x43) looking for
    formatString = "II"

    @staticmethod
    def encode(disc_type):
        """
        Make a data opjec for transfering over
        Networtk
        """
        return struct.pack(DiscObjectRequest.formatString,
                DiscObjectRequest.header, disc_type)

    @staticmethod
    def decode(packed_obj):
        """
        Get Data out of the object
        """
        temp = struct.unpack(DiscObjectRequest.formatString, packed_obj)
        if temp[0] != DiscObjectRequest.header:
            raise Exception("Wrong packed object")
        return temp[1]

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
