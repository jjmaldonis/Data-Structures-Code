
import random

def merge_sort(l):
    print ("In merge_sort")
    if len(l) <=1:
        return l
    left = l[0:len(l)/2]
    right = l[len(l)/2:]

    left = merge_sort(left)
    print (left)
    right = merge_sort(right)
    print (right)
    return merge(left,right)

def merge(left,right):
    print ("In merge")
    final = []
    while len(left) > 0 or len(right) > 0:
        if len(left) > 0 and len(right) > 0:
            if left[0] <= right[0]:
                final.append(left[0])
                left.pop(0)
            else:
                final.append(right[0])
                right.pop(0)
        elif len(left) > 0:
            final.append(left[0])
            left.pop(0)
        elif len(right) > 0:
            final.append(right[0])
            right.pop(0)
    return final


def main():
    l = range(10)
    random.shuffle(l)
    print ( "Before Sort: {0}".format(l) )
    l = merge_sort(l)
    print( "After Sort: {0}".format(l) )

if __name__ == '__main__':
    main()
