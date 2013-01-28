import sys
import getopt
import hashtable

def search(word,dic): #searches dic for word and for word.reverse()
    print(word)
    found = dic.find(word)
    if found != -1:
        print("I found the word '" + word + "'!")
    found = dic.find(word[::-1])
    if found != -1:
        print("I found the word '" + word[::-1] + "'!")


def main():
    args = str(sys.argv)
    optlist, args = getopt.getopt(args,':')
    args = args.replace("[","").replace("]","").replace("'","").replace(" ","")
    arglist = args.split(',')

    #read in file argument (which is the word matrix) and print the matrix as well
    infile = open(arglist[1],'r')
    matrix = []
    line = infile.readline()
    while line != '':
        print(line[:-1]) #print the matrix
        matrix.append(line[:-1]) #dont include the eol char
        line = infile.readline()
    nrows = len(matrix[0])
    ncol = len(matrix)
    print("Matrix is {} by {}".format(nrows,ncol))
    infile.close()

    #load the dictionary into the hash table
    print("Loading the dictionary...")
    dic = hashtable.Hashtable() #create hash table
    #infile = open('/usr/share/dict/american-english','r')
    infile = open('my_dict','r')
    line = infile.readline()
    while line != '':
        #print(line[:-1])
        dic.insert(line[:-1])
        line = infile.readline()
    infile.close()

    #search the matrix for words in the dictionary
    print("Dictionary loaded. Searching for words...")
    for c in range(0,ncol): #this loop searches for horizontal words DONE
        for i in range(0,nrows-1):
            for j in range(i+2,nrows+1):
                #print("{},{}".format(i,j))
                search(matrix[c][i:j],dic)
    for r in range(0,nrows): #this loop searches for vertical words DONE
        word = ''
        for c in range(0,ncol): #this loop creates the word
            word = word + matrix[c][r] 
        for i in range(0,ncol-1): #ncol = len(word) so i use that instead
            for j in range(i+2,ncol+1):
                print("{},{}".format(i,j))
                search(word[i:j],dic)

    for k in range(0,ncol): #these next 4 for loops are for the diagonal cases
        word = ''
        j = k
        i = 0
        while (j < ncol and i < nrows):
            word = word + matrix[i][j]
            i = i + 1
            j = j + 1
        search(word)
    for k in range(0,nrows):
        word = ''
        j = k
        i = 0
        while (j < nrows and i < ncol):
            word = word + matrix[j][i]
            i = i + 1
            j = j + 1
        search(word)
    for k in range (0,ncol):
        word = ''
        j = ncol - k - 1
        i = 0
        while (j > 0 and i < nrows-1):
            word = word + matrix[j][i]
            i = i + 1
            j = j - 1
        search(word)
    for k in range(0,nrows):
        word = ''
        j = nrows -k - 1
        i = 0
        while (j < nrows-1 and i < ncol):
            word = word + matrix[j][i]
            i = i + 1
            j = j -1
        search(word)





    return None


if __name__ == "__main__":
    main()
