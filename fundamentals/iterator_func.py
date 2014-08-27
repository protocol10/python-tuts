#! usr/bin/env python

import sys

class Counter:

    def __init__(self, low, high):
        self.high = high
        self.current = low

    def __iter__(self):
        return self

    def next(self):
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1

for c in Counter(3, 6):
    print c
