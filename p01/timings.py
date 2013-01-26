import random
import time
import quick
import insertion
import merge

def time_merge(l):
    start = time.time()
    merge.merge_sort(l)
    elapsed = time.time() - start
    print ('  Merge sort     took %.08f sec.' % elapsed )

def time_quick(l):
    start = time.time()
    quick.quick(l)
    elapsed = time.time() - start
    print ('  Quick sort     took %.08f sec.' % elapsed )

def time_insertion(l):
    start = time.time()
    insertion.insertion(l)
    elapsed = time.time() - start
    print ('  Insertion sort took %.08f sec.' % elapsed )

def time_pythonsort(l):
    start = time.time()
    insertion.insertion(l)
    elapsed = time.time() - start
    print ('  Python\'s sort  took %.08f sec.' % elapsed )


def sorts_on_list(l):
    lst = l
    time_merge(lst)
    lst = l
    time_quick(lst)
    lst = l
    time_insertion(lst)
    lst = l
    time_pythonsort(lst)
    print

def random_0to100(size):
    print( "List is shuffled numbers from 0 to {0}.".format(size) )
    l = range(size)
    random.shuffle(l)
    sorts_on_list(l)

def inorder_0to100(size):
    print( "List is numbers from 0 to {0} in order.".format(size) )
    l = range(size)
    sorts_on_list(l)

def reverse_0to100(size):
    print( "List is numbers from 0 to {0} in reverse order.".format(size) )
    l = range(size)
    l.reverse()
    sorts_on_list(l)

def same_nums(size):
    print( "List is {0} 5\'s.".format(size) )
    l = [5] * size
    sorts_on_list(l)

def main():
    random_0to100(100)
    inorder_0to100(100)
    reverse_0to100(100)
    same_nums(100)

    random_0to100(500)
    inorder_0to100(500)
    reverse_0to100(500)
    same_nums(500)


if __name__ == "__main__":
    main()
