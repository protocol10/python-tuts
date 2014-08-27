#! usr/bin/env python

import sys

def main():
    x = raw_input('Please Enter Integer Value')

    if x < 0:
        print 'It is zero'
    elif x > 0:
        print 'It is greater than zero'
    elif x == 40 :
        print 'Bingo'
    else:
        print 'Illegal entry'

    words = ['Akshay', 'Sukhada', 'Harshada', 'Sonali', 'Samit', 'Deepti', 
            'Deepti', 'Deepali', 'Prathamesh']

    print 'For loop '
    for w in words:
        print 'Name:' ,w ,'Length:', len(w)
        if 'Sukhada' and 'Akshay' in w:
            print 'Bingo'
    #New way Complex statements
    print 'Complex Stuff'
    for w in words: print 'bingo' if w == 'Akshay' or w == 'Sukhada' else None

if __name__ == '__main__':
    main()
