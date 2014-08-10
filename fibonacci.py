#! usr/bin/env python

import sys

def main():
    a, b = 0, 1
    while b < 10:
        a, b = b, a+b
#        print a
#        print 'a'
        print b
if __name__ == '__main__':
    main()
