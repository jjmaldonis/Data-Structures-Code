


#Graph.py
##Functions and initialization
Initialize a new graph using ... = Graph()

Functions include:\n

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
    

#Hashtable
##Functions and initialization
Initialize a new hashtable using ... = Hashtable()

Functions include:

    get_size()

        Returns the size of the hashtable.

    get_load()

        Returns the current load of the hashtable.

    insert(element)

        Inserts element into the table. Raises an exception if the element is already in there.

    find(element)

        Searches for element in the hashtable. If the element is found, the position of it is returned; if the element is not found, -1 is returned.

    print_table()

        Prints the hashtable for viewing purposes. Skips empty cells for clarity purposes.




#AVL Tree
##Functions and initialization
Initialize a new AVL tree using ... = AVLTree()

Functions include:

    add(item)

        Adds an item into the tree. Returns True on success and False otherwise. Items that are already in the tree are not re-added.

    __getitem__(item)

        Returns True if the item is in the tree and False otherwise.

    __unicode__(output=optional)

        If no argument is passed it will print the tree to the terminal, returning an empty string.

        If the argument output="string" is passed (note that output= is necessary to specify) then instead of printing the tree, it will be returned by the function in string format.

    makeEmpty()

        Removes all items from the tree, making an empty tree.

    isEmpty()

        Returns True if the tree is empty, False otherwise.



Note: DC said I should not have more than 3 levels of indentation in my AVL Tree because it can get hard to follow. However, I'm going to leave it because I actually think I'd get more confused if I did that; and my comments are good and quite helpful.
