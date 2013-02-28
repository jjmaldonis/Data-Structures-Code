#Project Description
This code implements a sorted binary search tree without AVL balancing.

#Code Description
My code creates a dictionary that represents a node. This node contains the node value, its right child, left child, left subtree height, and right subtree height. Nodes are then created in the add function in the appropriate spot (so the tree is sorted). The tree can also be printed, and items can be looked up. The algorithms are standard binary search tree algorithms.

#Execution Instructions
Create a word list file containing the words you want to add into the binary tree (numbers will work as well; in fact anything that can be compared using > and < will work). From the teriminal, execute 'python tree.py [your word list]'. You can modify the code in tree.py's main() funtion to do new prints if you want.

#Reflection
The most interesting thing was implementing the add(object) funtionality because it really taught me how binary search trees are implemented. My code isn't perfect right now, and I can probably clean it up quite a bit.
After completing this part of the project I am still not sure how I will implement the AVL portion of the tree because I don't exactly know how to change all the pointers, so I need to figure that out. We did some in class but I just need to do it on my own to practice.
The largest problem I faced was getting the heights of the binary trees correct. I ended up just having to go through my algorithm line by line and write out my debug session on paper to figure it out. I finally did.
I liked that you went over the unicode function in class. That helped a lot and I would definitely do that again in the future.
