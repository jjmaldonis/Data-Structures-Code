#Project Description
This code implements an undirected graph with nodes, neighbors, and weighed edges between nodes. It prints out the shortest distance from one node to another along with the path of the shortest distance.

#Code Description
This code takes an input file from the command line and reads in and stores a graph from that file. The code then prints out the shortest distance from one node to another along with the path of the shortest distance. The code is fairly self explanitory. Dijkstrata's algorithm to compute the shortest path is used. One thing I left that I did not change is the __init__ function taking the filename as a parameter. I like this implementation because then you aren't separating where the file comes from and where the data is coming from that you are using for the graph initilization.

#Execution instructions
From a terminal run 'python dijskrata.py <your input filename> <optional: the nodes you want to print out the shortest path of (all others will be omitted in the output)>'. Your input file must be in the same directory as the dijskrata.py file and must have the line format <node1> <node2> <optional: weight> separated by spaces. If the weight is omitted it will automatticaly be set to 1 (i.e. an unweighted graph). No lines can be left blank and all must have this exact format. Your input file must not repeat any edge or an exception will be called.

#Reflection
I liked this project. It was interesting to find a viable use of storing dictionaries inside of dictionaries.
After completing this project I am not sure how optimized it is and that is something I would like to improve (without losing readability). It would have been cool to figure out how to implement the gml parser code into our init algorithm to comply with the gml standards (can you create an excecutable / library / something from the C++ parser code and implement it in your python code - because that would be awesome).
I did not have much trouble writing this portion of the project at all. All of the python implementation we went over in class while doing the distraka algorthm was awesome because I was able to code so much faster and confidently.
I liked what we went over in class as far as you telling us what we should have known beforehand. That helped considerably. The distraka algorithm classes helped a ton and keeping track of the path was interesting to add in.
