


#Graph.py
##Functions and initialization
Initialize a new graph using ... = Graph()
Functions include:
    add_node(node)
        Adds node to graph.
    add_edge(node1,node2,weight)
        Adds an edge between specified nodes. Nodes not already in the graph will be added. Weight parameter is optional and set to 1 if omitted.
    edge_weight(node1,node2)
        Returns the weight of the edge between nodes node1 and node2.
    degree(node)
        Returns the degree of node node.
    neighbors(node)
        Returns a list of the neighbors of node node.
    nodes()
        Returns a list of all the nodes in the graph.
    single_source_shortest_path(node)
        Returns a touple containing a list with the shortest distance to each other node as well as a dictionary containing each node as keys with the value of each key being the node from which the shortest path came from just before.
    
