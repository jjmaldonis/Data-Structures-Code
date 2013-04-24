import heapq
import sys


class Graph(object):
    """ undirected graph class """

    def __init__(self, gmlfile=None):
        """ constructor 
        @param gmlfile optional file argument to load into the graph.
        """
        if gmlfile is None:
            raise Exception("No input graph file was given.")

        super(Graph, self).__init__()
        infile = open(gmlfile,'r')
        self.graph = {}
        for line in infile:
            words = line.split()

            # If there are an incorrect number of words / variables on this input line raise an exception.
            if(len(words) != 2 and len(words) != 3):
                raise Exception("Number of arguments per line in input file is not 2 or 3.")
            if(len(words) == 3):
                self.add_edge(words[0], words[1], eval(words[2]))
            else:
                self.add_edge(words[0], words[1])
        return None

    def add_node(self, node):
        """ add a node with the given ID
        Raises an error if the node already exists.
        @param node label for the node being added
        @return None
        """
        if node not in self.graph:
            raise Exception("Node already exists.")
        self.graph[node] = {}

    def add_edge(self, src, dst, weight=1):
        """ add an edge between two nodes
        Raises an error if the edge already exists.
        @param src label of the source node
        @param dst dst of the destination node
        @param weight weight of the edge
        @return 1 on success, 0 otherwise
        """
        if( src not in self.graph.keys() ):
            self.add_node(src)
        if( dst not in self.graph.keys() ):
            self.add_node(dst)
        try:
            self.graph[src][dst]
        except:
            self.graph[src][dst] = weight
            self.graph[dst][src] = weight
            return 1
        raise Exception("Edge already exists.")
        return 0

    def nodes(self):
        """ returns a list of all nodes """
        # Note that returning this returns a LIST whereas self.graph is a dictionary. Therefore a user searching through this (and having to use the list) is much slower than the programmer's search.
        return self.graph.keys()

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
        return len(self.neighbors(node))

    def edge_weight(self, src, dst):
        """ get the weight of an edge 
        @param src source node label
        @param dst destination node label
        @return the weight of the edge
        """
        return self.graph[src][dst]

    def __unicode__(self):
        return unicode(self)
    
    def single_source_shortest_path(self, n):
        # A heap pops off the thing that is the lowest in the heap so we make queue a heap.
        queue = []
        # Inserting as a tuple
        heapq.heappush(queue, (0, n))
        dist = {n:0}
        path = {n:None}
        visited = {}
        while(len(queue)):
            # Insert a touple into the heap to keep the order correct (order goes by the first element first). Note that weight is unused but I will leave it for potential future changes.
            weight, curnode = heapq.heappop( queue )
            if curnode in visited:
                continue
            visited[curnode] = True
            for nnode in self.graph[curnode]:
                neighDist = dist[curnode] + self.graph[curnode][nnode]
                if nnode not in dist or neighDist < dist[nnode]:
                    dist[nnode] = neighDist
                    path[nnode] = curnode
                    heapq.heappush(queue, (neighDist, nnode) )
        return dist, path



def main():
    graph = Graph(sys.argv[1])

    if(len(sys.argv) == 2):
        nodes = graph.nodes()
    else:
        nodes = sys.argv[2:]

    # Create a heap for the printout so we can print in shortest-path-first order.
    printout = []

    # For each node that the user wants us to calculate the shortest paths for, do it and print the results.
    for aNode in nodes:
        # Calculate shortest paths
        dist, path = graph.single_source_shortest_path(aNode)
        for node in dist:
            # For each node connected to aNode compute the path to get there and put the results into the printout heap (in order using touples).
            if(aNode != node):
                thisPath = ''
                temp = node
                while(path[temp] != aNode):
                    thisPath = path[temp] + ', ' + thisPath
                    temp = path[temp]
                thisPath = path[temp] + ', ' + thisPath + node
                printline = "{0} -> {1} \t {2} \t {3}".format(aNode, node, dist[node], thisPath)
                heapq.heappush( printout, (dist[node], len(printline), printline) )
        # Print the heap and empty it.
        while(printout):
            print(heapq.heappop(printout)[2])
        print



if __name__ == "__main__":
    """ testing code """
    main()
