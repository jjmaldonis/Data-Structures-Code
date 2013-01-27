import random
import time
import quick
import insertion
import merge

def time_merge(l):
    start = time.time()
    merge.merge_sort(l)
    return time.time() - start
    #print ('  Merge sort     took %.08f sec.' % elapsed )

def time_quick(l):
    start = time.time()
    quick.quick(l)
    return time.time() - start
    #print ('  Quick sort     took %.08f sec.' % elapsed )

def time_insertion(l):
    start = time.time()
    insertion.insertion(l)
    return time.time() - start
    #print ('  Insertion sort took %.08f sec.' % elapsed )

def time_pythonsort(l):
    start = time.time()
    insertion.insertion(l)
    return time.time() - start
    #print ('  Python\'s sort  took %.08f sec.' % elapsed )


def sorts_on_list(l):
    runs = 100
    avg_time = 0
    for i in range(0,runs):
        lst = l
        avg_time = avg_time + time_merge(lst)
    avg_time = avg_time/runs
    print ('  Avg of {0} Merge sorts     took {1:.08f} sec.'.format(runs,avg_time))

    avg_time = 0
    for i in range(0,runs):
        lst = l
        avg_time = avg_time + time_quick(lst)
    avg_time = avg_time/runs
    print ('  Avg of {0} Quick sorts     took {1:.08f} sec.'.format(runs,avg_time))
        
    avg_time = 0
    for i in range(0,runs):
        lst = l
        avg_time = avg_time + time_insertion(lst)
    avg_time = avg_time/runs
    print ('  Avg of {0} Insertion sorts took {1:.08f} sec.'.format(runs,avg_time))
    
    avg_time = 0
    for i in range(0,runs):
        lst = l
        avg_time = avg_time + time_pythonsort(lst)
    avg_time = avg_time/runs
    print ('  Avg of {0} Python\'s sorts  took {1:.08f} sec.'.format(runs,avg_time))

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

def few_shuffled(size):
    print( "List is numbers from 0 to {0} with a few shuffled.".format(size))
    l = range(0,size)
    for i in range(0,size/10):
        one = random.randrange(0,size)
        two = random.randrange(0,size)
        l[one],l[two] = l[two],l[one]
    sorts_on_list(l)

def few_unique(size):
    print( "List is numbers from 0 to {0} with a few numbers replaced with the number 0 (list is unshuffled).".format(size))
    l = range(0,size)
    for i in range(0,size/10):
        l[random.randrange(0,size)] = 0
    sorts_on_list(l)

def few_unique_shuffled(size):
    print( "List is numbers from 0 to {0} with a few numbers replaced with the number 0 (list is shuffled).".format(size))
    l = range(0,size)
    random.shuffle(l)
    for i in range(0,size/10):
        l[random.randrange(0,size)] = 0
    sorts_on_list(l)



def main():
    random_0to100(100)
    inorder_0to100(100)
    reverse_0to100(100)
    same_nums(100)
    few_shuffled(100)
    few_unique(100)
    few_unique_shuffled(100)

    print

    random_0to100(500)
    inorder_0to100(500)
    reverse_0to100(500)
    same_nums(500)
    few_shuffled(500)
    few_unique(500)
    few_unique_shuffled(100)



if __name__ == "__main__":
    main()
