

class Hashtable:
    PERTURB_SHIFT = 5

    def __init__(self):
        self.pos = 0
        self.size = 3 #this is the power of 2, not the actual size of the table
        self.htable = [None] * (2**self.size)
        self.entries = 0.0
        self.lf = 0.0 #load factor
        return None

    def print_table(self):
        for i in range(0,2**self.size):
            print( '  ' + self.htable[i] )

    def c_mul(self,a,b):
        return eval(hex((long(a) * b) & 0xFFFFFFFFL)[:-1])
    def pos_str_elem(self,element):
        value = ord(element[0]) << 7
        for char in element:
            value = self.c_mul(1000003, value) ^ ord(char)
        value = value ^ len(element)
        if value == -1:
            value = -2
        return value

    def rehash(self):
        print("Rehash table to size {}!".format(2**(self.size+1)))
        self.entries = 0.0
        self.pos = 0
        self.size = self.size + 1
        temphtable = self.htable[:] #copy old table
        self.htable = [None] * (2**self.size) #replace old table with new, bigger hash table
        for i in range(0,2**(self.size-1)):
            if(temphtable[i] != None):
                self.insert(temphtable[i])
            
        self.lf = (self.entries) / (2**self.size)
        #self.print_table()
        #print("Rehashing complete.")
        return None

    def reset_pos(self,element): #this is python's hashing function (see increment_pos() for collisions)
        self.pos = self.pos_str_elem(element) & (2**self.size-1)

    def increment_pos(self,perturb):
        self.pos = ((5*self.pos) + 1 + perturb) & (2**self.size-1) #the '& (2**self.size-1)' is the same as '^ (2**self.size)'
        perturb = perturb >> self.PERTURB_SHIFT
        #print(self.pos)
        return perturb

    def insert(self,element):
        self.reset_pos(element)
        perturb = self.pos_str_elem(element)
        while(self.htable[self.pos] != None): #navigate until we get to an open spot
            perturb = self.increment_pos(perturb)
        self.htable[self.pos] = element #;print("{0} was cast to {1}".format(element,self.pos))
        self.entries = self.entries + 1
        self.lf = ( self.entries ) / (2**self.size) #;print("load factor == {0}".format(self.lf))
        if(self.lf >= 2.0/3.0):
            self.rehash()
        return None

    def find(self,element):
        self.reset_pos(element)
        perturb = self.pos_str_elem(element)
        while(self.htable[self.pos] != None):
            if element == self.htable[self.pos]: #found it! return where it's at!
                return self.pos
            else: #didn't find it, check in the next spot we would have put it
                #print(self.htable[self.pos])
                perturb = self.increment_pos(perturb) #;print("didn't find {0}".format(element))
        return -1


def main():
    htable = Hashtable()
    htable.insert("jason")
    #htable.insert("jason")
    htable.insert("don")
    htable.insert("kyle")
    htable.insert("chris")
    htable.insert("jim")
    #htable.insert("lauri")
    #htable.insert("amanda")
    #htable.insert("joel")
    #htable.insert("donna")
    #htable.insert("june")
    #htable.insert("joe")

    htable.print_table()

    pos = htable.find("don")
    print("don found at {0}".format(pos))
    pos = htable.find("kyle")
    print("kyle found at {0}".format(pos))

    return None



if __name__ == "__main__":
    main()

