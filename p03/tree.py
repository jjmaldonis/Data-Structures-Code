# -*- coding: utf-8 -*-

import time
import sys
import getopt

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
        if(subtree['lchild'] != None ):
            self.makeEmpty(subtree['lchild'])

        #By the time we get here we will be working bottom up so everything below the current node will be gone.
        subtree = None
 

    def balance(self,node):
        print("Balancing {0}".format(node['object']))
        pass

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

    def __unicode__(self, cur=u"", pfx=u"", node=None):
        #A complex funtion that you will have to work through to understand. It's not so bad though if you ignore the cur and pfx arguments which are just for formatting.
        if( node == None):
            node = self.root
        print("{0}{1}{2} [{3},{4}]".format( pfx, cur, node['object'], node['lheight'], node['rheight'] ) )
        if( node['rchild'] != None ):
            if( node['lchild'] != None ):
                self.__unicode__(u"\\", pfx + u"| ", node['rchild'])
            else:
                self.__unicode__(u"\\", pfx + u"  ", node['rchild'])
        if( node['lchild'] != None ):
            self.__unicode__(u"-", pfx + u" ", node['lchild'])
        return None;

def main():
    start = time.time()

    infile = open(sys.argv[1],'r')
    line = infile.readline()

    #Check to see if the input file was blank
    if (line == ''):
        return None

    tree = BinarySearchTree()

    while(line != ''):
        print
        print( "\"{0}\" was put into the tree == {1}".format(line[:-1], tree.add(line[:-1])))
        tree.__unicode__()
        line = infile.readline()

    return 0;

if __name__ == "__main__":
    main()
