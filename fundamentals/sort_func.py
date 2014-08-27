#! usr/bin/env python

import sys

def main():
    a= ['James', 'ball', 'jsason', 'shelock', 'Bryan']
    print a

    a = sorted(a, reverse=True)
    print a

    print 'Using key'
    print sorted(a, key = len)

    sort1 = sorted(a , key=str.lower)
    print 'Small Case' ,sort1
if __name__ == '__main__':
    main()
