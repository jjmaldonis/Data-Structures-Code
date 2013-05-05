""" Hashtable class """

class Hashtable:
    """ Re-implements python's hash table functionality. """
    PERTURB_SHIFT = 5


    def __init__(self):
        """ Initialization function for my hash table. """
        self.pos = 0
        # The size below is the power of 2 of the hashtable, not the actual size of the table.
        self.size = 2
        self.htable = [None] * (2**self.size)
        self.entries = 0.0
        # Set the load factor to 0 initially.
        self.lf = 0.0
        return None


    def get_size(self):
        """ Returns the size of the table. """
        return 2**self.size


    def get_load(self):
        """ Returns the current load of the table. """
        return self.lf


    def print_table(self):
        """ Prints the hash table for the user (mainly for debugging). """
        for i in range(0, 2**self.size):
            if(self.htable[i]):
                print( '  {0}: '.format(i) + self.htable[i] )


    def c_mul(self, a, b):
        """ This is how python creates some crazy but unique numbers based on other numbers. """
        return eval(hex((long(a) * b) & 0xFFFFFFFFL)[:-1])


    def pos_str_elem(self, element):
        """ This is how python evaluates a string into an int value for hash usage. """
        value = ord(element[0]) << 7
        for char in element:
            value = self.c_mul(1000003, value) ^ ord(char)
        value = value ^ len(element)
        if value == -1:
            value = -2
        return value


    def rehash(self):
        """ Rehashing function. """
        self.entries = 0.0
        self.pos = 0
        self.size = self.size + 1
        # Point a temp pointer at the current hashtable.
        temphtable = self.htable
        # Replace old table with the new bigger one.
        self.htable = [None] * (2**self.size)
        for i in range(0, 2**(self.size-1)):
            if(temphtable[i] != None):
                self.insert(temphtable[i])
            
        self.lf = (self.entries) / (2**self.size)
        return None


    # The following two functions are an implementation of python's hashing function (see increment_pos() for collisions).
    def reset_pos(self, element):
        """ Set position to the beginning of where it should be for a given input element. """
        self.pos = self.pos_str_elem(element) & (2**self.size-1)

    def increment_pos(self, perturb):
        """ A collision occured to get the next position pos should be set to. """
        # Side note: '& (2**self.size-1)' is the same as '^ (2**self.size)' but its much faster.
        self.pos = ((5*self.pos) + 1 + perturb) & (2**self.size-1)
        perturb = perturb >> self.PERTURB_SHIFT
        return perturb

    def insert(self, element):
        """ Insert an element.
        Raises an exception if that element already exists.
        """
        if self.find(element) is not -1:
            raise Exception("{0} is already in the table.".format(element))
        self.reset_pos(element)
        perturb = self.pos_str_elem(element)
        #Navigate until we get to an open spot
        while(self.htable[self.pos] != None):
            perturb = self.increment_pos(perturb)
        self.htable[self.pos] = element
        self.entries = self.entries + 1
        self.lf = ( self.entries ) / (2**self.size)
        if(self.lf >= 2.0/3.0):
            self.rehash()
        return None

    def find(self, element):
        """ Finds an element in the hashtable.
        Returns the position if it is found, otherwise returns -1.
        """
        self.reset_pos(element)
        perturb = self.pos_str_elem(element)
        while(self.htable[self.pos] != None):
            if element == self.htable[self.pos]:
                # Found it! Return where it's at.
                return self.pos
            else:
                # Didn't find it, check the next spot we would have put it in.
                perturb = self.increment_pos(perturb)
        return -1


def main():
    """ Testing code. """

    print("Initializing hashtable...")
    h = Hashtable()

    print("Inserting 'a' twice and checking for an error...")
    h.insert('a')
    try:
        h.insert('a')
    except:
        print("'a' is already in the table and an exception was raised appropriately.")
    print("Printing table...")
    h.print_table()
    assert h.find('a') == 0

    print("Inserting 'b' into the table...")
    h.insert('b')
    assert h.get_size() == 4

    print("Printing table...")
    h.print_table()

    print("Inserting 'c' into the table... The hashtable should grow to size 8 from size 4...")
    h.insert('c')

    print("Checking the size...")
    assert h.get_size() == 8

    print("Inserting 'd' into the table...")
    h.insert('d')
    
    print("Checking the load...")
    assert h.get_load() == 0.5

    
    print("Searching for 'e', then adding it to the table, then searching for it again. It should be at position 4...")
    assert h.find('e') == -1
    h.insert('e')
    assert h.find('e') != -1
    assert h.find('e') == 4

    print("Printing table...")
    h.print_table()

    moreToAdd = ['jason', 'kyle', 'dictionary', 'potato', 'orange']
    
    print("Inserting 5 more elements... The hashtable should immediately grow to size 16... Also, 'e' will have changed positions due to the rehash.")
    for word in moreToAdd:
        h.insert(word)

    print("Printing table...")
    h.print_table()
    print("Checking the size and information about some words...")
    assert h.get_size() == 16
    assert h.find('jason') != -1
    assert h.find('e') != -1
    assert h.find('e') != 4
    
    print("All testing was sucessful.")

    return None


if __name__ == "__main__":
    main()
