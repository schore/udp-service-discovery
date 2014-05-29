"""
Enumeration of objects
"""

class Enumeration(object):
    """Small enumeration"""
    def __init__(self, sequence):
        """sequence of objects to enumerate"""
        self.length = len(sequence)
        self.numerated = list(enumerate(sequence))

    def print_sequence(self):
        """Debug Function not really usefull"""
        for i in self.numerated:
            print i

    def is_str_in_enum(self, input_string):
        """Check if string is in this enum"""
        for i in self.numerated:
            if i[1] == input_string:
                return True
        return False

    def is_numb_in_enum(self, index):
        """Check if number is in enum"""
        if self.length < index:
            return False
        return True

    def numb_to_string(self, index):
        """convert numb to string"""
        if not self.is_numb_in_enum(index):
            raise Exception()
        return self.numerated[index][1]

    def string_to_numb(self, inputstring):
        """convert string to numb"""
        for i in self.numerated:
            if i[1] == inputstring:
                return i[0]

if __name__ == '__main__':
    TEST_NUMERATION = Enumeration(("a", "b", "c"))
    print TEST_NUMERATION.numb_to_string(2)
    print TEST_NUMERATION.string_to_numb("c")
