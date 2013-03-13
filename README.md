refreshx2
=========
Hashtables:
    Wastes space.
    Does need keep things in sorted order.
    You have to make a good hashfuntion - this can make things fast / optimized if you want to optimize for your data. Python's is good though in general.
    Insertion is fast.

Binary Search Tree:
    log N lookup time.
    Sorted order.

Array:
    Can keep in sorted order.
    log N lookup time by looking at the middle element each time.
    Insertion is slow.
    Deletion in the middle is slow (at the beginning as well but you can get around this by having a designated starting point, you just then may have trouble growing the array).

B-Tree:
    Array implementation of a binary tree. This is very useful when you can't store the entire binary tree data structure in memory.

