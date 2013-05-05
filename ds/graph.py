import heapq


class Graph(object):
    """ undirected graph class """

    def __init__(self):
        """ constructor 
        No parameters, simple constructor
        """
        super(Graph, self).__init__()
        self.graph = {}

    def add_node(self, node):
        """ add a node with the given ID
        Raises an error if the node already exists.
        @param node label for the node being added
        @return None
        """
        if node in self.graph:
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
        if type(weight) is not type(1) or type(weight) is not type(0.1):
            raise Exception("Weight must be a number.")
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

    print("Initializing graph...")
    graph = Graph()

    nodesToAdd = ["A","B","C","D","E","F","G"]
    edges = {"A":[{"B":1}], "B":[{"C":2}], "C":[{"A":1},{"D":5}], "D":[{"E":2},{"F":3}]}

    print("Testing if graph.nodes() is empty...")
    assert graph.nodes() == []

    print("Adding node 'A'...")
    graph.add_node("A")
    assert graph.nodes() == ["A"]

    print("Adding adge A-B with weight 1...")
    graph.add_edge("A","B",1)
    assert graph.nodes() == ["A","B"]

    print("Adding all nodes...")
    # For each node that the user wants us to calculate the shortest paths for, do it and print the results.
    for aNode in nodesToAdd:
        try:
            graph.add_node(aNode)
        except:
            if(aNode is not "A" and aNode is not "B"):
                raise Exception("Problem! Node {0} was incorrectly handled when added.".format(aNode))

    assert sorted(graph.nodes()) == nodesToAdd

    print("Adding all edges...")
    for anEdge in edges.keys():
        for edge2 in edges[anEdge]:
            try:
                graph.add_edge(anEdge,(edge2.keys())[0],edge2[edge2.keys()[0]])
            except:
                if(anEdge != "A" and edge2.keys()[0] != "B"):
                    raise Exception("Problem! Edge {0}-{1} was incorreclty handled when added.".format(anEdge,edge2.keys()[0]))

    print("Testing neighbors, degree, and edge_weight functions...")
    assert graph.neighbors("D") == ["C","E","F"]
    assert graph.degree("C") == 3
    assert graph.edge_weight("C","D") == 5

    print("Calculating and checking shortest paths...")
    # Create a heap to store path information in
    printout = []
    # Calculate shortest paths from aNode to all other nodes
    aNode = "A"
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

    assert "A -> B \t 1 \t A, B" == heapq.heappop(printout)[2]
    assert "A -> C \t 1 \t A, C" == heapq.heappop(printout)[2]
    assert "A -> D \t 6 \t A, C, D" == heapq.heappop(printout)[2]
    assert "A -> E \t 8 \t A, C, D, E" == heapq.heappop(printout)[2]
    assert "A -> F \t 9 \t A, C, D, F" == heapq.heappop(printout)[2]

    print("All tests succeeded.")



if __name__ == "__main__":
    """ testing code """
    main()
