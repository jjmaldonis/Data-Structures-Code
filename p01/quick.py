import random

def quick(list):
    if(len(list) <= 1):
        return list
    pivot = -1 #set the pivot to the last element
    i = 0
    for j in range(len(list)-1): #iterate through the entire list except the pivot (which is the last thing)
        if list[j] <= list[pivot]:
            list[i], list[j] = list[j], list[i] #swap
            i = i + 1
    list[i], list[pivot] = list[pivot], list[i] #switch the pivot with i
    #now the pivot is in the correct spot with everything to its left lower than it and everything to its right higher than it
    list_left = quick(list[:i]) #sort the left side of the pivot
    list_right = quick(list[i+1:]) #sort the right side of the pivot
    return list_left + [list[i]] + list_right #return the sorted left side + pivot + sorted right side

def main():
    list = range(100)
    random.shuffle(list)
    print ("Shuffled list: {0}".format(list) )
    list = quick(list)
    print ("Sorted list: {0}".format(list) )

if __name__ == "__main__":
    main()
