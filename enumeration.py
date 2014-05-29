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

    def is_in_list(self, search):
        """look if the object is in the list"""
        if type(search) == int:
            return self.is_numb_in_enum(search)
        if type(search) == str:
            return self.is_str_in_enum(search)
        return False

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

    def get_numb(self, inp):
        """
        Get Number of the Element back return -1
        in case of an error
        """
        if not self.is_in_list(inp):
            return -1
        if type(inp) == int:
            return inp
        return self.string_to_numb(inp)

    def get_string(self, inp):
        """
        Get String of the Element back
        """
        if not self.is_in_list(inp):
            return "Error " + str(inp)
        if type(inp) == str:
            return inp
        return self.numb_to_string(inp)


if __name__ == '__main__':
    TEST_NUMERATION = Enumeration(("a", "b", "c"))
    print TEST_NUMERATION.numb_to_string(2)
    print TEST_NUMERATION.string_to_numb("c")
