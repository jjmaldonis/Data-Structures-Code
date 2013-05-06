refreshx2
=========
Hashtables:
    Wastes space.
    Does need keep things in sorted order.
    You have to make a good hashfuntion - this can make things fast / optimized if you want to optimize for your data. Python's is good though in general.
    Insertion is fast.

Binary Search Tree:
    log N lookup time.
    Sorted order.

Array/Vector:
    Can keep in sorted order.
    log N lookup time by looking at the middle element each time.
    Insertion is slow.
    Deletion in the middle is slow (at the beginning as well but you can get around this by having a designated starting point, you just then may have trouble growing the array).

B-Tree:
    Array implementation of a binary tree. This is very useful when you can't store the entire binary tree data structure in memory. The nodes of a B-Tree are a list of the children of the current node (we visualize it something like this:   [->|10|->|20|->|30|->|] where -> represents a pointer to another node with all the numbers less than the following number in the list). Check out the book for more details, it really is necessary. DC thinks the B in B-Tree should stand for "block" because its like loading a block into memory; it isn't known what the B stands for actually.



Skip lists: Here is an implementation for some functions:
    nodestruct:
        next[]
        val

    def find(item):
        #We are going to return an array of nodes, and the array 'steps' will contains these. They will be the (rightmost) node at which we went down a level.
        #If the item exists, it will return the node containing the item at the beginning of the array 'steps'.
        #If the item does not exist in the list, the node before where the item would have been is returned at the beginning of the array 'steps'.
        steps = []
        node = self.head
        level = len(node.next) -1
        while(level >= 0):
            while(node.next[level] and node.next[level].val <= item):
                node = node.next[level]
            steps.append(node)
            level = level - 1
        return reversed(steps)

    def search(item):
        node = find(item)[0];
        if(node == self.head):
            return False;
        return (node.val == item)

    #This is an implementation of a Random-Height Skip List's insert function.
    #When finding the spot at which to insert, initially set the level to 0, then flip a coin, if heads, put item into the list at the level, if tails do level++; and repeat the coin toss.
    def insert(item):
        #We don't want to search because because it's a waste if the item isn't in there because you just have to call find again in the search function.
        node = find(item)
        if(node == self.head):
            #Item is not in there, but self.head does not have a .val so we must be careful.
        elif( node.val != item):
            #Now we know that node is the node before where we want to insert item.
            new = nodestruct()
            new.val = item
            #Generate a random number, either 0 or 1. Also, set a max height of 4.
            while( len(new.next) < 4 and random.getrandbits(1) ):
                    lvl = len(new.next)
                    new.next.append( node[lvl].next[level] )
                    #Now we need to change the pointers before the new node to point to it when they should.
                    node[level].next[level] = new;
            
        else:
            #The item is already in there because the last elif returned false (i.e. node.val == item).
            return False;


