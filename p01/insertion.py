#if you import this module you can type help(insertion) and it will give you the help info below
"""
insertion sort

script that demonstrates implementation of insertion sort.
"""

import random

def insertion(l):
    """
    implements insertion sort

    pass it a list, list will be modified in plase
    """

    for i in range(1,len(l)):
        for j in range(0,i):
            if l[i] < l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
                #l[j], l[i] = l[i], l[j] #this is the same thing in one line
    return l

def main():
    l = range(100)
    random.shuffle(l)
    print( "Before Sort: {0}".format(l) )

    insertion(l) #you don't need l =
    print( "After Sort: {0}".format(l) )

if __name__ == "__main__":
    main()
