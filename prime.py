#! usr/bin/env python

import sys

def main():
    print 'Prime'
    for n in range(2, 10):
        print 'N= ',n
        for x in range(2, n):
            print 'X= ',x
            if n % x == 0:
                print n, 'NOT PRIME'
                break
        else:
            print n, 'PRIME NUMBER'
if __name__ == '__main__':
    main()
