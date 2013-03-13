import pdb
import math
import time
import sys
import getopt

from tree import BinarySearchTree

def max(a,b):
    if( a > b):
        return a
    else:
        return b

class AVLTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)
        #super(AVLTree, self).__init__(self)

    def fixSubtreeHeights(self,subtree):
        if(subtree['rchild'] != None ):
            self.fixSubtreeHeights(subtree['rchild'])
        if(subtree['lchild'] != None ):
            self.fixSubtreeHeights(subtree['lchild'])

        if(subtree['rchild'] == None and subtree['lchild'] == None):
            subtree['lheight'] = 0;
            subtree['rheight'] = 0;
        elif(subtree['rchild'] == None):
            subtree['rheight'] = 0;
            subtree['lheight'] = max( subtree['lchild']['lheight'], subtree['lchild']['rheight'] ) + 1;
        elif(subtree['lchild'] == None):
            #pdb.set_trace()
            subtree['lheight'] = 0;
            subtree['rheight'] = max( subtree['rchild']['lheight'], subtree['rchild']['rheight'] ) + 1;
        else:
            subtree['lheight'] = max( subtree['lchild']['lheight'], subtree['lchild']['rheight'] ) + 1;
            subtree['rheight'] = max( subtree['rchild']['lheight'], subtree['rchild']['rheight'] ) + 1;



    def balance(self,node,cb,p):
        #pdb.set_trace()
        if(cb == 'lchild' and node[cb]['rheight'] > node[cb]['lheight'] ): #double rotation
            node['lchild'] = node['rchild']['rchild']
            node['rchild']['rchild'] = node['rchild']['rchild'][not'rchild']
            node['lchild']['lchild'] = node['rchild']
            print("Fixing Heights.")
            self.fixSubtreeHeights(self.root)
        elif(cb == 'rchild' and node[cb]['lheight'] > node[cb]['rheight'] ): #double rotation
            node['rchild'] = node['lchild']
            node['lchild']['lchild'] = node['lchild']['lchild']['rchild']
            node['rchild']['rchild'] = node['lchild']
            print("Fixing Heights.")
            self.fixSubtreeHeights(self.root)
        if(p != None):
            print("Balancing {0}. Parent = {1}. Childbranch = {2}".format(node['object'],p['object'],cb))
        else:
            print("Balancing {0}. Parent = None. Childbranch = {1}".format(node['object'],cb))
        if( cb == 'lchild' ):
            notcb = 'rchild'
        else:
            notcb = 'lchild'
        if( p == None ):
            self.root = node[cb]
            node[cb] = node[cb][notcb]
            self.root[notcb] = node
            print("Fixing Heights.")
            self.fixSubtreeHeights(self.root)
            return self.root
        else:
            if( p['rchild'] == node ):
                pb = 'rchild'
                notpb = 'lchild'
            elif( p['lchild'] == node):
                pb = 'lchild'
                notpb = 'rchild'
            else:
                print("Oh crap.")
            print("Parentbranch = {0}".format(pb))
            p[pb] = node[cb]
            node[cb] = node[cb][notcb]
            p[pb][notcb] = node
            print("PRINTING TREE")
            self.__unicode__()
            print("Fixing Heights.")
            self.fixSubtreeHeights(self.root)
            return p[pb]


    def add(self, value, node=None, parent=None):
        #If no parent is provided then the user is calling "add" so set node to self.root for initial run through.
        if(value == 'viola'):
            pdb.set_trace()
        if(parent == None):
            node = self.root
        #Place value and return.
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
                print("Fixing Heights.")
                self.fixSubtreeHeights(self.root)
                while( math.fabs( node['lheight'] - node['rheight'] ) >= 2 ):
                    if(node['lheight'] - node['rheight'] > 0 ):
                        node = self.balance(node,'lchild',parent);
                    else:
                        node = self.balance(node,'rchild',parent);
                    print("PRINTING 2. Node = {0}".format(node['object']))
                    self.__unicode__()
                if( parent == None):
                    print("PRINTING 3. Node = {0}".format(node['object']))
                    self.__unicode__()
                    return True;
                print("PRINTING 5. Node = {0}".format(node['object']))
                self.__unicode__()
                return node;
        #Going right.
        elif(value > node['object']):
            child = self.add(value,node['rchild'],node)
            if ( child ):
                node['rchild'] = child;
                print("Fixing Heights.")
                self.fixSubtreeHeights(self.root)
                while( math.fabs( node['rheight'] - node['lheight'] ) >= 2 ):
                    if(node['lheight'] - node['rheight'] > 0 ):
                        node = self.balance(node,'lchild',parent);
                    else:
                        node = self.balance(node,'rchild',parent);
                    print("PRINTING 2. Node = {0}".format(node['object']))
                    self.__unicode__()
                if( parent == None):
                    print("PRINTING 3. Node = {0}".format(node['object']))
                    self.__unicode__()
                    return True;
                print("PRINTING 6. Node = {0}".format(node['object']))
                self.__unicode__()
                return node;
        return False;



def main():
    print("Hello World")
    start = time.time()

    infile = open(sys.argv[1],'r')
    line = infile.readline()
    #Check to see if the input file was blank
    if (line == ''):
        return None

    tree = AVLTree()

    while(line != ''):
        print
        #print( "\"{0}\" was put into the tree == {1}".format(line[:-1], tree.add(line[:-1])))
        print( "\"{0}\" was put into the tree".format(line[:-1]))
        tree.add(line[:-1])
        tree.__unicode__()
        line = infile.readline() #get rid of the elo character

    return 0;


if __name__ == "__main__":
    main()
