#insertion -- impletments insertion sort

def insertion(l):
    print ("in insertion function")
    for i in range(1,len(l)):
        for j in range(0,i):
            if l[i] < l[j]:
                tmp = l[i]
                l[i] = l[j]
                l[j] = tmp
    return l

def main():
    l = [6,7,24,1,18,23,4]
    #l = [9,7,4,2]
    print( "Before Sort: {0}".format(l) )

    l = insertion(l)
    print( "After Sort: {0}".format(l) )

if __name__ == "__main__":
    main()
