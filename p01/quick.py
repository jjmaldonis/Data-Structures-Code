# note that in the algorithm we move from left to right, so j represents the spot to the right of where we will split the list and insert the pivot. that help to concepualize this and better understand what's going on.
import random

def quick(list):
    if(len(list) <= 1):
        return list
    #set the pivot to the last element
    pivot = -1
    i = 0
    #iterate through the entire list except the pivot (which is the last thing)
    for j in range(len(list)-1):
        if list[j] <= list[pivot]:
            list[i], list[j] = list[j], list[i] #swap
            i = i + 1
    #switch the pivot with i
    list[i], list[pivot] = list[pivot], list[i] 
    #now the pivot is in the correct spot with everything to its left lower than it and everything to its right higher than it

    #sort the left and sides of the pivot
    list_left = quick(list[:i])
    list_right = quick(list[i+1:])
    #return the sorted left side + pivot + sorted right side
    return list_left + [list[i]] + list_right

def main():
    list = range(100)
    random.shuffle(list)
    print ("Shuffled list: {0}".format(list) )
    print( "running quick sort" )
    list = quick(list)
    print ("Sorted list: {0}".format(list) )

if __name__ == "__main__":
    main()
