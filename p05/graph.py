#import ctypes
#import sys
#import getopt


#Psuedo code for adding to the graph:
#To add node 'A' with neighbors 'B','C' with lengths between them of 5 and 8 respectively:
#   graph['A'] = [{'B':5},{'C':8}];


class Graph(object):
    """ undirected graph class """

    def __init__(self, gmlfile=None):
        """ constructor 
        @param gmlfile optional file argument to load into the graph.
        """
        super(Graph, self).__init__()

        infile = open(gmlfile,'r')
        nextLineIsW = False

        for line in infile:
            sLine = line.strip()
            indent = ( len(line) - len(sLine) - 1 ) / 4
            words = sLine.split()

            if(sLine == ''):
                continue
            
            if(nextLineIsW and words[0] != "weight"):
                raise Exception("A neightbor line must be followed by a weight line. Check your input file {0}.".format(gmlfile))
        
            if(indent == 0 and words[0] == "graph"):
                self.graph = {};
                self.name = words[1]

            elif(indent == 1 and words[0] == "node"):
                name = words[1];
                self.add_node(name)

            elif(indent == 2 and words[0] == "neighbor"):
                neigh = words[1]
                nextLineIsW = True

            elif(indent == 3 and words[0] == "weight"):
                self.graph[name][neigh] = words[1]
                nextLineIsW = False
                #I could use eval around words[1] in the line above to store an int instead of a string but its irrelevant as far as the printout goes

        return None

    def add_node(self, node):
        """ add a node with the given ID
        Raises an error if the node already exists.
        @param node label for the node being added
        @return None
        """
        if node not in self.graph:
            self.graph[node] = {};
        else:
            raise Exception("Node already exists.")
        return None

    def add_edge(self, src, dst, weight=1):
        """ add an edge between two nodes
        Raises an error if the edge already exists.
        @param src label of the source node
        @param dst dst of the destination node
        @param weight weight of the edge
        @return 1 on success, 0 otherwise
        """
        if(self.graph[srs][dst] != None):
            self.graph[srs].append({dst:weight});
            self.graph[dst].append({srs:weight});
            return 1;
        else:
            raise Exception("Edge already exists.");
        return 0;

    def nodes(self):
        """ returns a list of all nodes """
        return self.graph.keys();

    def neighbors(self, node):
        """ list of neighbors of node `n`
        @param node node label
        @return list of neighbor node labels
        """
        return self.graph[node].keys()

    def degree(self, node):
        """ get the number of neighbors of a node
        @param node node label
        @return degree of node
        """
        return len(self.neighbors(node));

    def edge_weight(self, src, dst):
        """ get the weight of an edge 
        @param src source node label
        @param dst destination node label
        @return the weight of the edge
        """
        return self.graph[src][dst];

def main():

    #Text file g1 contains a basic graph as shown below:
    #           A
    #          / \
    #       1 /   \ 2
    #        /     \
    #       B       C
    #Text file g2 contains a circular graph as shown below:
    #           Jason
    #        3 /     \ 1
    #        Don    Kyle
    #          \_____/
    #             2
    infiles = ["g1.txt","g2.txt"]
    for files in infiles:
        print
        graph = Graph(files);
        nodes = graph.nodes()
        print("{0} has nodes {1}.".format(graph.name,nodes))
        for aNode in nodes:
            print("  Node {0} is of degree {1}.".format(aNode,graph.degree(aNode)))
            neighbors = graph.neighbors(aNode);
            print( "  The neighbors of {0} are {1}.".format(aNode,neighbors) )
            for neigh in neighbors:
                print("    The {0}-{1} edge has weight {2}.".format(aNode,neigh,graph.edge_weight(aNode,neigh)))

    #parser = ctypes.CDLL('/home/students/jjmaldonis/refreshx2/p05/parser/gml_parser.so')
    #testlib = ctypes.CDLL("libc.so.6")
    #print testlib.time(None)

    print
    print("END!")


if __name__ == "__main__":
    """ testing code """
    main();




