#! usr/bin/env python

import sys

def main():

    print 'Printing Stack'

    stack = [2, 3, 6]

    stack.append(63)
    stack.append(81)

    print stack

    stack.pop()
    print 'Stack is pop', stack

    print 'Queue starts'

if __name__ == '__main__':
    main()
