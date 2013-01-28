

class Hashtable:

    def __init__(self):
        self.pos = 0
        self.size = 3 #this is the power of 2, not the actual size of the table
        self.htable = [''] * (2**self.size)
        self.entries = 0.0
        self.lf = 0.0 #load factor
        return None

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

    def increment_pos(self):
        self.pos = ((5*self.pos) + 1) % (2**self.size) #if you change this makes sure its still a function of self.size


    def rehash(self):
        print("Rehash table to size {}!".format(2**(self.size+1)))
        self.entries = 0.0
        self.pos = 0
        self.size = self.size + 1
        temphtable = self.htable[:] #copy old table
        self.htable = [''] * (2**self.size) #replace old table with new, bigger hash table
        for i in range(0,2**(self.size-1)):
            if(temphtable[i] != ''):
                self.insert(temphtable[i])
            
        self.lf = (self.entries) / (2**self.size)
        print("Rehashing complete.")
        return None

    def insert(self,element):
        self.pos = self.pos_str_elem(element) % self.size
        placed = False
        while(placed == False):
            if(self.htable[self.pos] == ''):
                self.htable[self.pos] = element
                placed = True
            else:
                self.increment_pos()

        self.entries = self.entries + 1
        self.lf = ( self.entries ) / (2**self.size)
        #print("load factor == {0}".format(self.lf))
        if(self.lf >= 2.0/3.0):
            self.rehash()
        return None


    def find(self,element):
        self.pos = self.pos_str_elem(element) % self.size
        for i in range(0,2**self.size):
            if element == self.htable[self.pos]:
                return self.pos
            else:
                self.increment_pos()
        return -1

    def print_table(self):
        for i in range(0,2**self.size):
            print( '  ' + self.htable[i] )




def main():
    htable = Hashtable()
    htable.insert("jason")
    htable.insert("jason")
    htable.insert("don")
    htable.insert("kyle")
    htable.insert("chris")
    htable.insert("jim")
    htable.insert("lauri")
    htable.insert("amanda")
    htable.insert("joel")
    htable.insert("donna")
    htable.insert("june")
    htable.insert("joe")

    pos = htable.find("joel")
    print("item found at {0}".format(pos))

    htable.print_table()
    return None



if __name__ == "__main__":
    main()

