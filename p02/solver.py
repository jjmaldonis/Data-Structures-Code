""" Implements a word search given an input word search text file and an optional dictionary (otherwise it will use a default dictionary). """

import time
import sys
import getopt
import hashtable

PERTURB_SHIFT = 5


def search(word, dic):
    """ Searches dic for word and for word.reverse().
    Returns 0 if found forward, returns 1 if found in reverse.
    """
    found = dic.find(word)
    if found != -1:
        print(word)
        return 0
    found = dic.find(word[::-1])
    if found != -1:
        print(word[::-1])
        return 1


def main():
    """ main function reads in a matrix and performs the word search algorithm """
    start = time.time()
    #Read in file argument (which is the word matrix) and print the matrix as well.
    infile = open(sys.argv[1], 'r')
    matrix = []
    line = infile.readline()
    if (line == ''):
        #If the input word maxtrix was blank
        return None
    while line != '':
        line = line.replace(" ", "")
        #Don't include the eol character in the line when we put it into the matrix
        matrix.append(line[:-1])
        line = infile.readline()
    nrows = len(matrix[0])
    ncol = len(matrix)
    time.sleep(.1)
    infile.close()

    #Load the dictionary into the hash table
    dic = hashtable.Hashtable()
    if len(sys.argv) > 2:
        infile = open(sys.argv[2], 'r')
    else:
        infile = open('/usr/share/dict/american-english-insane', 'r')
    line = infile.readline()
    while line != '':
        dic.insert(line[:-1])
        line = infile.readline()
    infile.close()

    #Search the matrix for words in the dictionary
    deltaHoriz = [0,1]
    deltaVert = [1,0]
    deltaDiagLtoR = [1,1]
    deltaDiagRtoL = [1,-1]
    for c in range(0, ncol):
        for r in range(0, nrows):
            #These next 8 variables are the row and column that we are at for each direction we could search (horizontal, vertical, diagonal left to right, and diagonal right to left)
            horiz = [c,r]
            vert = [c,r]
            diagLtoR = [c,r]
            diagRtoL = [c,r]
            #These are the words that will be searched for / are added to as we increment through the word matrix
            h_word = matrix[c][r]
            v_word = matrix[c][r]
            dlr_word = matrix[c][r]
            drl_word = matrix[c][r]
            for _ in range(c, ncol):
                for _ in range(r, nrows):
                    if (horiz[0] + 0 < ncol and horiz[1] + 1 < nrows):
                        #If the next horizontal spot is not out of range then move in the direction we should move for the horizontal word (0 down, 1 right)
                        horiz[0] = horiz[0] + deltaHoriz[0]
                        horiz[1] = horiz[1] + deltaHoriz[1]
                        #Add the character onto the word and then search for the new word (this searches forward and backward)
                        h_word = h_word + matrix[horiz[0]][horiz[1]]
                        search(h_word, dic)
                    if (vert[0] + 1 < ncol and vert[1] + 0 < nrows):
                        #If the next vertical spot is not out of range we do very similar things.
                        vert[0] = vert[0] + deltaVert[0]
                        vert[1] = vert[1] + deltaVert[1]
                        v_word = v_word + matrix[vert[0]][vert[1]]
                        search(v_word, dic)
                    if (diagLtoR[0] + 1 < ncol and diagLtoR[1] + 1 < nrows):
                        #If the next diagonal left to right spot is not out of range we do very similar things.
                        diagLtoR[0] = diagLtoR[0] + deltaDiagLtoR[0]
                        diagLtoR[1] = diagLtoR[1] + deltaDiagLtoR[1]
                        dlr_word = dlr_word + matrix[diagLtoR[0]][diagLtoR[1]]
                        search(dlr_word, dic)
                    if (diagRtoL[0] + 1 < ncol and diagRtoL[1] - 1 >= 0):
                        #If the next diagonal right to left sopt is not out of range we do very similar things.
                        diagRtoL[0] = diagRtoL[0] + deltaDiagRtoL[0]
                        diagRtoL[1] = diagRtoL[1] + deltaDiagRtoL[1]
                        drl_word = drl_word + matrix[diagRtoL[0]][diagRtoL[1]]
                        search(drl_word, dic)

    end = time.time()
    print("Program took {0} seconds to run.".format(end - start))
    return None


if __name__ == "__main__":
    main()
