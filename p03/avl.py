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
            subtree['lheight'] = 0;
            subtree['rheight'] = max( subtree['rchild']['lheight'], subtree['rchild']['rheight'] ) + 1;
        else:
            subtree['lheight'] = max( subtree['lchild']['lheight'], subtree['lchild']['rheight'] ) + 1;
            subtree['rheight'] = max( subtree['rchild']['lheight'], subtree['rchild']['rheight'] ) + 1;



    def balance(self,node,cb,p):
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
        else:
            if( p['rchild'] == node ):
                pb = 'rchild'
                notpb = 'lchild'
            elif( p['lchild'] == node):
                pb = 'lchild'
                notpb = 'rchild'
            else:
                print("Oh crap.")
            #if(pb != cb): #double rotation
                #self.balance()
            print("Parentbranch = {0}".format(pb))
            #print("{0} set to {1}".format(p[pb]['object'],node[cb]['object']))
            p[pb] = node[cb]
            #print("{0} set to {1}".format(node[cb]['object'],node[cb][notcb]['object']))
            node[cb] = node[cb][notcb]
            #print("{0} set to {1}".format(p[pb][notcb]['object'],node['object']))
            p[pb][notcb] = node #should that be notpb??? instead of notcb???
            #p[pb] = node[cb][notcb]
            print(p[pb]['object'])
            print("PRINTING TREE")
            self.__unicode__()

            self.fixSubtreeHeights(self.root)
        return None

    def add(self, value, node=None, parent=None):
        #If no parent is provided then the user is calling "add" so set node to self.root for initial run through.
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
                self.fixSubtreeHeights(self.root)
                #if( node['lchild'] and node['rchild'] ):
                    #node['lheight'] = max( max(node['lchild']['lheight'], node['lchild']['rheight'] ) + 1, max(node['rchild']['lheight'], node['rchild']['rheight'] ) );
                #elif( node['lchild'] ):
                    #node['lheight'] = max( node['lchild']['lheight'], node['lchild']['rheight']) + 1
                #elif( node['rchild'] ):
                    #node['lheight'] = max( node['rchild']['lheight'], node['rchild']['rheight'])
                #else:
                    #node['lheight'] += 1
                if( node['lheight'] - node['rheight'] >= 2 ):
                    self.balance(node,'lchild',parent);
                    print("PRINTING 2. Node = {0}".format(node['object']))
                    self.__unicode__()
                if( parent == None):
                    print("PRINTING 3. Node = {0}".format(node['object']))
                    self.__unicode__()
                    return True;
                self.fixSubtreeHeights(self.root)
                print("PRINTING 5. Node = {0}".format(node['object']))
                self.__unicode__()
                return node;
        #Going right.
        elif(value > node['object']):
            child = self.add(value,node['rchild'],node)
            if ( child ):
                node['rchild'] = child;
                self.fixSubtreeHeights(self.root)
                #if( node['lchild'] and node['rchild'] ):
                    #node['rheight'] = max( max(node['lchild']['lheight'], node['lchild']['rheight']), max(node['rchild']['lheight'], node['rchild']['rheight'] ) + 1 );
                #elif( node['lchild'] ):
                    #node['rheight'] = max( node['lchild']['lheight'], node['lchild']['rheight'] )
                #elif( node['rchild'] ):
                    #node['rheight'] = max( node['rchild']['lheight'], node['rchild']['rheight'] ) + 1
                #else:
                    #node['rheight'] += 1
                if( node['rheight'] - node['lheight'] >= 2 ):
                    self.balance(node,'rchild',parent);
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
