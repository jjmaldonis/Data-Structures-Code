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



    def fixSubtreeHeights(self,subtree):
        if(subtree['rchild'] != None ):
            self.fixSubtreeHeights(subtree['rchild'])
        if(subtree['lchild'] != None ):
            self.fixSubtreeHeights(subtree['lchild'])
        #By the time we get here we will be working bottom up so everything below the current node will have the correct height.
        if(subtree['rchild'] == None and subtree['lchild'] == None):
            subtree['lheight'] = 0;
            subtree['rheight'] = 0;
        elif(subtree['rchild'] == None):
            subtree['rheight'] = 0;
            subtree['lheight'] = max( subtree['lchild']['lheight'], subtree['lchild']['rheight'] ) + 1;
        elif(subtree['lchild'] == None):
            subtree['lheight'] = 0;
            subtree['rheight'] = max( subtree['rchild']['lheight'], subtree['rchild']['rheight'] ) + 1;
        else:
            subtree['lheight'] = max( subtree['lchild']['lheight'], subtree['lchild']['rheight'] ) + 1;
            subtree['rheight'] = max( subtree['rchild']['lheight'], subtree['rchild']['rheight'] ) + 1;



    def balance(self,node,cb,p):
        #Check if we need to do a double rotation. If so, do it.
        if(cb == 'lchild' and node[cb]['rheight'] > node[cb]['lheight'] and math.fabs( node['lheight'] - node['rheight'] ) >= 2 ):
            self.balance(node[cb],'rchild',node)
        elif(cb == 'rchild' and node[cb]['lheight'] > node[cb]['rheight'] and math.fabs( node['lheight'] - node['rheight'] ) >= 2 ):
            self.balance(node[cb],'lchild',node)

        #Set a direction variable.
        if( cb == 'lchild' ):
            notcb = 'rchild'
        else:
            notcb = 'lchild'
        #If there is no parent we have to do our re-routing slightly different.
        if( p == None ):
            self.root = node[cb]
            node[cb] = node[cb][notcb]
            self.root[notcb] = node

            #Fix heights.
            self.fixSubtreeHeights(self.root)

            #Return the replaced node.
            return self.root

        #There is a parent, so do our re-routing accordingly.
        else:
            #Set another direction variable.
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

            #Return the replaced node.
            return p[pb]



    def add(self, value, node=None, parent=None):
        #If no parent is provided then the user is calling "add" so set node to self.root for initial run through.
        if(parent == None):
            node = self.root

        #Place value and return if we have found an empty spot.
        if(node == None):
            node = {'object':value,'lchild':None,'rchild':None,'lheight':0,'rheight':0}
            if( parent == None):
                self.root = node
                return True
            return node;

        #Going left recursively.
        if(value < node['object']):

            #I am being very careful with my return statements in this function because of this next time. I don't want 'child' set to True or False.
            child = self.add(value,node['lchild'],node)
            if( child ):
                node['lchild'] = child;

                #Fix heights because we did some re-routing.
                self.fixSubtreeHeights(self.root)

                #Check if we need to balance. Balance recursively if necessary.
                while( math.fabs( node['lheight'] - node['rheight'] ) >= 2 ):
                    if(node['lheight'] - node['rheight'] > 0 ):
                        node = self.balance(node,'lchild',parent);
                    else:
                        node = self.balance(node,'rchild',parent);

                #If there is no parent we need to return True because we are at the top and we want the overall add function to return True / False.
                if( parent == None):
                    return True;
                return node;

        #Going right recursively.
        elif(value > node['object']):

            #I am being very careful with my return statements in this function because of this next time. I don't want 'child' set to True or False.
            child = self.add(value,node['rchild'],node)
            if ( child ):
                node['rchild'] = child;

                #Fix heights because we did some re-routing.
                self.fixSubtreeHeights(self.root)

                #Check if we need to balance. Balance recursively if necessary.
                while( math.fabs( node['rheight'] - node['lheight'] ) >= 2 ):
                    if(node['lheight'] - node['rheight'] > 0 ):
                        node = self.balance(node,'lchild',parent);
                    else:
                        node = self.balance(node,'rchild',parent);

                #If there is no parent we need to return True because we are at the top and we want the overall add function to return True / False.
                if( parent == None):
                    return True;
                return node;

        #If we got here then the value already exists, so return False.
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
        print( "Putting \"{0}\" into the tree".format(line[:-1]))
        tree.add(line[:-1])

        #Print the tree
        tree.__unicode__()
        line = infile.readline()

    return 0;


if __name__ == "__main__":
    main()
