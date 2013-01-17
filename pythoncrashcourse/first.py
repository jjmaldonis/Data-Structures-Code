
#I can write the below lane and then execute this script by typing "./first.py" in the terminal:
##!/usr/bin/env python

# first.py --- my first python file

import sys
import getopt

#import argparse #this module does parsing from the command line too but i didn't take the time to really figure it out

#the following for lines parse the arguments given in the termal into a list called arglist; the elements of arglist are all str's
args = str(sys.argv)
optlist, args = getopt.getopt(args,':')
args = args.replace("[","").replace("]","").replace("'","").replace(" ","")
arglist = args.split(',')

def fib(x):
    if x <= 2:
        return 1
    return fib(x-1) + fib(x-2)

print fib(int(arglist[1]))



#some notes:
#if you want to copy list x you can do:
#   x = [1,2,3]
#   y = x[:]
#   now you can modify x without changing y (whereas if you said y = x then changing x would chage y)
#
#   now try some stuff by setting x = 'donaldcurtis'
#   x[1:-1]
#   x[3:]
#   x[:-1]
#   x[0::2] #this will skip every other character
