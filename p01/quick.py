# Note that in the algorithm we move from left to right, so j represents the spot to the right of where we will split the list and insert the pivot. that help to concepualize this and better understand what's going on.
import random

def quick(list):
    if(len(list) <= 1):
        return list

    # Set the pivot to the last element
    pivot = -1
    i = 0

    # Iterate through the entire list except the pivot (which is the last thing)
    for j in range(len(list)-1):
        if list[j] <= list[pivot]:
            list[i], list[j] = list[j], list[i] #swap
            i = i + 1

    # Switch the pivot with i
    list[i], list[pivot] = list[pivot], list[i] 
    # Now the pivot is in the correct spot with everything to its left lower than it and everything to its right higher than it

    # Return the sorted left side + pivot + sorted right side
    return quick(list[:i]) + [list[i]] + quick(list[i+1:])

def main():
    list = range(100)
    random.shuffle(list)
    print ("Shuffled list: {0}".format(list) )
    list = quick(list)
    print ("Sorted list after Quicksort: {0}".format(list) )

if __name__ == "__main__":
    main()
