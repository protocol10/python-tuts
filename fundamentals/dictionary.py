#! usr/bin/env python

import sys

def main():
    
    tel = {'Guido': 2568, 'Jack': 2568, 'James': 3666, 'Frank':2568}
    print tel

    tel['Snape'] = 2568
    print tel

    del tel['Jack']
    print tel

    if 'James' in tel:
        print  'James is present'
    else:
        print 'Incorrect No'

    print 'Using Dict Constructor'

    dictionary = dict(james = 25, sherlock = 26, arrow = 27)
    print dictionary

    print 'Using List comprehension'

    dict_comp = {x:x**2 for x in (1, 2, 3)}
    print dict_comp

    print 'looping in traditional way'

   #value is similar to tel.keys() and tel[value] is similar to tel.value() 
    for value in tel:
        print value, 'is',tel[value]

    print 'using enumerate function'
    for index, key in enumerate(tel):
        print index, key

    print 'Using iteritems'
    for key,value in tel.iteritems():
        print key,value

if __name__ == '__main__':
    main()
