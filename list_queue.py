#! usr/bin/env python

import sys
from collections import deque

def f(x): return x % 2 != 0 and x % 3 !=0

def main():

    queue = deque(["James", "Sherlock", "Bryan"])
    print queue
    queue.append("Arrow")
    print queue

    queue.popleft()
    print queue

if __name__ == '__main__':
    main()
