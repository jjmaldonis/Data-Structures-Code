#Project Description
This code implements a sorted binary search tree without AVL balancing.

#Code Description
My tree.py code creates a dictionary that represents a node. This node contains the node value, its right child, left child, left subtree height, and right subtree height. Nodes are then created in the add function in the appropriate spot (so the tree is sorted). The tree can also be printed, and items can be looked up. The algorithms are standard binary search tree algorithms. Furthermore, my avl.py code impelements avl balancing on top of the binary tree implemented in tree.py. Heights are all correctly calculted.

#Execution Instructions
Create a word list file containing the words you want to add into the binary tree (numbers will work as well; in fact anything that can be compared using > and < will work). From the teriminal, execute 'python tree.py [your word list]' OR 'python avl.py [your word list]'. You can modify the code in tree.py's / avl.py's main() funtion to do new prints if you want.

#Reflection
The most interesting thing was implementing the add(object) funtionality because it really taught me how binary search trees are implemented. My code isn't perfect right now, and I can probably clean it up some, although it could be very complicated and it's not too inefficient right now.
One thing I still do not fully understand is the best way to implement the height corrections when you add and balance your tree. It's complex, although if I used a flag to say which way I was moving in my recursive add function it may have made things easier. Balancing is probably less complicated, but still complicated enough that I just ignored it and made a function to fix the heights of the entire tree automattically (I call that fix height funtion at the appropriate times).
One of the largest problems I faced was getting the heights of the binary trees correct. I ended up just having to go through my algorithm line by line and write out my debug session on paper to figure it out. I finally did. I also had a heck of a time getting that AVL functionality to work. The largest problem there was correctly balancing. I was also having so much trouble with the heights I just wrote a function that fixed the heights of every element in the binary tree -- with my implementation it made it a million times easier and significantly reduced the complexity of my 'add' and 'balance' functions.
I liked that you went over the unicode function in class. That helped a lot and I would definitely do that again in the future.
