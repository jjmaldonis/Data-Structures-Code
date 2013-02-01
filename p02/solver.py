import time
import sys
import getopt
import hashtable

PERTURB_SHIFT = 5

def search(word,dic): #searches dic for word and for word.reverse(). returns 0 if found forward, returns 1 if found in reverse
    found = dic.find(word)
    if found != -1:
        print(word)
        return 0
    found = dic.find(word[::-1])
    if found != -1:
        print(word[::-1])
        return 1


def main():
    args = str(sys.argv)
    optlist, args = getopt.getopt(args,':')
    args = args.replace("[","").replace("]","").replace("'","").replace(" ","")
    arglist = args.split(',')

    #read in file argument (which is the word matrix) and print the matrix as well
    infile = open(arglist[1],'r')
    matrix = []
    line = infile.readline()
    if (line == ''): #if the input word matrix was blank
        return None
    while line != '':
        matrix.append(line[:-1]) #dont include the eol char
        line = infile.readline()
    nrows = len(matrix[0])
    ncol = len(matrix)
    #print("Matrix is {} by {}".format(nrows,ncol))
    time.sleep(.1)
    infile.close()

    #load the dictionary into the hash table
    #print("Loading the dictionary...")
    dic = hashtable.Hashtable() #create hash table
    infile = open('/usr/share/dict/american-english-insane','r')
    #infile = open('my_dict','r')
    line = infile.readline()
    while line != '':
        dic.insert(line[:-1])
        line = infile.readline()
    infile.close()

    #search the matrix for words in the dictionary
    for c in range(0,ncol):
        for r in range(0,nrows):
            #these next 8 variables are the row and column that we are at for each direction we could search (horizontal, vertical, diagonal left to right, and diagonal right to left)
            h_c = c
            h_r = r
            v_c = c
            v_r = r
            dlr_c = c
            dlr_r = r
            drl_c = c
            drl_r = r
            #these are the words that will be searched for / are added to as we increment through the word matrix
            h_word = matrix[c][r]
            v_word = matrix[c][r]
            dlr_word = matrix[c][r]
            drl_word = matrix[c][r]
            for x in range(c, ncol):
                for y in range(r,nrows):
                    if (h_c + 0 < ncol and h_r +1 < nrows): #if the next horizontal spot is not out of range:
                        h_c = h_c + 0 #move in the direction we should move for the horizontal word (0 down, 1 right)
                        h_r = h_r + 1
                        h_word = h_word + matrix[h_c][h_r] #add onto the word
                        search(h_word,dic) #search for the word (this searches forward and back)
                    if (v_c + 1 < ncol and v_r +0 < nrows): #if the next vertical spot is not out of range:
                        v_c = v_c + 1
                        v_r = v_r + 0
                        v_word = v_word + matrix[v_c][v_r]
                        search(v_word,dic)
                    if (dlr_c + 1 < ncol and dlr_r +1 < nrows): #if next diagonal left to right spot is not out of range:
                        dlr_c = dlr_c + 1
                        dlr_r = dlr_r + 1
                        dlr_word = dlr_word + matrix[dlr_c][dlr_r]
                        search(dlr_word,dic)
                    if (drl_c + 1 < ncol and drl_r -1 >= 0): #if the next diagonal right to left spot is not out of range:
                        drl_c = drl_c  + 1
                        drl_r = drl_r  - 1
                        drl_word = drl_word + matrix[drl_c][drl_r]
                        search(drl_word,dic)

    return None


if __name__ == "__main__":
    main()
