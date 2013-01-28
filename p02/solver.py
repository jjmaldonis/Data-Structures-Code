import sys
import getopt
import hashtable

def search(word,dic): #searches dic for word and for word.reverse()
    #print(word)
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
    for c in range(0,ncol):
        for r in range(0,nrows):
            print('Reset')
            h_c = c
            h_r = r
            v_c = c
            v_r = r
            dlr_c = c
            dlr_r = r
            drl_c = c
            drl_r = r
            h_word = matrix[c][r]
            v_word = matrix[c][r]
            dlr_word = matrix[c][r]
            drl_word = matrix[c][r]
            for x in range(c, ncol):
                for y in range(r,nrows):
                    if (h_c + 0 < ncol and h_r +1 < nrows):
                        h_c = h_c + 0
                        h_r = h_r + 1
                        h_word = h_word + matrix[h_c][h_r]
                        #print(h_word)
                        search(h_word,dic)
                    if (v_c + 1 < ncol and v_r +0 < nrows):
                        v_c = v_c + 1
                        v_r = v_r + 0
                        v_word = v_word + matrix[v_c][v_r]
                        #print(v_word)
                        search(v_word,dic)
                    if (dlr_c + 1 < ncol and dlr_r +1 < nrows):
                        dlr_c = dlr_c + 1
                        dlr_r = dlr_r + 1
                        dlr_word = dlr_word + matrix[dlr_c][dlr_r]
                        #print(dlr_word)
                        search(dlr_word,dic)
                    if (drl_c + 1 > ncol and drl_r -1 > nrows):
                        drl_c = drl_c  + 1
                        drl_r = drl_r  - 1
                        drl_word = drl_word + matrix[drl_c][drl_r]
                        print(drl_word)
                        search(drl_word,dic)






    return None


if __name__ == "__main__":
    main()
