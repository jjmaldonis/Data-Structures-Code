import random
import math
import time
import sys
from cStringIO import StringIO

def max(a,b):
    if( a > b):
        return a
    else:
        return b

class BinarySearchTree:

    def __init__(self):
        self.root = None
        return None;


    def isEmpty(self):
        if(self.root == None):
            return True;
        else:
            return False;


    def makeEmpty(self,subtree=None):
        if(subtree == None):
            subtree = self.root
        if(subtree['rchild'] != None ):
            self.makeEmpty(subtree['rchild'])
            subtree['rchild'] = None
        if(subtree['lchild'] != None ):
            self.makeEmpty(subtree['lchild'])
            subtree['lchild'] = None
        if(subtree == self.root):
            self.root = None
 

    def add(self, value, node=None, parent=None):
        #If no parent is provided then the user is calling "add" so set node to self.root for initial run through.
        if(parent == None):
            node = self.root

        #Place value and return if we have found an open spot.
        if(node == None):
            node = {'object':value,'lchild':None,'rchild':None,'lheight':0,'rheight':0}
            if( parent == None):
                self.root = node
                return True
            return node;

        #Going left.
        if(value < node['object']):
            child = self.add(value,node['lchild'],node)
            if( child ):
                node['lchild'] = child;
                if( node['lchild'] and node['rchild'] ):
                    node['lheight'] = max( max(node['lchild']['lheight'], node['lchild']['rheight'] ) + 1, max(node['rchild']['lheight'], node['rchild']['rheight'] ) );
                elif( node['lchild'] ):
                    node['lheight'] = max( node['lchild']['lheight'], node['lchild']['rheight']) + 1
                elif( node['rchild'] ):
                    node['lheight'] = max( node['rchild']['lheight'], node['rchild']['rheight'])
                else:
                    node['lheight'] += 1
                if( node['lheight'] - node['rheight'] >= 2 ):
                    self.balance(node);
                if( parent == None):
                    return True;
                return node;

        #Going right.
        elif(value > node['object']):
            child = self.add(value,node['rchild'],node)
            if ( child ):
                node['rchild'] = child;
                if( node['lchild'] and node['rchild'] ):
                    node['rheight'] = max( max(node['lchild']['lheight'], node['lchild']['rheight']), max(node['rchild']['lheight'], node['rchild']['rheight'] ) + 1 );
                elif( node['lchild'] ):
                    node['rheight'] = max( node['lchild']['lheight'], node['lchild']['rheight'] )
                elif( node['rchild'] ):
                    node['rheight'] = max( node['rchild']['lheight'], node['rchild']['rheight'] ) + 1
                else:
                    node['rheight'] += 1
                if( node['rheight'] - node['lheight'] >= 2 ):
                    self.balance(node);
                if( parent == None):
                    return True;
                return node;
        return False;


    def __getitem__(self, value, node=None, parent=None):
        #Recursive function that is based on its previous return value. It's really pretty self explanatory.
        if( node == None):
            node = self.root
        if( node == None):
            return False
        if (node['object'] == value ):
            return True
        elif( value < node['object'] ):
            if (node['lchild'] != None ):
                if( self.__getitem__(value, node['lchild'], node) ):
                    return True
        elif( value > node['object'] ):
            if( node['rchild'] != None ):
                if( self.__getitem__(value, node['rchild'], node) ):
                    return True
        return False


    def __unicode__(self, cur=u"", pfx=u"", node=None, output=sys.stdout):
        fullOut = ""
        mystdout = StringIO()
        if( output == "string" and sys.stdout != StringIO() ):
            old_stdout = sys.stdout
            sys.stdout = mystdout
        #A complex funtion that you will have to work through to understand. It's not so bad though if you ignore the cur and pfx arguments which are just for formatting.
        if( self.root == None ):
            return None
        if( node == None):
            node = self.root
        print("{0}{1}{2} [{3},{4}]".format( pfx, cur, node['object'], node['lheight'], node['rheight'] ) )
        if( node['rchild'] != None ):
            fullOut += self.__unicode__(u"\\", pfx + u"| ", node['rchild'], output)
        if( node['lchild'] != None ):
            fullOut += self.__unicode__(u"-", pfx + u" ", node['lchild'], output)
        if( output == "string" ):
            sys.stdout = old_stdout
        return mystdout.getvalue() + fullOut


class AVLTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)



    def fixSubtreeHeights(self,subtree):
        if(subtree['rchild'] != None ):
            self.fixSubtreeHeights(subtree['rchild'])
        if(subtree['lchild'] != None ):
            self.fixSubtreeHeights(subtree['lchild'])
        # By the time we get here we will be working bottom up so everything
        #   below the current node will have the correct height.
        if subtree['rchild'] is not None:
            subtree['rheight'] = max(subtree['rchild']['lheight'], subtree['rchild']['rheight']) + 1;
        else:
            subtree['rheight'] = 0;
        if subtree['lchild'] is not None:
            subtree['lheight'] = max(subtree['lchild']['lheight'], subtree['lchild']['rheight']) + 1;
        else:
            subtree['lheight'] = 0;



    def balance(self,node,cb,p):
        # Check if we need to do a double rotation. If so, do it.
        if(cb == 'lchild' and node[cb]['rheight'] > node[cb]['lheight'] and math.fabs( node['lheight'] - node['rheight'] ) >= 2 ):
            self.balance(node[cb],'rchild',node)
        elif(cb == 'rchild' and node[cb]['lheight'] > node[cb]['rheight'] and math.fabs( node['lheight'] - node['rheight'] ) >= 2 ):
            self.balance(node[cb],'lchild',node)

        # Set a direction variable.
        if( cb == 'lchild' ):
            notcb = 'rchild'
        else:
            notcb = 'lchild'
        # If there is no parent we have to do our re-routing slightly different.
        if( p == None ):
            self.root = node[cb]
            node[cb] = node[cb][notcb]
            self.root[notcb] = node

            # Fix heights.
            self.fixSubtreeHeights(self.root)

            # Return the replaced node.
            return self.root

        # There is a parent, so do our re-routing accordingly.
        else:
            # Set another direction variable.
            if( p['rchild'] == node ):
                pb = 'rchild'
                notpb = 'lchild'
            elif( p['lchild'] == node):
                pb = 'lchild'
                notpb = 'rchild'
            p[pb] = node[cb]
            node[cb] = node[cb][notcb]
            p[pb][notcb] = node

            #Fix heights.
            self.fixSubtreeHeights(self.root)

            # Return the replaced node.
            return p[pb]



    def add(self, value, node=None, parent=None):
        # If no parent is provided then the user is calling "add"
        #   so set node to self.root for initial run through.
        if(parent == None):
            node = self.root

        # Place value and return if we have found an empty spot.
        if(node == None):
            node = {'object':value,'lchild':None,'rchild':None,'lheight':0,'rheight':0}
            if( parent == None):
                self.root = node
                return True
            return node

        # Going left recursively.
        if(value < node['object']):

            # I am being very careful with my return statements in this function
            #   because of this next time. I don't want 'child' set to True or
            #   False.
            child = self.add(value, node['lchild'], node)
            if( child ):
                node['lchild'] = child

                # Fix heights because we did some re-routing.
                self.fixSubtreeHeights(self.root)

                # Check if we need to balance. Balance recursively if necessary.
                while( math.fabs( node['lheight'] - node['rheight'] ) >= 2 ):
                    if(node['lheight'] - node['rheight'] > 0 ):
                        node = self.balance(node, 'lchild', parent)
                    else:
                        node = self.balance(node, 'rchild', parent)

                # If there is no parent we need to return True because we
                #   are at the top and we want the overall add function
                #   to return True / False.
                if( parent == None):
                    return True
                return node

        # Going right recursively.
        elif(value > node['object']):

            # I am being very careful with my return statements in this function
            #   because of this next time. I don't want 'child' set to True or
            #   False.
            child = self.add(value, node['rchild'], node)
            if ( child ):
                node['rchild'] = child

                # Fix heights because we did some re-routing.
                self.fixSubtreeHeights(self.root)

                # Check if we need to balance. Balance recursively if necessary.
                while( math.fabs( node['rheight'] - node['lheight'] ) >= 2 ):
                    if(node['lheight'] - node['rheight'] > 0 ):
                        node = self.balance(node, 'lchild', parent)
                    else:
                        node = self.balance(node, 'rchild', parent)

                # If there is no parent we need to return True because we are
                #   at the top and we want the overall add function to
                #   return True / False.
                if( parent == None):
                    return True
                return node

        # If we got here then the value already exists, so return False.
        return False




def main():
    print("Hello World!")
    start = time.time()

    print("Initializing tree...")
    tree = AVLTree()

    print("Testing if tree is empty...")
    assert tree.isEmpty()

    print("Adding 1 to the tree...")
    tree.add(1)
    print("Testing if tree is empty...")
    assert not tree.isEmpty()
    print("Searching for 1...")
    assert tree.__getitem__(1)
    print("Searching for 2 which should not be in the tree...")
    assert not tree.__getitem__(2)

    print("Adding 1 again and checking to make sure it was not added again...")
    tree.add(1)
    output = tree.__unicode__(output="string")
    assert output == "1 [0,0]\n"

    print("Making tree empty, searching for 1, and checking if tree is empty...")
    tree.makeEmpty()
    assert not tree.__getitem__(1)
    assert tree.isEmpty()

    print("Adding nodes (in this order) 5, 4, 8, 9, 6, 7 which creates a double rotation when adding 7 to balance correctly. ")
    print("Checking to make sure this does indeed balance correctly...")
    tree.add(5)
    tree.add(4)
    tree.add(8)
    output = tree.__unicode__(output="string")
    assert output == u"5 [1,1]\n| \8 [0,0]\n -4 [0,0]\n"
    tree.add(9)
    tree.add(6)
    output = tree.__unicode__(output="string")
    assert output == u"5 [1,2]\n| \8 [1,1]\n| | \9 [0,0]\n|  -6 [0,0]\n -4 [0,0]\n"
    tree.add(7)
    output = tree.__unicode__(output="string")
    assert output == u"6 [2,2]\n| \8 [1,1]\n| | \9 [0,0]\n|  -7 [0,0]\n -5 [1,0]\n  -4 [0,0]\n"

    print("Creating and adding a list of 20 random numbers between 0 and 100...")
    elementsToAdd = random.sample(range(0,100),20)
    for item in elementsToAdd:
        tree.add(item)

    print("Looking for which items were added and making sure they were all added while also ensuring nothing else was added...")
    found = []
    for item in range(0,100):
        if tree.__getitem__(item):
            found.append(item)
    assert sorted(found) == list(set(elementsToAdd+[5,4,8,9,6,7]))

    print("Lastly, print the tree...")
    tree.unicode()


    print("All tests successful.")
    return 0


if __name__ == "__main__":
    main()
