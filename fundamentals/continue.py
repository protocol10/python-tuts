#! usr/bin/env python

import sys

def main():
    print 'Test'

    letter ='Django'

    for l in letter:
        if l == 'D':
            continue
        print 'Letter is ', l

    for i in range(1,10):
        if i % 2 == 0:
           # print 'Number', i,' is even'
            continue
        print 'Number',i ,' is odd'
if __name__ == '__main__':
    main()
