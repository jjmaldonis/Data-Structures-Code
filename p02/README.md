#Project Description
This project solves a word search for you! It searches through the /usr/share/dict/american-english-insane dictionary for comparisons.

#Code Description
This code re-implements Python's hash functionality, hashes the /usr/share/dict/american-english-insane dictionary into the hash table, searches through a word search you pass, and prints any words it finds.

#Execution Instructions
First prepare a word search and storing it in a file. When you write the word search, each character must be lowercase, each row should be on a new line, and you should not include spaces between the characters. You can also just use one of my matrices as well (matrix2 is the best). You then execute the code by calling 'python solver.py [your word search file]'. Note that you can also pass the dictionary you want it to read. If a dictionary is not passed, the program defaults to the american-insane as specified above.

#Reflection
The most interesting thing I learned was definitely how to implement the hash functionality. I enjoyed doing this because I had never done it before and I can now understand a hash table's usefulness. The only the thing I don't like about hash tables is that you have to rehash the entire thing when you need to grow. If you have some idea of how big the hash table should be to start with however you can avoid the rehash functionality by changing the initial hash table size.
You mentioned that Python's hash function can actually return a negative value, but our implementation does not allow that. I do not understand how exactly Python's hash function works then, and I would be curious to find out.
The biggest problem I faced was implementing the matrix search to get every possible combination of letters (in a row) correctly. After talking to you and understanding that using a type of 'movement vector' for each search direction was the best option I was able to correctly write the code (after plenty of debugging).
I would tell someone starting this project not to use the insane dictionary, but rather to make their own. Find a word search online and copy it into a file and put their words to find into your dictionary. Then run the program on that word search with that dictionary. This way the dictionary loads quickly and you can easily check that it is finding all the words. Also, I would tell them (like you told us) to make sure you get the hash table working first and start with the simple insertion (not perturbed) before moving on to the word search.


Notes: Python's hash function is
def hash(x):
    return x & (2^i-1) #where 2^i is the size of the hash table
because as long as the size is a power of 2, the above bit operation does the same thing as mod but its way faster.
The collision cases are explained in svn.python.org/view/python/trunk/Objects/dictobject.c?view=markup#l87 (scroll up a bit for the simpler case that they modified a bit with perturb to make it better).
