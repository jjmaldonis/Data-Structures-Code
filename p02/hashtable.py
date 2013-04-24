""" Hashtable class """

class Hashtable:
    """ re-implements python's hash table functionality """
    PERTURB_SHIFT = 5

    def __init__(self):
        """ init function for my hash table. """
        self.pos = 0
        #The size below is the power of 2 of the hashtable, not the actual size of the table
        self.size = 3
        self.htable = [None] * (2**self.size)
        self.entries = 0.0
        #Let the load factor to 0 initially
        self.lf = 0.0
        return None

    def print_table(self):
        """ Prints the hash table for the user (mainly for debugging) """
        for i in range(0, 2**self.size):
            print( '  ' + self.htable[i] )

    def c_mul(self, a, b):
        """ This is how python creates some crazy but unique numbers based on other numbers """
        return eval(hex((long(a) * b) & 0xFFFFFFFFL)[:-1])
    def pos_str_elem(self, element):
        """ This is how python evaluates a string into an int value for hash usage """
        value = ord(element[0]) << 7
        for char in element:
            value = self.c_mul(1000003, value) ^ ord(char)
        value = value ^ len(element)
        if value == -1:
            value = -2
        return value

    def rehash(self):
        """ Rehashing function """
        print("Rehash table to size {}!".format(2**(self.size+1)))
        self.entries = 0.0
        self.pos = 0
        self.size = self.size + 1
        #Point a temp pointer at the current hashtable
        temphtable = self.htable
        #Replace old table with the new bigger one
        self.htable = [None] * (2**self.size)
        for i in range(0, 2**(self.size-1)):
            if(temphtable[i] != None):
                self.insert(temphtable[i])
            
        self.lf = (self.entries) / (2**self.size)
        return None

    #The following two functions are an implementation of python's hashing function (see increment_pos() for collisions)
    def reset_pos(self, element):
        """ Set position to the beginning of where it should be for a given input element """
        self.pos = self.pos_str_elem(element) & (2**self.size-1)

    def increment_pos(self, perturb):
        """ A collision occured to get the next position pos should be set to """
        #Side note: '& (2**self.size-1)' is the same as '^ (2**self.size)'
        self.pos = ((5*self.pos) + 1 + perturb) & (2**self.size-1)
        perturb = perturb >> self.PERTURB_SHIFT
        return perturb

    def insert(self, element):
        """ Insert an element """
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
        """ find an element in the hashtable
        Returns the position if it is found else returns -1
        """
        self.reset_pos(element)
        perturb = self.pos_str_elem(element)
        while(self.htable[self.pos] != None):
            if element == self.htable[self.pos]:
                #Found it! Return where it's at.
                return self.pos
            else:
                #Didn't find it, check the next spot we would have put it in
                perturb = self.increment_pos(perturb)
        return -1


def main():
    """ main """
    htable = Hashtable()
    htable.insert("jason")
    htable.insert("don")
    htable.insert("kyle")
    htable.insert("chris")
    htable.insert("jim")

    htable.print_table()

    pos = htable.find("don")
    print("don found at {0}".format(pos))
    pos = htable.find("kyle")
    print("kyle found at {0}".format(pos))

    return None



if __name__ == "__main__":
    main()

