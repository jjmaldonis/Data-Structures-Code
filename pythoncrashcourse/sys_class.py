
import sys
import getopt
import fileinput


def main():
    args = str(sys.argv)
    print(len(sys.argv))
    print(sys.argv)
    optlist, args = getopt.getopt(args,':')
    args = args.replace("[","").replace("]","").replace("'","").replace(" ","")
    arglist = args.split(',')

    for line in fileinput.input():
        print(line)
    print(fileinput.filename())

    return None


if __name__ == "__main__":
    main()
